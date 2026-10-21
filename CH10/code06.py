# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH10 / code06.py  |  موازی سازی با multiprocessing
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

from concurrent.futures import ProcessPoolExecutor

def job(x):
    return x * x

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(job, range(6)))
    print(results)
