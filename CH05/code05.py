# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH05 / code05.py  |  تعریف تابع، آرگومان‌ها و خروجی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

def show_information(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_information(name="Ali", age=25, city="Tehran")
