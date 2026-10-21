# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code19.py  |  تنظیمات کاربردی و رسم چند نمودار
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [3, 4, 2, 5, 7, 6, 8, 7]

cats = ["A", "B", "C", "D"]
vals = [12, 7, 15, 5]

fig, axes = plt.subplots(2, 2, figsize=(8, 6))

axes[0, 0].plot(x, y, color="black", linewidth=2)
axes[0, 1].scatter(xs, ys, s=50, facecolors="white", edgecolors="black", linewidths=1.2)

bars = axes[1, 0].bar(cats, vals, color="white", edgecolor="black", linewidth=1.0)
for b, h in zip(bars, ["///", "\\\\", "xx", ".."]):
    b.set_hatch(h)

axes[1, 1].hist(np.random.normal(0, 1, 200), bins=12, color="white", edgecolor="black", linewidth=1.0)

fig.tight_layout()
plt.show()
