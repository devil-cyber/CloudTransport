from __future__ import division
import sys
import os




try:
    from tqdm import tqdm
except ImportError:
    class TqdmWrap(object):
        # tqdm not installed - construct and return dummy/basic versions
        def __init__(self, *a, **k):
            pass

        def viewBar(self, a, b):
            # original version
            res = a / int(b) * 100
            sys.stdout.write('\rComplete precent: %.2f %%' % (res))
            sys.stdout.flush()

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False
else:
    class TqdmWrap(tqdm):
        def viewBar(self, a, b):
            self.total = int(b)
            self.update(int(a - self.n))  # update pbar with increment