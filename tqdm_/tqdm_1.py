"""
`$ python3 tqdm_1.py`
"""

from tqdm import tqdm
from time import sleep

for i in tqdm(range(100)):
    sleep(0.02)
