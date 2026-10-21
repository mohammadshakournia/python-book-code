# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH11 / code28.py  |  مرتب‌سازی و فیلتر کردن داده‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

nums = [5, 1, 4, 2, 3]

a = sorted(nums)
print("sorted result:", a)
print("original:", nums)

nums.sort()
print("after sort:", nums)
