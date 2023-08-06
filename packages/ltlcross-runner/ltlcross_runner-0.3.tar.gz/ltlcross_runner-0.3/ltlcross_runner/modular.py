# Copyright (c) 2019 Fanda Blahoudek
"""
@author: fblahoudek
"""

import csv
import math
import os
import subprocess as sp
import time
import random
from ltlcross_runner.ltlcross_runner import LtlcrossRunner

def _renumber_formula(line, increase):
    """Increase formula id on the given ltlcross-log line

    Parameters
    ==========
    `line` — line from ltlcross log with formula to be translated.
    `increase` — number of which we should increase the formula id
    """
    splitted = line.split(":")
    splitted[1] = str(int(splitted[1]) + increase)
    return ":".join(splitted)

def id_to_str(i, pad_length=2):
    return str(i).zfill(pad_length)

class modulizer():
    """Split a big ltlcross task into smaller ones that can
    be executed separately, and merge the results into one
    final `.csv` file with results and one `.log` file.
    
    Expected use:
    m = modulizer(parameters)
    m.run()
    
    When resuming an interupted computation, delete `.log` files
    of not-finished jobs (such that no `.csv` file exists).
    
    Parameters
    ==========
     * `name` : str — name of the job
     * `tools` : dict — dictionary with tools config passed to LtlcrossRunner
     * `formula_file` : str — path to file to split
     * `chunk_size` : int — number of formulas in one chunk
     * `tmp_dir` : str — directory to perform (or continue) computations
     * final output files (all are `{name}.ext` by default):
       - out_res_file (`.csv`, final results)
       - out_log_file (`.log`, merged logs)
       - out_bogus_file (`_bogus.ltl`, merged bogus formulae)
    """
    def __init__(self, name, tools,
                 formula_file, chunk_size,
                 tmp_dir=None,
                 out_res_file=None, out_log_file=None, out_bogus_file=None):
        self.name = name
        self.tools = tools
        self.chunk_size = chunk_size
        self.formula_file = formula_file

        # Set the tmp dirs
        self.tmp_dir = f"{name}.parts" if tmp_dir is None else tmp_dir
        if not os.path.isdir(self.tmp_dir):
            os.mkdir(self.tmp_dir)

        self.prefix = f"{self.tmp_dir}/{name}"

        # Set output files names
        self.out_res_file = f"{name}.csv" if \
            out_res_file is None else out_res_file
        self.out_log_file = f"{name}.log" if \
            out_log_file is None else out_log_file
        self.out_bogus_file = f"{name}_bogus.ltl" if \
            out_bogus_file is None else out_bogus_file

        # Get the count of chunks
        length = sum(1 for line in open(self.formula_file))
        self.chunks = math.ceil(length/self.chunk_size)
        
    def get_res_name(self, part):
        return f"{self.prefix}-{id_to_str(part)}.csv"

    def get_ltl_name(self, part):
        return f"{self.prefix}-{id_to_str(part)}.ltl"
    
    def get_log_name(self, part):
        return f"{self.prefix}-{id_to_str(part)}.log"
    
    def is_splitted(self):
        """Check if the task is already splitted.
        
        Return `False` if even the first file is not created.
        Return `True` if the last file is created.
        Raises `ValueError` if more files than expected are
           already present in the tmp_dir.
           
        Sleeps for 5ms after detection of the 1st file to give
        enough time if another process is doing the splitting
        already.
        """
        too_much = self.get_ltl_name(self.chunks)
        start = self.get_ltl_name(0)
        end = self.get_ltl_name(self.chunks - 1)
        if os.path.isfile(too_much):
            raise ValueError(f"The tmp_dir {self.tmp_dir} already contains "
                             + "more files than expected. Remove them first!")
        if not os.path.isfile(start):
            return False
        time.sleep(.05)
        return os.path.isfile(end)

    def split_task(self):
        """Split the formulas for the given task into smaller files,
        each containing `chunk_size` formulas.
        
        The last part can contain less formulas.
        """
        in_f = open(self.formula_file, "r")

        ## Create all files but last (which can be shorter) ##
        for i in range(self.chunks - 1):
            out_f = open(self.get_ltl_name(i),"w")
            for j in range(self.chunk_size):
                line = in_f.readline()
                print(line, file = out_f, end='')
            out_f.close()

        ## Create the last file ##
        i = self.chunks - 1 # We start with 0
        out_f = open(self.get_ltl_name(i),"w")
        for line in in_f:
            print(line, file=out_f, end='')
        out_f.close()

        in_f.close()

    def is_started(self, part):
        """Returns True for parts which have their `.log` file
        already created.
        """
        return os.path.isfile(self.get_log_name(part))

    def part_done(self, part=None):
        """Check if the given part is done.
        
        Checks if all parts are done if `part` not specified.
        
        The check looks for file `prefix-ii.csv`.
        """
        if part is not None:
            return os.path.isfile(self.get_res_name(part))

        ## else Check all parts
        for i in range(self.chunks):
            if not self.part_done(i):
                return False
        return True

    def next_job(self):
        """Return the next job to be done.

        Return:
            * 'done' if the final result file is created
            * 'split' if the formula file is not splitted yet,
            * id of the first job not started yet,
            * 'merge' if all parts done but not merged,
            * `None` otherwise.
            
        Wait for a random time to avoid some duplicate work with
        simple paralization.
        """
        delay = random.random()
        time.sleep(delay)
        
        # all done?
        if self.is_merged():
            return "done"
        
        # Split needed?
        if not self.is_splitted():
            return "split"
        
        # Detect jobs not started yet
        for i in range(self.chunks):
            if not self.is_started(i):
                return i

        # Merge if all parts are finished but not merged
        if self.part_done() and not self.is_merged():
            return "merge"

        # Else nothing
        return None

    def is_merged(self):
        """Check if the final result file is created."""
        return os.path.isfile(self.out_res_file)

    def run_part(self, part):
        res_file  = self.get_res_name(part)
        form_file = self.get_ltl_name(part)
        r = LtlcrossRunner(self.tools, [form_file], res_file)
        r.run_ltlcross()

    def merge_parts(self):
        m = merger(self.prefix, self.prefix, 
                   self.chunks, self.chunk_size,
                   self.out_res_file, self.out_log_file, 
                   self.out_bogus_file)
        m.merge_files()
        
    def _work_next(self):
        job = self.next_job()
        if job is None:
            return False
        print(job)
        if job == "done":
            return False
        if job == "split":
            self.split_task()
            return True
        if job == "merge":
            self.merge_parts()
            return True
        self.run_part(job)
        return True
    
    def run(self):
        while self._work_next():
            pass


class merger():
    """Merge `.csv`, `.log`, and `_bogus.ltl` files from partial runs
    of ltlcross into aggregated files.

    Expects the files to be named:
      * `{prefix}-ii.csv`, and
      * `{prefix}-ii.log`
      * `{prefix}-ii_bogus.ltl`

    Parameters:
    ===========
    * `prefix` — path prefix (including directories) to files to merge

    * `formula_prefix`: — path prefix to files with formulas used to compute
    intermediate results (needed to correct reunbering of formulas in `.log`
    files).

    * `chunks` — number of chunks to merge

    * `chunk_size` — number if formulas in one chunk

    * `csv_output` — path for the final results

      - will be overwritten by calling `merge_res_files()` and `merge_files()`
      - `{prefix}.csv` by default
    * `log_output` — path for the final results

      - will be overwritten by calling `merge_log_files()` and `merge_files()`
      - `{prefix}.log` by default

    * `bogus_output` — path for the final bogus-formulas file

      - will be overwritten by calling `merge_bogus()` and `merge_files()`
      - `{prefix}_bogus.ltl` by default
    """

    def __init__(self, prefix, formula_prefix,
                 chunks, chunk_size,
                 csv_output=None, log_output=None, bogus_output=None):
        self.prefix = prefix
        self.formula_prefix = formula_prefix
        self.chunks = chunks
        self.chunk_size = chunk_size

        if csv_output is None:
            self.output = f"{prefix}.csv"
        else:
            self.output = csv_output
        if log_output is None:
            self.log_output = f"{prefix}.log"
        else:
            self.log_output = log_output
        if bogus_output is None:
            self.bogus_output = f"{prefix}_bogus.ltl"
        else:
            self.bogus_output = bogus_output

        self.writer = None
        self.log_file_h = None

    ### CSV files ###
    def _print_res_header(self):
        """Write header of csv files based on given prefix.

        Uses the writer to print headers that are taken from
        the first file with given prefix:
        ```
        prefix-00.csv
        ```

        Parameters
        ==========
        `writer` : csv.writer to use
        `prefix` : str prefix of filenames to be merged
        """
        input_f = f"{self.prefix}-00.csv"
        reader = csv.reader(open(input_f, "r"))
        header_row = reader.__next__()
        self.writer.writerow(header_row)

    def _append_res_part(self, i):
        """Append rows from file `prefix-ii.csv` to writer.

        By `ii` we mean i padded to have two digits.
        """
        i_s = id_to_str(i)
        input_f = f"{self.prefix}-{i_s}.csv"
        reader = csv.reader(open(input_f, "r"))
        reader.__next__()
        self.writer.writerows(reader)

    def merge_res_files(self):
        """Merge files `prefix-00.csv` ... `prefix-chunks.csv`
        into file `prefix.csv`.
        """
        f = open(self.output, "w")
        self.writer = csv.writer(f)

        self._print_res_header()
        for i in range(self.chunks):
            self._append_res_part(i)

        f.close()

    ### LOGS ###
    def _append_log_part(self, i):
        """Apend one partial `.log` file into final log.

        Renumbers the formula ids accordingly.
        """
        increase = i * self.chunk_size
        i_s = id_to_str(i)
        formula_file = f"{self.formula_prefix}-{i_s}.ltl"
        f = open(f"{self.prefix}-{i_s}.log", "r")

        # Skip 3 lines with common info
        for i in range(3):
            f.__next__()

        for line in f:
            if line.startswith(formula_file):
                line = _renumber_formula(line, increase)
            print(line, end="", file=self.log_file_h)

        f.close()

    def merge_log_files(self):
        """Merge files `prefix-00.log` ... `prefix-chunks.log`
        into file `prefix.log`.
        """
        self.log_file_h = open(self.log_output, "w")

        # copy the first 3 lines from the 1st log file
        f = open(f"{self.prefix}-00.log", "r")
        for i in range(3):
            line = f.readline()
            self.log_file_h.writelines(line)
        f.close()

        # apppend the rest
        for i in range(self.chunks):
            self._append_log_part(i)
        self.log_file_h.close()

    ### bogus formulas ###
    def merge_bogus(self):
        """Merge files `prefix-00_bogus.ltl` ...
        into file `prefix_bogus.ltl`.
        """
        files = [f"{self.prefix}-{id_to_str(i)}_bogus.ltl" \
                 for i in range(self.chunks)]
        f_h = open(self.bogus_output, "w")
        sp.call(["cat"] + files, stdout=f_h)
        f_h.close()

    def merge_files(self):
        """Merge result, log, and bogus-formulas files."""
        self.merge_res_files()
        self.merge_log_files()
        self.merge_bogus()

    def delete_parts(self, types=[".log",".csv","_bogus.ltl"]):
        """Delete the partial results, log, and ltl files

        `types` — list of files to delete
        """
        for t in types:
            for i in range(self.chunks):
                i_s = id_to_str(i)
                input_f = f"{self.prefix}-{i_s}{t}"
                os.remove(input_f)
