# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH04 / code26.py  |  مجموعه‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

base = {1, 2, 3, 4}

print("base =", base)

print("len(base) ->", len(base))
print("2 in base ->", 2 in base)

base.add(5)
base.discard(1)

print("after add and discard ->", base)

other = {3, 4, 6}

print("union ->", base.union(other))
print("intersection ->", base.intersection(other))
print("difference ->", base.difference(other))
