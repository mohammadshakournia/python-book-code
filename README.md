# Python Programming Guide: Book Code

Repository: <https://github.com/mohammadshakournia/python-book-code>

[English](README.md) | [فارسی](README.fa.md)

Source code for the Persian book **«راهنمای جامع برنامه‌نویسی پایتون»** (*A Comprehensive Guide to Python Programming*, from fundamentals to machine learning) by **Mohammad Reza Shakournia**.

This repository contains every Python example printed in the book: **389 examples in the 18 chapters and 4 in Appendix B**, organised by chapter, numbered in the order they appear in the book, and stored together with the output shown in the book.

The book itself is written in Persian. Code, identifiers and output are in English, so the code is usable without reading Persian. The README files inside the chapter folders list the book section for each example (in Persian).

## Repository layout

Each chapter has its own folder named `CHxx` (for example `CH12` is Chapter 12). Examples are numbered in book order:

```
CH12/
  code01.py            first code example of Chapter 12
  code01_output.txt    the output shown in the book for this example
  code02.py
  ...
  snippets/            non-Python commands (e.g. pip install) and deliberately incomplete fragments
  README.md            index of the chapter's examples and their book sections
```

The command line shown above each output in the book matches this layout exactly:

```
C:\Users\python-book\ch12> python code01.py
```

| Folder | Topic | Examples |
|---|---|---|
| [`CH01`](CH01/) | Introduction and installing Python | 7 |
| [`CH02`](CH02/) | Variables, data types and operators | 29 |
| [`CH03`](CH03/) | Control flow | 21 |
| [`CH04`](CH04/) | Working with data (lists, tuples, dictionaries) | 32 |
| [`CH05`](CH05/) | Functions and modules | 24 |
| [`CH06`](CH06/) | Files and data persistence | 10 |
| [`CH07`](CH07/) | Object-oriented programming | 25 |
| [`CH08`](CH08/) | Error handling | 16 |
| [`CH09`](CH09/) | Decorators and generators | 19 |
| [`CH10`](CH10/) | Multithreading, parallelism and concurrency | 7 |
| [`CH11`](CH11/) | Data processing and analysis in Python | 34 |
| [`CH12`](CH12/) | NumPy | 32 |
| [`CH13`](CH13/) | Pandas | 29 |
| [`CH14`](CH14/) | Data visualization with Matplotlib | 23 |
| [`CH15`](CH15/) | Introduction to machine learning | 22 |
| [`CH16`](CH16/) | Supervised learning | 49 |
| [`CH17`](CH17/) | Unsupervised learning | 7 |
| [`CH18`](CH18/) | Advanced topics: deep learning | 3 |
| [`APPENDIX_A`](APPENDIX_A/) | Appendix A: Git, Docker and CI/CD (config files and commands) | n/a |
| [`APPENDIX_B`](APPENDIX_B/) | Appendix B: code optimization and design patterns | 4 |

## Getting started

The examples were run with Python 3.13; a recent Python 3 release should work.

```bash
git clone https://github.com/mohammadshakournia/python-book-code.git
cd python-book-code

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python CH03/code01.py
```

- The deep learning examples in `CH18` need `tensorflow` and `torch` (`requirements-deeplearning.txt`).
- Run each script from the repository root, or `cd` into its folder if it reads or writes files next to itself.

## Notes

- **Examples are not always standalone.** As in the book, some examples build on earlier ones in the same section, read input files, or call `input()`. A few are intentionally broken to demonstrate an error, and fragments that cannot run on their own are kept in `snippets/`.
- **Line numbers in tracebacks.** Every file starts with a 10-line header (author, email and copyright comments plus a blank line), so line numbers in a real traceback are 10 higher than the ones printed in the book.
- **Output may differ slightly** from the book for examples that use random numbers, time, or model accuracy, and with newer library versions.
- **Library versions.** Some examples use functions that newer scikit-learn releases have removed or changed, so you may see errors or warnings with the latest versions.

## Author

**Mohammad Reza Shakournia**
Email: mohammadshakournia@gmail.com

## License and rights

Copyright (c) 2026 Mohammad Reza Shakournia. All rights reserved.

All material and moral rights to the book and to the code in this repository belong to the author. Any commercial use or redistribution without the author's written permission is prohibited. See [LICENSE](LICENSE).
