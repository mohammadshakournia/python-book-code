# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH05 / code24.py  |  نوشتن یک ماژول شخصی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
if __name__ == "__main__":
    print(add(2, 3))
    print(multiply(3, 4))
