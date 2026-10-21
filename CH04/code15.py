# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH04 / code15.py  |  تاپل و کاربردهای آن
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

base = (3, 1, 4, 1, 5)

print("base =", base)

print("len(base) ->", len(base))
print("sorted(base) ->", sorted(base))
print("min(base) ->", min(base))
print("max(base) ->", max(base))
print("sum(base) ->", sum(base))

print("base.count(1) ->", base.count(1))
print("base.index(4) ->", base.index(4))

text = "Python"
print("tuple(text) ->", tuple(text))

lst = list(base)
lst.append(9)
print("list(base) after append ->", lst)
