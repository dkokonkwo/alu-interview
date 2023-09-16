#!/usr/bin/python3

def minOperations(n):
    char = 1
    count = 0
    while char != n:
        if char == 1:
            char = char + 1
            count += 2
        if n % 2 == 0 and n % 3 != 0:
            char = char * 2
            count += 2
        if n % 3 == 0:
            if char == 2:
                char = char + 1
                count += 1
            if n / char == 2:
                char = char * 2
                count += 2
            if char == 3:
                char = char * 2
                count += 2
            elif char > 3 and char < n:
                char = char + 3
                count += 1
    return count
