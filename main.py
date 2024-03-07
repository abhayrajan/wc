import sys
import getopt   
import os

def main(argv):
    if not sys.stdin.isatty():
        opts = getopt.getopt(argv, "clmw")
        print(opts)
        return
    else:
        opts, args = getopt.getopt(argv, "c:l:m:w:")
        if not opts or len(opts) == 0:
            if len(args) == 0:
                print("file or stdin required")
                return
            
            print_info(None, args[0])    
            return
        
        print_info(opts[0][0], opts[0][1])        


def print_info(option, file_name):
    if not file_name:
        print("No such file")
        return

    if option == '-c':
        print(os.path.getsize(file_name),file_name)
        return

    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()

        if option == '-l':
              print(len(lines), file_name)
              return            

        words, chars = get_word_char_counts(lines)
    
        if option == '-w':
            print(words, file_name)
            return
        
        if option == '-m':
            print(chars, file_name)
            return
        
        if option is None:
            print(len(lines), words, chars, file_name)
            return;        
        
def get_word_char_counts(lines):
    words = 0
    chars = 0

    for line in lines:
        words += len(line.split())
        chars += len(line)

    return (words, chars)

if __name__ == "__main__":
    main(sys.argv[1:])