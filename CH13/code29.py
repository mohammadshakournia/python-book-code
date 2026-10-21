# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code29.py  |  خواندن داده و نوشتن داده از/در فایل
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004],
    "price": [120000, 85000, 99000, 150000],
    "city": ["Tehran", "Tabriz", "Tehran", "Shiraz"]
})

summary = orders.groupby("city")["price"].agg(["count", "mean", "max"]).reset_index()

with pd.ExcelWriter("sales_report.xlsx") as writer:
    orders.to_excel(writer, index=False, sheet_name="Orders")
    summary.to_excel(writer, index=False, sheet_name="Summary")

print("Saved sales_report.xlsx")
