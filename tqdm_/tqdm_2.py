"""
`$ python3 tqdm_2.py`
"""

import pandas as pd
import numpy as np
from tqdm import tqdm

df = pd.DataFrame(np.random.randint(0, 100, (100000, 600)))

tqdm.pandas(desc="my bar!")

df.progress_apply(lambda x: x ** 2)
