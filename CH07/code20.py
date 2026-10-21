# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code20.py  |  متدها، سازنده و ویژگی‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class User:
    def __init__(self, username, role="member"):
        self.username = username
        self.role = role

u1 = User("ali")
u2 = User("sara", "admin")

print(u1.username, u1.role)
print(u2.username, u2.role)
