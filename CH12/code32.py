# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH12 / code32.py  |  توابع آماری
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import numpy as np

a = np.array([[1.5, 2.5],
              [3.5, 4.5]])

np.savetxt("data.txt", a)

b = np.loadtxt("data.txt")
print(b)
