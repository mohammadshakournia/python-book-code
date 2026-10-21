# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH08 / code13.py  |  چهار سناریوی کاربردی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

while True:
    try:
        x = int(input("Enter a positive integer: "))
        if x <= 0:
            raise ValueError("Number must be positive.")
    except ValueError as e:
        print("Invalid input:", e)
    else:
        print("Accepted:", x)
        break
