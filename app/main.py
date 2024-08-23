import sys

class Scanner():

    def __init__(self):
        self.uni_character_token = {"(" : "LEFT_PAREN", ")": "RIGHT_PAREN", 
                                    "{" : "LEFT_BRACE", "}" : "RIGHT_BRACE",
                                    ".": "DOT", "," : "COMMA", "+": "PLUS",
                                    "*": "STAR", "-": "MINUS", ";": "SEMICOLON",
                                    "=" : "EQUAL", "!" : "BANG" ,"<" : "LESS",
                                    ">":"GREATER"}
        self.bi_character_token = {"==" : "EQUAL_EQUAL","!=" :"BANG_EQUAL",
                                   "<=" : "LESS_EQUAL",
                                   ">=":"GREATER_EQUAL"}
        
        self.invalid_tokens = set(["$", "#", "@", "%"])
    
    def scan_content(self, content):
        exit_code = 0
        n =  len(content)
        i = 0
        line_number = 1
        while (i < n):
            if content[i] == "\n":
                line_number +=1
                i+=1
            elif content[i] in  self.invalid_tokens:
                print(f"[line {line_number}] Error: Unexpected character: {content[i]}", file= sys.stderr)
                exit_code = 65
                i+=1
            elif i+1 < n and content[i]+content[i+1] in self.bi_character_token:
                ele = content[i] + content[i+1]
                print(self.bi_character_token[ele]  , ele , "null")
                i+=2
            elif content[i] in self.uni_character_token:
                print(self.uni_character_token[content[i]] , content[i] , "null")
                i+=1
        print("EOF" ,"", "null") 
        return exit_code

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

    return_code = Scanner().scan_content(file_contents)

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
