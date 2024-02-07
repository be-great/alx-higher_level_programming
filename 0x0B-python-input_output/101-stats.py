#!/usr/bin/python3
"""
script that reads
stdin parts by parts and computes metrics:
"""


def print_cumulative_stats(size, status):
    """
    Args: (int) size , (status_code)
    """
    print("File size: {}".format(size))
    for key in sorted(status):
        print("{}: {}".format(key, status[key]))


if __name__ == "__main__":
    import sys
    size = 0
    length = 0
    status = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for parts in sys.stdin:
            # Check if it's time to print statistics
            if length == 10:
                print_cumulative_stats(size, status)
                length = 1
            else:
                length += 1

            # Split the input parts and process the information
            parts = parts.split()

            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in codes:
                    if status.get(parts[-2], -1) == -1:
                        status[parts[-2]] = 1
                    else:
                        status[parts[-2]] += 1
            except IndexError:
                pass
        # Print final statistics
        print_cumulative_stats(size, status)

    except KeyboardInterrupt:
        # Handle CTRL+C interruption and print final statistics
        print_cumulative_stats(size, status)
        raise
