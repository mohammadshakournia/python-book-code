# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : CH07 / code24.py  |  اصول برنامه نویسی شی گرا
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self._balance += amount
        return "Deposit successful"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > self._balance:
            return "Not enough balance"
        self._balance -= amount
        return "Withdraw successful"


account = BankAccount(1000)

print(account.get_balance())
print(account.withdraw(1500))
print(account.deposit(500))
print(account.get_balance())
