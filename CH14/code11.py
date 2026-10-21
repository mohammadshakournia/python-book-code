# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code11.py  |  نمودارهای پرکاربرد
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
sizes = [40, 25, 20, 15]

wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct="%1.0f%%",
    wedgeprops={"edgecolor": "black", "linewidth": 1.0}
)

patterns = ["///", "\\\\", "xx", ".."]
for w, pat in zip(wedges, patterns):
    w.set_hatch(pat)

plt.show()
