# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code22.py  |  اصول برنامه نویسی شی گرا
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return "My name is " + self.name


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_id(self):
        return "My student id is " + self.student_id


s1 = Student("Ali", "ST123")
print(s1.introduce())
print(s1.show_id())
