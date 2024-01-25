#!/usr/bin/python3
"""
Log parsing script.
"""

import sys

if __name__ == '__main__':
    # Initialize variables to track total file size and line count
    filesize, count = 0, 0
    
    # List of status codes to monitor
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    
    # Dictionary to store the count of each status code
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Helper function to print accumulated statistics.
        """
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        # Read input lines from stdin
        for line in sys.stdin:
            count += 1
            
            # Split the line into data components
            data = line.split()
            
            try:
                # Extract the status code from the data
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                # Ignore exceptions related to status code extraction
                pass
            
            try:
                # Extract the file size from the data and update the total file size
                filesize += int(data[-1])
            except BaseException:
                # Ignore exceptions related to file size extraction
                pass
            
            # Print statistics after every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)
        
        # Print final statistics
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        # Handle keyboard interruption by printing current statistics
        print_stats(stats, filesize)
        raise
