import os
import json
import numpy as np
from rouge_score import rouge_scorer, scoring
DATA_DIR = os.path.join("./curated-data")

TRAIN_DS = os.path.join(DATA_DIR, "law-qa-train.jsonl")
VAL_DS = os.path.join(DATA_DIR, "law-qa-val.jsonl")
TEST_DS = os.path.join(DATA_DIR, "law-qa-test.jsonl")
