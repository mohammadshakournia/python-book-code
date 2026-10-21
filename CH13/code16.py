# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code16.py  |  گروه‌بندی، فیلتر، Merge
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004],
    "price": [120000, 85000, 99000, 150000],
    "city": ["Tehran", "Tabriz", "Tehran", "Shiraz"]
})

filtered = df[df["city"] == "Tehran"]
print(filtered)
