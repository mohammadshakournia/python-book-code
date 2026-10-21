# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH08 / code12.py  |  تعریف و کاربرد استثناءهای سفارشی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class PasswordTooShortError(Exception):
    pass


def set_password(password: str) -> None:
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters.")
    print("Password set successfully.")


try:
    set_password(input("Enter a password: "))
except PasswordTooShortError as e:
    print("Password error:", e)
