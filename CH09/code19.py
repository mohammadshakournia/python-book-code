# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH09 / code19.py  |  ژنراتور
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

from functools import wraps

def count_items(gen_func):
    @wraps(gen_func)
    def wrapper(*args, **kwargs):
        count = 0
        for item in gen_func(*args, **kwargs):
            count += 1
            yield item
        print(f"Total items: {count}")
    return wrapper

@count_items
def make_numbers(n):
    for i in range(n):
        yield i

for x in make_numbers(4):
    print("item:", x)
