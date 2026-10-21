# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code17.py  |  متدها، سازنده و ویژگی‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class User:
    def __init__(self, username, is_active):
        self.username = username
        self.is_active = is_active

    def is_user_active(self):
        return self.is_active

user1 = User("ali", True)

if user1.is_user_active():
    print("User is active")
else:
    print("User is not active")
