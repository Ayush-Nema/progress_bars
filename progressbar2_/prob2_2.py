"""
`$ python3 prob2_2.py`
"""

from time import sleep

from progress.bar import Bar
from progressbar import progressbar

# The issue with combining print statement with progress bars
with Bar('Processing', max=5) as bar:
    for i in range(5):
        sleep(0.1)
        print('\n', i)
        bar.next()

# The solution to above issue
for i in progressbar(range(100), redirect_stdout=True):
    print('Some text', i)
    sleep(0.1)
