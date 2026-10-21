# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH09 / code18.py  |  ژنراتور
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

def echo():
    value = yield "ready"
    while True:
        value = yield f"got: {value}"

g = echo()
print(next(g))
print(g.send("A"))
print(g.send("B"))
g.close()
