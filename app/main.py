import sys


def main():
    # # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    return_code = scan_for_tokens(file_contents)

    print("EOF  null") # Placeholder, remove this line when implementing the scanner
    exit(return_code)


def scan_for_tokens(content):
    return_code= 0
    tokens = {"(" : "LEFT_PAREN", ")": "RIGHT_PAREN", 
              "{" : "LEFT_BRACE", "}" : "RIGHT_BRACE",
              ".": "DOT", "," : "COMMA", "+": "PLUS",
              "*": "STAR", "-": "MINUS", ";": "SEMICOLON"}
    invalid_tokens = set(["$", "#", "@", "%"])
    line_number  = 1
    equals = 0
    bangs= 0    
    for chr in  content:
        if equals and chr != "=":
            print("EQUAL = null")
            equals= 0
        if bangs and chr != "=":
            print("BANG ! null")
            bangs = 0
        if chr in tokens:
            print(tokens[chr], chr , "null")
        elif chr in invalid_tokens:
            print(f"[line {line_number}] Error: Unexpected character: {chr}", file= sys.stderr)
            return_code = 65
        elif chr == "\n":
            line_number += 1
        elif chr == "=":
            if equals:
                print("EQUAL_EQUAL == null")
                equals = 0
            elif bangs:
                print("BANG_EQUAL != null")
                bangs = 0
            else:
                equals += 1
        elif chr == "!":
            bangs += 1

    if equals:
        print("EQUAL = null")
    if bangs:
        print("BANG ! null")

    return return_code
        
    

if __name__ == "__main__":
    main()
