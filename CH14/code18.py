# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code18.py  |  تنظیمات کاربردی و رسم چند نمودار
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y, linewidth=2, color="black")

ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
plt.show()
