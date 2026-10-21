# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH05 / code06.py  |  تعریف تابع، آرگومان‌ها و خروجی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

def full_example(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

full_example(1, 2, 3, 4, name="Ali", age=25)
