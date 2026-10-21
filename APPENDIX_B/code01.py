# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : APPENDIX_B / code01.py  |  اندازه‌گیری پیش از بهینه‌سازی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import timeit

numbers = list(range(10000))
numbers_set = set(numbers)

t_list = timeit.timeit(lambda: 9999 in numbers, number=1000)
t_set = timeit.timeit(lambda: 9999 in numbers_set, number=1000)
print("set is faster:", t_set < t_list)
