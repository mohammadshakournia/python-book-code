# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH04 / code20.py  |  دیکشنری و ساختار کلید–مقدار
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

product = {"name": "Laptop", "price": 1200, "stock": 5}

print("product =", product)

print("len(product) ->", len(product))
print("keys() ->", product.keys())
print("values() ->", product.values())
print("items() ->", product.items())

print("get('price') ->", product.get("price"))

product["stock"] = 4
product.update({"brand": "Dell"})

removed = product.pop("price")

print("after changes ->", product)
print("removed price ->", removed)
