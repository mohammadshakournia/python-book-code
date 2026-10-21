# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH09 / code16.py  |  ژنراتور
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

def only_long(words, min_len):
    for w in words:
        if len(w) >= min_len:
            yield w

def to_upper(words):
    for w in words:
        yield w.upper()

data = ["cat", "tiger", "ant", "elephant", "dog"]
pipeline = to_upper(only_long(data, 5))

for item in pipeline:
    print(item)
