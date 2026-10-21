# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH18 / code01.py  |  تانسور و مشتق خودکار
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

import torch

x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(x.shape)
print(x * 2)

w = torch.tensor(3.0, requires_grad=True)
loss = (w * 2 - 10) ** 2
loss.backward()
print(w.grad)
