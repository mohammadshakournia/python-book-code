# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH14 / code12.py  |  نمودارهای پرکاربرد
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
t = np.linspace(0, 4*np.pi, 200)
x = np.cos(t)
y = np.sin(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot3D(x, y, z, color="black", linewidth=2)

plt.show()
