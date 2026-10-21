# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code07.py  |  Series و DataFrame
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Ali", "Sara", "Reza", "Mina"],
    "age": [23, 19, 31, 27],
    "city": ["Tehran", "Tabriz", "Shiraz", "Tehran"]
})

print(df.loc[2, "name"])
print(df.iloc[0, 1])
