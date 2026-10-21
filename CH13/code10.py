# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code10.py  |  پاک‌سازی داده
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Ali", "Sara", "Reza", "Mina"],
    "age": [23, None, 31, None],
    "score": [18.5, 19.0, None, 17.0]
})

age_mean = df["age"].mean()
df["age"] = df["age"].fillna(age_mean)
df["score"] = df["score"].fillna(0)

print(age_mean)
print(df)
