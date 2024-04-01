import json
import math
import os
import random
import re
import shutil
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import datetime
import logging

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    datefmt="%y-%m-%d %H:%M",
    format="%(asctime)s %(filename)s %(lineno)d: %(message)s",
)


SEED = 0
random.seed(SEED)
logger.info(f'{datetime.datetime.now() = }')
with open("output/1.txt", "w", encoding="utf-8") as f:
    f.write(f"{datetime.datetime.now()}\n")

logger.info(f"{SEED = }")
