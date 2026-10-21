# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH12 / code28.py  |  توابع آماری
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import numpy as np

x = np.array([10, 20, 30, 40, 100])

print("mean:", x.mean())
print("median:", np.median(x))
print("std:", x.std())
print("argmax:", x.argmax())
print("max:", x.max())
