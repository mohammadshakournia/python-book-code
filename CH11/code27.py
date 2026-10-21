# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH11 / code27.py  |  تاریخ و زمان
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import jdatetime

s = "1404-11-04"
y, m, d = map(int, s.split("-"))
jdt = jdatetime.date(y, m, d)

print("Jalali:", jdt)
print("Gregorian:", jdt.togregorian())
