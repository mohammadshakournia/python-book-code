# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code11.py  |  پاک‌سازی داده
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Ali", "Sara", "Sara", "Mina"],
    "city": ["Tehran", "Tabriz", "Tabriz", "Tehran"]
})

print(df.duplicated())
print(df.drop_duplicates())
