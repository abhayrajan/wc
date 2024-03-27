import sys
import getopt   
from enum import Enum

# TODO 
# create supported options string
# cleanup stream
# handle exceptions
# unit tests

def main(argv):
        opts, args = get_opts(argv)

        input = parse_opts(opts)

        stream, file_name = get_stream(opts, args)

        match input:
            case ProgramOptions.BYTES:
                print_counts(file_name, len(bytes(stream.read(), 'utf-8')))
            case ProgramOptions.LINES:
                print_counts(file_name, len(stream.readlines()))
            case ProgramOptions.WORDS:
                numWords = get_word_counts(stream.readlines())
                print_counts(file_name, numWords)
            case ProgramOptions.CHARS:
                numChars = get_char_counts(stream.readlines())
                print_counts(file_name, numChars)
            case ProgramOptions.NONE:
                lines = stream.readlines()
                numWords = get_word_counts(lines)
                numChars = get_char_counts(lines)
                print_counts(file_name, len(lines), numWords, numChars) 

def parse_opts(opts):
    if not opts or len(opts) == 0 or len(opts[0]) == 0:    
        return ProgramOptions.NONE
    if opts[0][0] == '-c':
        return ProgramOptions.BYTES
    if opts[0][0] == '-l':
        return ProgramOptions.LINES    
    if opts[0][0] == '-w':
        return ProgramOptions.WORDS    
    if opts[0][0] == '-m':
        return ProgramOptions.CHARS        

def get_opts(argv):
    if not sys.stdin.isatty():    
        return getopt.getopt(argv, "clmw")
    else:
        return getopt.getopt(argv, "c:l:m:w:")
    
def get_stream(opts, args):
    if not sys.stdin.isatty():
        return (sys.stdin, None)
    else:
        return get_file(opts, args)

def get_file(opts, args):
    if not opts or len(opts) == 0:        
        if not args or len(args) == 0:
            raise Exception('no such file')
        else:
            return (open(args[0], "r", encoding="utf-8"), args[0])
    
    if not opts[0][1]:
        raise Exception('no such file')
    
    return (open(opts[0][1], "r", encoding="utf-8"), opts[0][1])

def get_word_counts(lines):
    num_words = 0

    for line in lines:
        num_words += len(line.split())

    return num_words
        
def get_char_counts(lines):
    num_chars = 0

    for line in lines:
        num_chars += len(line)

    return num_chars

def print_counts(file_name, *counts):
    if not file_name:
        print(*counts)
    else:    
        print(*counts, file_name)

class ProgramOptions(Enum):
    NONE = 0
    BYTES = 1
    LINES = 2
    WORDS = 3
    CHARS = 4

if __name__ == "__main__":
    main(sys.argv[1:])