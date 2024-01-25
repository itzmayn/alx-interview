#!/usr/bin/python3
"""
Log Parsing Script
"""

import sys

def print_msg(dict_sc, total_file_size):
    """
    Method to print statistics.
    
    Args:
        dict_sc (dict): Dictionary containing status codes and their counts.
        total_file_size (int): Total size of the files.
    
    Returns:
        None
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the input line into tokens
        parsed_line = parsed_line[::-1]  # Reverse the list (inverting)

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # Extract and accumulate file size
                code = parsed_line[1]  # Extract status code

                if code in dict_sc:
                    dict_sc[code] += 1  # Update status code count

            if counter == 10:
                print_msg(dict_sc, total_file_size)  # Print statistics after processing 10 lines
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)  # Print final statistics after processing all lines
