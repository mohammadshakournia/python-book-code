# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code21.py  |  ذخیره و خروجی گرفتن
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y, linewidth=2, color="black")
plt.grid(True)

plt.savefig("plot.png", dpi=300, bbox_inches="tight")
plt.savefig("plot.jpg", dpi=300, bbox_inches="tight")
plt.savefig("plot.svg", bbox_inches="tight")

plt.show()
