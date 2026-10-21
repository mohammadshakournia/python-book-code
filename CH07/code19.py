# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code19.py  |  متدها، سازنده و ویژگی‌ها
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("Laptop", 35000)
print(p1.name)
print(p1.price)
