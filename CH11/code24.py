# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH11 / code24.py  |  تاریخ و زمان
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import jdatetime

jdt = jdatetime.date(1404, 11, 4)
print(jdt.strftime("%Y/%m/%d"))
print(jdt.strftime("%Y-%m-%d"))
