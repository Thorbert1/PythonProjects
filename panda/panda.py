# Hello bois

import numpy as np
import pandas as pd
from matplotlib import pyplot

randn = np.random.randn

s = pd.Series([1, 3, 4, np.nan, 9])

print(s)

dates = pd.date_range("20210113", periods=6)

print(dates)
