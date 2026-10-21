# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH12 / code29.py  |  توابع آماری
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("sum axis=0:", data.sum(axis=0))
print("sum axis=1:", data.sum(axis=1))
