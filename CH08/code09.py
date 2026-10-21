# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH08 / code09.py  |  چارچوب try/except برای مدیریت کنترل‌شده استثناءها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
