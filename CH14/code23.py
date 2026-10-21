# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code23.py  |  ذخیره و خروجی گرفتن
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1, 2], [0, 1, 4], color="black")
plt.savefig("fig1.png", dpi=300, bbox_inches="tight")

plt.figure()
plt.plot([0, 1, 2], [0, 1, 2], linestyle="--", color="black")
plt.savefig("fig2.png", dpi=300, bbox_inches="tight")

plt.show()
