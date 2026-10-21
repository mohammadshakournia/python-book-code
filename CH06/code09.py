# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH06 / code09.py  |  ذخیره‌سازی داده با pickle
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pickle

user = {
    "username": "admin",
    "age": 30,
    "active": True
}

file = open("user.pkl", "wb")
pickle.dump(user, file)
file.close()

print("User data saved.")
