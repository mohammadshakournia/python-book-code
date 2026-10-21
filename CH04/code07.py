# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH04 / code07.py  |  لیست و عملیات مهم روی آن
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

base = [3, 1, 4, 1, 5]
print("base =", base)
# ---- توابع عمومی ----
print("len(base) ->", len(base))
print("sorted(base) ->", sorted(base))
print("min(base) ->", min(base))
print("max(base) ->", max(base))
print("sum(base) ->", sum(base))
# ---- متدهای بدون تغییر محتوای پایه ----
print("base.count(1) ->", base.count(1))
print("base.index(4) ->", base.index(4))
# ---- متدهای تغییردهنده (روی کپی) ----
a = base.copy()
a.append(9)
print("append on copy ->", a)
b = base.copy()
b.extend([9, 2])
print("extend on copy ->", b)

c = base.copy()
c.insert(2, 99)
print("insert on copy ->", c)

d = base.copy()
d.remove(1)
print("remove on copy ->", d)

e = base.copy()
removed = e.pop(3)
print("pop on copy -> removed =", removed, "| list =", e)

f = base.copy()
f.sort()
print("sort on copy ->", f)

g = base.copy()
g.reverse()
print("reverse on copy ->", g)

h = base.copy()
h.clear()
print("clear on copy ->", h)

# ---- تابع list برای تبدیل ----
text = "Python"
print("list(text) ->", list(text))
