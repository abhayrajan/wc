# Function that parses command line args
# Function that reads bytes

import sys
import getopt   
import os

def main(argv):
    opts, args = getopt.getopt(argv, "-c:")

    for opt, arg in opts:
        if opt == '-c':
            get_bytes(arg)

def get_bytes(file_name):
    print(os.path.getsize(file_name),file_name)

if __name__ == "__main__":
    main(sys.argv[1:])