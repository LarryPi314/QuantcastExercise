# Quantcast Exercise

## Quantcast Coding Task Exercise Submission

This submission is fully equipped with Github automated validation using pytest through GitHub Actions.

To execute the program, run the following command: `$ ./most_active_cookie <filepath> -d <date>` (ensuring proper execute permissions).

## Repository File Structure:

- `most_active_cookie` Compiled program (derived from most_active_cookie.py) for effortless command-line interface (CLI) usage.
- `most_active_cookie.py` Uncompiled Python script presenting my solution to the Most Active Cookie problem.
- `most_active_cookie_optimized.py` Uncompiled Python script containing my optimized solution to the Most Active Cookie problem (using binary search). This script was tested successfully on my unit tests.
- `test_cookie_cases.py` Pytest file containing unit tests for GitHub Actions automation.

`most_active_cookie` was compiled using `pyinstaller --noconfirm --onefile --console "most_active_cookie.py"`

## Problem specifications

Given a cookie log format in the following format:

cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00

Process the log file and return the most active cookie on a specified day. If multiple cookies fit that criteria, return all of them on separate lines. We may assume that cookies are sorted by timestamp. 


