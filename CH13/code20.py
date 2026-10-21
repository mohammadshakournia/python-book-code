# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH13 / code20.py  |  گروه‌بندی، فیلتر، Merge
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import pandas as pd

a = pd.DataFrame({
    "id": [1, 2, 3],
    "val_a": ["A1", "A2", "A3"]
})

b = pd.DataFrame({
    "id": [2, 3, 4],
    "val_b": ["B2", "B3", "B4"]
})

inner_join = a.merge(b, on="id", how="inner")
outer_join = a.merge(b, on="id", how="outer").sort_values("id")
left_join = a.merge(b, on="id", how="left").sort_values("id")
right_join = a.merge(b, on="id", how="right").sort_values("id")

print("INNER JOIN")
print(inner_join)
print("\nLEFT JOIN")
print(left_join)
print("\nRIGHT JOIN")
print(right_join)
print("\nOUTER JOIN")
print(outer_join)
