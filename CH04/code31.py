# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH04 / code31.py  |  لیست‌های تو در تو و داده‌های پیچیده
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

students = [
    {"name": "Ali", "scores": [18, 17, 19]},
    {"name": "Sara", "scores": [20, 19, 18]},
    {"name": "Reza", "scores": [16, 15, 17]}
]

print(students[1]["name"])
print(students[1]["scores"][0])
