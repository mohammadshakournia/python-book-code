# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH10 / code07.py  |  همروندی غیرهمزمان با asyncio
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import asyncio

async def job(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    results = await asyncio.gather(
        job("A", 0.2),
        job("B", 0.1),
        job("C", 0.3),
    )
    print(results)

asyncio.run(main())
