# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code08.py  |  نمودارهای پرکاربرد
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 4, 2, 5, 7, 6, 8, 7]

sizes = [20, 40, 30, 60, 80, 70, 90, 75]
values = [10, 20, 15, 30, 40, 35, 45, 38]

plt.scatter(x, y, s=sizes, alpha=0.55, c=values, cmap="gray")
plt.show()
