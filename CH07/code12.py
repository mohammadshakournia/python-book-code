# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code12.py  |  متدها، سازنده و ویژگی‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class User:
    def __init__(self, username):
        self.username = username

    def greet(self):
        print("Welcome", self.username)

u1 = User("admin")
print(u1.username)
u1.greet()
