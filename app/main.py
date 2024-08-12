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


    if file_contents:
        return_code = scan_for_tokens(file_contents)


    print("EOF  null") # Placeholder, remove this line when implementing the scanner
    exit(return_code)


def scan_for_tokens(content):
    return_code= 0
    tokens = {"(" : "LEFT_PAREN", ")": "RIGHT_PAREN", 
              "{" : "LEFT_BRACE", "}" : "RIGHT_BRACE",
              ".": "DOT", "," : "COMMA", "+": "PLUS",
              "*": "STAR", "-": "MINUS", ";": "SEMICOLON"}
    invalid_tokens = set(["$", "#", "@"])
    line_number  = 1    
    for chr in  content:
        if chr in tokens:
            print(tokens[chr], chr , "null")
        elif chr in invalid_tokens:
            print(f"[line {line_number}] Error: Unexpected character: {chr}", file= sys.stderr)
            return_code = 65
        elif chr == "\n":
            line_number += 1
    return return_code
        
    

if __name__ == "__main__":
    main()
