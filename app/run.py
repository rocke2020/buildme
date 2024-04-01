import argparse
import json
import logging
import math
import os
import random
import re
import shutil
import sys
import time
import warnings
from collections import defaultdict
from datetime import datetime
from pathlib import Path

warnings.simplefilter(action="ignore", category=FutureWarning)
sys.path.append(os.path.abspath("."))


logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    datefmt="%y-%m-%d %H:%M",
    format="%(asctime)s %(filename)s %(lineno)d: %(message)s",
)


parser = argparse.ArgumentParser()
parser.add_argument("--args_file", default="app/args/demo_binder.yml")
raw_args = parser.parse_args()


SEED = 0
random.seed(SEED)
logger.info(f"{datetime.now() = }")
with open("output/1.txt", "w", encoding="utf-8") as f:
    f.write(f"{datetime.now()}\n")
    f.write(f"{raw_args.args_file}\n")

logger.info('end')
