#!/usr/bin/python3
# Larry Wang
# 11/11/23

import sys
from typing import List

def get_right_cookie(cmpTimeStamps: List[int], cmpDate: int) -> int:
    """
    Helper function for find_most_active_cookies. Finds
    the right-most cookie that occurrs 
    on a targetDate in a list of cookies sorted in order 
    of decreasing timestamp. Uses binary search.

    ***ASSUMPTION: the list of cookies and timestamps are
    sorted in order of decreasing timestamp as per given
    in the log file. 

    Average case time complexity: O(log n)

    Parameters
    ----------
    cmpTimeStamps : List[int]
        List of cookie timestamps stored as integers 
        in sorted descending order. 
    cmpDate : int
        The target date we wish to determine the leftmost
        cookie of. 

    Returns
    -------
    int
        The index of the right-most cookie that occurs
        on cmpDate. -1 if no cookie falls on cmpDate.
    """

    rightmost = -1
    l = 0; r = len(cmpTimeStamps)-1
    while l <= r:
        m = l+int((r-l)/2)
        if cmpTimeStamps[m] >= cmpDate: 
            rightmost = m 
            l = m+1 # found cookie >= cmpDate, can we do better?
        else:
            r = m-1 
    return rightmost


def get_left_cookie(cmpTimeStamps: List[int], cmpDate: int) -> int:
    """
    Helper function for find_most_active_cookies. Finds
    the left-most cookie that occurrs 
    on a targetDate in a list of cookies sorted in order 
    of decreasing timestamp. Uses binary search.

    ***ASSUMPTION: the list of cookies and timestamps are
    sorted in order of decreasing timestamp as per given
    in the log file. 

    Average case time complexity: O(log n)

    Parameters
    ----------
    cmpTimeStamps : List[int]
        List of cookie timestamps stored as integers 
        in sorted descending order. 
    cmpDate : int
        The target date we wish to determine the leftmost
        cookie of. 

    Returns
    -------
    int
        The index of the right-most cookie that occurs
        on a date strictly greater than cmp date (which
        determines the left-most cookie that occurs
        on cmpDate).
        -1 if no such cookie exists.
    """

    rightmost = -1
    l = 0; r = len(cmpTimeStamps)-1
    while l <= r:
        m = l+int((r-l)/2)
        if cmpTimeStamps[m] > cmpDate:
            rightmost = m
            l = m+1 # found cookie > cmpDate, can we do better? 
        else: 
            r = m-1
    return rightmost


def find_most_active_cookies(lines: List[str], targetDate: str) -> List[str]:
    """
    Takes a list of cookies and timestamps and returns
    a list of cookies that occur most frequently on
    a given timestamp using a binary search.

    ***ASSUMPTION: the list of cookies and timestamps are
    sorted in order of decreasing timestamp as per given
    in the log file. 

    Average case time complexity: O(log n)

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
    # determine the left and right endpoints of the window of cookies 
    # that occurr on targetDate using binary search
    occurrences = {}  # mapping from cookie to number of occurences on targetDate

    cmpDate = int(''.join(targetDate.split('-'))) # condense targetDate into the integer "YYYYMMDD" for comparison
    strTimeStamps = [line.split(',')[1] for line in lines] # list of cookie timestamps as strings
    cmpTimeStamps = [int(''.join(timestamp.split('-'))[:8]) for timestamp in strTimeStamps] #condense timestamps into integers "YYYYMMDD" for comparison.
    
    l = get_left_cookie(cmpTimeStamps, cmpDate) # find leftmost cookie that falls on targetDate
    r = get_right_cookie(cmpTimeStamps, cmpDate) # find rightmost cookie that falls on targetDate

    if r == -1 \
        or cmpTimeStamps[r] != cmpDate: # if targetDate isn't in lines
        return []

    for i in range(l+1, r+1): # iterate through cookies that occurr on targetDate
        cookie, timestamp = lines[i].split(',')
        if cookie not in occurrences:
            occurrences[cookie] = 0
        occurrences[cookie] += 1
    
    # print cookie with most occurences, including those tied for most occurences
    # runs in in O(n) time and O(n) space

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
    on a given date in a given well-formatted log file. 
    
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
        print("Error: invalid command, to use run ./most_active_cookie_optimized.py <filepath> -d <date>")

    for most_active_cookie in most_active_cookies_from_file(filepath, targetDate):
        print(most_active_cookie)
