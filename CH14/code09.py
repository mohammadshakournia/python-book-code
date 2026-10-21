# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code09.py  |  نمودارهای پرکاربرد
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [12, 7, 15, 5]

bars = plt.bar(categories, values)

patterns = ["///", "\\\\", "xx", ".."]
for bar, pat in zip(bars, patterns):
    bar.set_hatch(pat)
    bar.set_edgecolor("black")
    bar.set_linewidth(1.2)

plt.show()
