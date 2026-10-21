# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH10 / code05.py  |  مدیریت نخ‌ها با Thread Pool
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

from concurrent.futures import ThreadPoolExecutor
import time

def job(x):
    time.sleep(0.2)
    return x * x

with ThreadPoolExecutor(max_workers=4) as ex:
    futures = [ex.submit(job, i) for i in range(6)]
    results = [f.result() for f in futures]

print(results)
