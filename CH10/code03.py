# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH10 / code03.py  |  وضعیت مشترک و Race Condition
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import threading

counter = 0
lock = threading.Lock()

def inc_many(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

threads = []
for _ in range(5):
    t = threading.Thread(target=inc_many, args=(100000,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter)
