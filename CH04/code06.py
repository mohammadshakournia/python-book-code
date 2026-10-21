# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH04 / code06.py  |  لیست و عملیات مهم روی آن
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

items = ["pen", "book", "phone", "tablet", "phone"]

items.remove("phone")
removed_item = items.pop(1)
del items[1:3]

print(items)
print(removed_item)
