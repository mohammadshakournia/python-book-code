# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH16 / code29.py  |  الگوریتم‌های یادگیری ماشین نظارت شده
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import mglearn

X, y = mglearn.datasets.make_forge()

fig, ax = plt.subplots(1, 1, figsize=(5, 3))
clf = LogisticRegression().fit(X, y)

mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=0.7)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)

ax.set_title("LogisticRegression")
ax.set_xlabel("Feature 0")
ax.set_ylabel("Feature 1")
ax.legend()
plt.show()
