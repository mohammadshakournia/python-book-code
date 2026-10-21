# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH03 / code21.py  |  کاربردهای واقعی شرط‌ها و حلقه‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == "admin123":
        print("Access granted")
        break
    attempts += 1
