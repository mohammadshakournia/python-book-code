# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH11 / code21.py  |  تاریخ و زمان
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

from datetime import datetime, timedelta

dt = datetime(2026, 1, 24, 0, 0, 0)
future = dt + timedelta(days=10)
past = dt - timedelta(hours=36)

print(future)
print(past)
