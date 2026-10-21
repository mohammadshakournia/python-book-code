# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH11 / code34.py  |  مرتب‌سازی و فیلتر کردن داده‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

people = [
    {"name": "Ali", "age": 28},
    {"name": "Sara", "age": 22},
    {"name": "Reza", "age": 35},
    {"name": "Mina", "age": 26},
]

filtered = [p for p in people if p["age"] >= 25]
result = sorted(filtered, key=lambda p: p["age"])

print(result)
