# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH08 / code14.py  |  چهار سناریوی کاربردی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

f = None
try:
    f = open("notes.txt", "r", encoding="utf-8")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("OS error:", e)
finally:
    if f is not None:
        f.close()
        print("File closed.")
