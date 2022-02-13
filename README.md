# Eluvio Assessment

## Problem Statement

Given a large number of binary files, write a program that finds the
longest strand of bytes that is identical between two or more files

Use the test set attached (files sample.*)

The program should display:
- the length of the strand
- the file names where the largest strand appears
- the offset where the strand appears in each file

## Solution

Below is a high level description to identify the longest strand of bytes common in atleast 2 files,

- Consider a pair of files at a time.
- Use dynamic programming to efficiently identify the longest strand between the pair of files.
- Store the strand and file details (name and offset) in a hash map which enables us to find the longest strand accross all files.

Programming Language:
- Python 2.7.16

Entry Point/Main file:
- src/main.py

Excecution steps:
- ```cd src```
- ```python main.py```

Results:
- Stored in src/results.txt and displayed in console

Sample Results:
```
 Max length of Strand = 27648
 File Name = sample.2 Offset = 3072
 File Name = sample.3 Offset = 17408
```

Overall Time Complexity:
- O((k*(k-1)/2)*n^2), k = files count, n = file size

Execution Time:
- Approximately 30 minutes
