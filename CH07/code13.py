# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code13.py  |  متدها، سازنده و ویژگی‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class User:
    role = "member"

    def __init__(self, username):
        self.username = username

u1 = User("Ali")
u2 = User("Sara")

print(u1.role)
print(u2.role)
