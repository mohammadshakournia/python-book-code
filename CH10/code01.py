# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH10 / code01.py  |  مفهوم نخ یا Thread
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import threading
import time

def worker(name, delay):
    for i in range(3):
        print(f"[{name}] step={i}")
        time.sleep(delay)

t1 = threading.Thread(target=worker, args=("A", 0.2))
t2 = threading.Thread(target=worker, args=("B", 0.2))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished.")
