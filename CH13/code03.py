# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code03.py  |  Series و DataFrame
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

data = {
    "name": ["Ali", "Sara", "Reza", "Mina"],
    "age": [23, 19, 31, 27],
    "city": ["Tehran", "Tabriz", "Shiraz", "Tehran"]
}

df = pd.DataFrame(data)
print(df)
