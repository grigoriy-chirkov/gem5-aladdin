import os
import subprocess
import sys
import tempfile

from xenon.base.datatypes import *
from xenon.generators import base_generator
from benchmarks.datatypes import *

class RunGenerator(base_generator.Generator):
  def __init__(self, sweep):
    super(RunGenerator, self).__init__()
    self.sweep = sweep
    # Return the next sweep_id for this benchmark.
    self.next_sweep_id_ = {}

  def next_id(self, benchmark_name):
    if benchmark_name in self.next_sweep_id_:
      self.next_sweep_id_[benchmark_name] += 1
      sweep_id = self.next_sweep_id_[benchmark_name]
      return sweep_id
    else:
      self.next_sweep_id_[benchmark_name] = 0
      return 0

  def run(self):
    run_errors_fd, run_errors_path = tempfile.mkstemp()
    with open(run_errors_path, "r+") as run_errors_f:
      cwd = os.getcwd()
      genfiles = []
      for benchmark in self.sweep.iterattrvalues(objtype=Sweepable):
        assert(isinstance(benchmark, Benchmark))
        index = self.next_id(benchmark.name)
        print("Running benchmark %s" % (benchmark.name))
        run_dir = os.path.join(self.sweep.output_dir, benchmark.name)
        if not os.path.isabs(run_dir):
          run_dir = os.path.join(cwd, run_dir)
        os.chdir(run_dir)
        indexes = os.listdir(os.getcwd())
        for i in indexes:
          if i == 'inputs':
            continue
          print("Running benchmark %s:%s" % (benchmark.name, i))
          os.chdir(os.path.join(run_dir, i))
          ret = subprocess.call("sbatch run.sh",
                                stdout=run_errors_f, stderr=subprocess.STDOUT, shell=True)
          if ret:
            self.handle_error("Failed to launch the run.", run_errors_f)
          os.chdir(run_dir)

    os.chdir(cwd)
    return genfiles
