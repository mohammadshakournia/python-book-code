# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code28.py  |  خواندن داده و نوشتن داده از/در فایل
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

report = pd.DataFrame({
    "city": ["Tehran", "Tabriz"],
    "mean_price": [135000, 85000]
})

report.to_excel("report.xlsx", index=False, sheet_name="Summary")
print("Saved report.xlsx")
