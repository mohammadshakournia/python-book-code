# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Author   : Mohammad Reza Shakournia
# Email    : mohammadshakournia@gmail.com
# Book     : راهنمای جامع برنامه‌نویسی پایتون (Python Programming Guide)
# Source   : APPENDIX_B / code04.py  |  الگوهای طراحی
# Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.
# حقوق مادی و معنوی این اثر برای نویسنده محفوظ است.
# ---------------------------------------------------------------------------

class JsonExporter:
    def export(self, data):
        return f"JSON: {data}"

class CsvExporter:
    def export(self, data):
        return f"CSV: {data}"

def exporter_factory(kind):
    exporters = {"json": JsonExporter, "csv": CsvExporter}
    return exporters[kind]()

exporter = exporter_factory("csv")
print(exporter.export([1, 2, 3]))
