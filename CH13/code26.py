# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code26.py  |  خواندن داده و نوشتن داده از/در فایل
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

df = pd.DataFrame({
    "name": ["Ali", "Sara", "Reza"],
    "price": [120000.0, None, 99000.5]
})

df.to_csv("sales_clean.csv", index=False, na_rep="NA", float_format="%.2f", encoding="utf-8-sig")
print("Saved sales_clean.csv")
