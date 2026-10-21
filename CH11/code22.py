# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH11 / code22.py  |  تاریخ و زمان
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

from datetime import datetime

rows = [
    {"event": "A", "time": "2026-01-24 09:15"},
    {"event": "B", "time": "2026-01-24 08:10"},
    {"event": "C", "time": "2026-01-23 22:05"},
]

for r in rows:
    r["dt"] = datetime.strptime(r["time"], "%Y-%m-%d %H:%M")

rows_sorted = sorted(rows, key=lambda r: r["dt"])

for r in rows_sorted:
    print(r["event"], r["time"])
