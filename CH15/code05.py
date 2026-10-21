# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH15 / code05.py  |  ابزارها و کتابخانه‌های مکمل در یادگیری ماشین
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Location": ["New York", "Paris", "Berlin", "London"],
    "Age": [24, 13, 53, 33],
}

data_pandas = pd.DataFrame(data)
print(data_pandas)

print("\nAge > 30:")
print(data_pandas[data_pandas.Age > 30])
