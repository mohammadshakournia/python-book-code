# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code18.py  |  گروه‌بندی، فیلتر، Merge
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "city": ["Tehran", "Tabriz", "Shiraz", "Tehran", "Shiraz"],
    "price": [120000, 85000, 99000, 150000, 70000]
})

stats = df.groupby("city")["price"].agg(["count", "mean", "max"])
print(stats)
