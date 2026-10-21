# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH08 / code16.py  |  چهار سناریوی کاربردی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class InvalidAgeError(Exception):
    pass


class PasswordTooShortError(Exception):
    pass


def validate_age(age: int) -> None:
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")


def validate_password(password: str) -> None:
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters.")


try:
    age_input = input("Enter your age: ")
    age = int(age_input)
    validate_age(age)

    password = input("Enter your password: ")
    validate_password(password)

except ValueError:
    print("Age must be an integer.")
except InvalidAgeError as e:
    print("Age error:", e)
except PasswordTooShortError as e:
    print("Password error:", e)
else:
    print("Registration successful.")
