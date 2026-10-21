# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH06 / code07.py  |  ذخیره‌سازی داده با pickle
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pickle

scores = [18, 15, 20, 17]

file = open("scores.pkl", "wb")
pickle.dump(scores, file)
file.close()

print("Data saved.")
