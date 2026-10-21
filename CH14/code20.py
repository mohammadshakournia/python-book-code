# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code20.py  |  تنظیمات کاربردی و رسم چند نمودار
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]

fig, axes = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

axes[0].plot(x, y1, color="black", linewidth=2, marker="o")
axes[1].plot(x, y2, color="black", linewidth=2, linestyle="--", marker="s")

fig.tight_layout()
plt.show()
