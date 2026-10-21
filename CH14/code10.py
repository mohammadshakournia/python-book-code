# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code10.py  |  نمودارهای پرکاربرد
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

data = [10, 11, 12, 12, 13, 15, 16, 16, 16, 18, 19, 20, 20, 21, 22, 25]

plt.hist(data, bins=5, edgecolor="black", linewidth=1.2)
plt.show()
