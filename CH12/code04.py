# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH12 / code04.py  |  آرایه‌ها و ساختار ndarray
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import numpy as np

a = np.array([1, 2, 3], dtype=np.float64)
b = np.array([1.2, 2.7, 3.9])

print(a.dtype)
print(b.astype(int))
print(b.astype(int).dtype)
