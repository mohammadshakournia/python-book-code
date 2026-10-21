# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : APPENDIX_B / code03.py  |  الگوهای طراحی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

def percent_discount(price):
    return price * 0.9

def fixed_discount(price):
    return price - 5

def checkout(price, strategy):
    return strategy(price)

print(checkout(100, percent_discount))
print(checkout(100, fixed_discount))
