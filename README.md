# Quantcast Exercise

Quantcast Coding Task Exercise Submission

This submission is fully equipped with Github automated validation using pytest through GitHub Actions.

To execute the program, run the following command: `$ ./most_active_cookie <filepath> -d <date>` (ensuring proper execute permissions).

Repository File Structure:

- `most_active_cookie` Compiled program (derived from most_active_cookie.py) for effortless command-line interface (CLI) usage.
- `most_active_cookie.py` Uncompiled Python script presenting my solution to the Most Active Cookie problem.
- `most_active_cookie_optimized.py` Uncompiled Python script containing my optimized solution to the Most Active Cookie problem (using binary search). This script was tested successfully on my unit tests.
- `test_cookie_cases.py` Pytest file containing unit tests for GitHub Actions automation.

`most_active_cookie` was compiled using `pyinstaller --noconfirm --onefile --console "most_active_cookie.py"`


