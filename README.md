# LeetCode #767: Reorganize String (Daily Challenge 08/23/2023)
This repository contains a Python 3 solution to the LeetCode daily challenge #767 for 08/23/2023. https://leetcode.com/problems/reorganize-string/

This solution beats 85.26% of users in runtime (39 ms) and 46.15% of users in memory usage (16.32 MB).

## Running
The Python solution can be run with
```
python3 reorganize_string.py
```

There are no arguments; the test cases are hard-coded into the Python file. Example output:

```
Testing Report
--------------------------------------------------------------------------------------------------------
reorganizeString("aab"): aba
\--------------Expected: aba
Test case 1 passed!

reorganizeString("aaab"): 
\---------------Expected: 
Test case 2 passed!

reorganizeString("aaabc"): abaca
\----------------Expected: abaca
Test case 3 passed!

reorganizeString("aaaabcd"): abacada
\------------------Expected: abacada
Test case 4 passed!

reorganizeString("aaaabbbb"): abababab
\-------------------Expected: abababab
Test case 5 passed!

reorganizeString("bfrbs"): bfbrs
\----------------Expected: bfbrs
Test case 6 passed!

reorganizeString("zhmyo"): zhmyo
\----------------Expected: zhmyo
Test case 7 passed!

reorganizeString("cxmwmmm"): mcmxmwm
\------------------Expected: mcmxmwm
Test case 8 passed!

reorganizeString("mjpssblxurlkotcdsvzfc... (479 more chars)"): azamzmzmzmzmzmzmzmzmz... (479 more chars)
\----------------------------------------------------Expected: azamzmzmzmzmzmzmzmzmz... (479 more chars)
Test case 9 passed!

Test cases passed: 100.0%
--------------------------------------------------------------------------------------------------------
```