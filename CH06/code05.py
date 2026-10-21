# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH06 / code05.py  |  استفاده از دستور with
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

with open("with_notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python\n")
    file.write("This file is written using with\n")
    file.write("End\n")

print("Writing finished.")
