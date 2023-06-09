r"""Compares the csv generated by two runs of a benchmark.

Usage example:
  bazel run -c opt \
      //third_party/yggdrasil_decision_forests/cli/monitoring:compare_benchmark\
      -- --p1=/tmp/train_benchmark.csv --p2=/tmp/train_benchmark_new.csv
"""

from absl import app
from absl import flags
import pandas as pd

FLAGS = flags.FLAGS

flags.DEFINE_string("p1", "", "First csv file")
flags.DEFINE_string("p2", "", "Second csv file")


def main(argv) -> None:
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  d1 = pd.read_csv(FLAGS.p1)
  d2 = pd.read_csv(FLAGS.p2)
  d1["new_training_time"] = d2["training_time"]

  d1["delta"] = (d1["new_training_time"] - d1["training_time"]) / d1[
      "training_time"
  ]
  print(d1)


if __name__ == "__main__":
  app.run(main)
