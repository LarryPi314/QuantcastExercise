# test_cookie_cases.py

from most_active_cookie_optimized import *

# Provided test case with one most active cookie
def test_one_cookie():
    with open('logs/test_cookie_cases.csv', 'w+') as f:
        f.write('''cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00''')
    assert most_active_cookies_from_file('logs/test_cookie_cases.csv', "2018-12-09") == ['AtY0laUfhglK3lC7']

# test case where multiple cookies are tied on the given date
def test_tie():
    with open('logs/test_cookie_cases.csv', 'w+') as f:
        f.write('''cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T22:03:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
5UAVanZf6UtGyKVS,2018-12-07T23:30:00+00:00''')
    assert most_active_cookies_from_file('logs/test_cookie_cases.csv', "2018-12-09") == ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA']

# test case where all cookies are unique (all tied) on a larger dataset
def test_unique():
    with open('logs/test_cookie_cases.csv', 'w+') as f:
        f.write('''cookie,timestamp
9ah7N1X6Yt43PV2L,2023-02-17T01:22:00+00:00
oR5z8F2sU1jx0K9h,2023-02-17T01:53:00+00:00
yT4G3X8vJhU2f1Oq,2023-02-17T02:22:00+00:00
aQ8L2s5V7K4U9I0t,2023-02-17T02:41:00+00:00
vB3N6c8n5A0Z7f4Y,2023-02-17T03:16:00+00:00
4S6yA3vZ2u0P1G9r,2023-02-17T03:45:00+00:00
wL9M2a5P1c8U7I0t,2023-02-17T04:18:00+00:00
kD3V6z1j2N8o0R9h,2023-02-17T04:59:00+00:00
7rH3o2P8G5U1Z4sA,2023-02-17T05:20:00+00:00''')
    assert most_active_cookies_from_file('logs/test_cookie_cases.csv', "2023-02-17") == [
        '9ah7N1X6Yt43PV2L',
        'oR5z8F2sU1jx0K9h',
        'yT4G3X8vJhU2f1Oq',
        'aQ8L2s5V7K4U9I0t',
        'vB3N6c8n5A0Z7f4Y',
        '4S6yA3vZ2u0P1G9r',
        'wL9M2a5P1c8U7I0t',
        'kD3V6z1j2N8o0R9h',
        '7rH3o2P8G5U1Z4sA'
    ]

# test case where no cookies occur on the given date
def test_no_cookie():
    with open('logs/test_cookie_cases.csv', 'w+') as f:
        f.write('''cookie,timestamp
9ah7N1X6Yt43PV2L,2023-02-17T01:22:00+00:00
oR5z8F2sU1jx0K9h,2023-02-17T01:53:00+00:00
yT4G3X8vJhU2f1Oq,2023-02-17T02:22:00+00:00
aQ8L2s5V7K4U9I0t,2023-02-17T02:41:00+00:00
vB3N6c8n5A0Z7f4Y,2023-02-17T03:16:00+00:00
4S6yA3vZ2u0P1G9r,2023-02-17T03:45:00+00:00
wL9M2a5P1c8U7I0t,2023-02-17T04:18:00+00:00
kD3V6z1j2N8o0R9h,2023-02-17T04:59:00+00:00
7rH3o2P8G5U1Z4sA,2023-02-17T05:20:00+00:00''')
    assert most_active_cookies_from_file('logs/test_cookie_cases.csv', "2023-02-18") == []

# test an empty csv file
def test_empty_file():
    with open('logs/test_cookie_cases.csv', 'w+') as f:
        f.write('''cookie,timestamp''')
    assert most_active_cookies_from_file('logs/test_cookie_cases.csv', "2023-11-23") == []

# test a csv file consisting only of entries of the same cookie
def test_unanimous():
    with open('logs/test_cookie_cases.csv', 'w+') as f:
        f.write('''cookie,timestamp
9ah7N1X6Yt43PV2L,2023-02-17T01:21:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T01:45:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T02:11:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T02:38:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T03:05:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T03:31:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T04:14:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T04:44:00+00:00
9ah7N1X6Yt43PV2L,2023-02-17T05:17:00+00:00''')
    assert most_active_cookies_from_file('logs/test_cookie_cases.csv', "2023-02-17") == ['9ah7N1X6Yt43PV2L']

# test multiple cookies being tied on a larger dataset.
def test_big():
    with open('logs/test_cookie_cases.csv', 'w+') as f:
        f.write('''cookie,timestamp
1qR7F9oC1V0M8tI5,2023-02-17T01:22:00+00:00
8jN9Y6tJ3x1K9hR5,2023-02-17T01:53:00+00:00
2Z2V7J4hU7I4O9qT,2023-02-17T02:22:00+00:00
6u0P9G4rA3vZ2u0P,2023-02-17T02:41:00+00:00
5V7K4U1Z4sA3vZ2u,2023-02-17T03:16:00+00:00
2u0P1G9r4S6yA3vZ,2023-02-17T03:45:00+00:00
1c8U7I0tW9M2a5P1,2023-02-17T04:18:00+00:00
2N8o0R9hK3V6z1j2,2023-02-17T04:59:00+00:00
5G1Z4sA7rH3o2P8G,2023-02-17T05:20:00+00:00
1s9qA75kD3V6z1j2,2023-02-17T05:54:00+00:00
4S6yA3vZ2u0P1G9r,2023-02-17T06:12:00+00:00
8G5U1Z4sA3vZ2u0P,2023-02-17T06:51:00+00:00
1c8U7I0tW9M2a5P1,2023-02-17T07:03:00+00:00
2N8o0R9hK3V6z1j2,2023-02-17T07:53:00+00:00
5G1Z4sA7rH3o2P8G,2023-02-17T08:09:00+00:00
1s9qA75kD3V6z1j2,2023-02-17T08:37:00+00:00
4S6yA3vZ2u0P1G9r,2023-02-17T09:23:00+00:00
8G5U1Z4sA3vZ2u0P,2023-02-17T09:55:00+00:00
1c8U7I0tW9M2a5P1,2023-02-17T10:21:00+00:00
2N8o0R9hK3V6z1j2,2023-02-17T10:57:00+00:00''')
    assert most_active_cookies_from_file('logs/test_cookie_cases.csv', "2023-02-17") == [
        '1c8U7I0tW9M2a5P1',
        '2N8o0R9hK3V6z1j2'
    ]
