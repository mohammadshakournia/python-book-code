# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code19.py  |  گروه‌بندی، فیلتر، Merge
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "user_id": [1, 2, 1],
    "price": [120000, 85000, 99000]
})

users = pd.DataFrame({
    "user_id": [1, 2],
    "name": ["Ali", "Sara"],
    "city": ["Tehran", "Tabriz"]
})

merged = orders.merge(users, on="user_id", how="left")
print(merged)
