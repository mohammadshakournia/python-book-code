# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH09 / code08.py  |  دکوراتور
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

from functools import wraps

def deco_a(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("A: before")
        result = func(*args, **kwargs)
        print("A: after")
        return result
    return wrapper

def deco_b(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("B: before")
        result = func(*args, **kwargs)
        print("B: after")
        return result
    return wrapper

@deco_a
@deco_b
def work():
    print("Work")

work()
