import sys
import getopt   
import os

def main(argv):
    opts, args = getopt.getopt(argv, "c:l:")

    for opt, arg in opts:
        match opt:
            case '-c':
                get_bytes(arg)        
            case '-l':
                get_lines(arg)

def get_bytes(file_name):
    print(os.path.getsize(file_name),file_name)

def get_lines(file_name):
    num_lines = 0
    with open(file_name) as file_handler:
        for line in file_handler:
            num_lines += 1
    print(num_lines, file_name)

if __name__ == "__main__":
    main(sys.argv[1:])