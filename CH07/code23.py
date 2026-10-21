# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code23.py  |  اصول برنامه نویسی شی گرا
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class Animal:
    def speak(self):
        return "Animal makes a sound"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


class Cat(Animal):
    def speak(self):
        return "Cat meows"


animals = [Dog(), Cat(), Animal()]

for a in animals:
    print(a.speak())
