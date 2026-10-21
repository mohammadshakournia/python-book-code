# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH09 / code10.py  |  دکوراتور
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

# file: 09_builtin_decorators.py
class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 1

    @classmethod
    def from_string(cls, s):
        first, last = s.split(",")
        return cls(first.strip(), last.strip())

u = User.from_string("Sara, Smith")
print(u.full_name)
print(User.is_valid_name("A"))
print(User.is_valid_name("Sara"))
