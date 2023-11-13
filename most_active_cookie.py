#!/usr/bin/python3
# Larry Wang
# 11/11/23

import sys
from typing import List


def find_most_active_cookies(lines: List[str], targetDate: str) -> List[str]:
    """
    Takes a list of cookies and timestamps and returns
    a list of cookies that occur most frequently on
    a given timestamp

    Complexity: O(n) time and O(n) space
    Parameters
    ----------
    lines : List[str]
        List of cookies containing unseparated 
        cookie,timestamp pairs
    date : str
        The date the most active cookies fall on
        (formatted YYYY-MM-DD)

    Returns
    -------
    List[str]
        The cookie that was most active on the input date, 
        or the most active cookies in the case of a tie.
    """
    # count how frequently each cookie appears on targetDate
    occurrences = {}  # maps cookies to their number of occurrences on targetDate
    for line in lines:
        cookie, time = line.split(',')
        if time[:10] == targetDate:  # only count cookies that occurred on targetDate
            if cookie in occurrences:
                occurrences[cookie] += 1
            else:
                occurrences[cookie] = 1
    if not occurrences: # no cookies occurred on targetDate
        return []
        
    # print cookie with most occurences, including those tied for most occurences
    mostFreq = max(occurrences.values())
    return [cookie for cookie, counts in occurrences.items() if counts == mostFreq]


def read_file(path: str) -> List[str]:
    """
    Takes a path to the input file and reads the 
    lines of the file in the path to a list

    Parameters
    ----------
    filepath : str
        The path to the input file to be read. 

    Returns
    -------
    List[str]
        The lines consisting of unseparated cookie, timestamp pairs
    """

    try:
        with open(path, 'r') as f:
            lines = f.read().split('\n')
            assert lines[0] == "cookie,timestamp"  # ensure CSV is formatted correctly
            return lines[1:]
    except AssertionError:
        print("Error: input file is not in the correct format: header must read cookie,timestamp")
    except FileNotFoundError:
        print(f"Error: file at {filepath} not found")
    

def most_active_cookies_from_file(filepath: str, targetDate: str) -> List[str]:
    """
    Returns a list of cookies that were most active
    on a given date in a well-formatted log file. 
    
    Parameters
    ----------
    filepath : str
        The filepath to the well-formatted csv file
        containing cookie, timestamp pairs. 
    targetDate : str
        The date the most active cookies should fall on
        (formatted YYYY-MM-DD)

    Returns
    -------
    List[]
        The cookie that was most active on the input date, 
        or the several most active cookies in the case of a tie.
    """

    lines = read_file(filepath)
    mostActiveCookies = find_most_active_cookies(lines, targetDate)
    return mostActiveCookies


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 4  # ensure correct number of arguments
        filepath = sys.argv[1]
        targetDate = sys.argv[3]
    except AssertionError:
        print("Error: invalid command, to use run ./most_active_cookie <filepath> -d <date>")

    for most_active_cookie in most_active_cookies_from_file(filepath, targetDate):
        print(most_active_cookie)
