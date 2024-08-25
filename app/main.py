import sys

class Scanner():

    def __init__(self):
        self.uni_character_token = {"(" : "LEFT_PAREN", ")": "RIGHT_PAREN", 
                                    "{" : "LEFT_BRACE", "}" : "RIGHT_BRACE",
                                    ".": "DOT", "," : "COMMA", "+": "PLUS",
                                    "*": "STAR", "-": "MINUS", ";": "SEMICOLON",
                                    "=" : "EQUAL", "!" : "BANG" ,"<" : "LESS",
                                    ">":"GREATER", "/" : "SLASH"}
        self.bi_character_token = {"==" : "EQUAL_EQUAL","!=" :"BANG_EQUAL",
                                   "<=" : "LESS_EQUAL",
                                   ">=":"GREATER_EQUAL", "//": "COMMENT"}
        
        self.invalid_tokens = set(["$", "#", "@", "%"])

    def scan_file(self,filepath):
        rt = 0
        line_number = 1
        with open(filepath) as file:
            for line in file:
                rt = self.scan_content(line, line_number) or rt 
                line_number+=1
        print("EOF", "" ,"null")
        return rt
    def find(self,chr ,  i ,content, n):
        match_index = -1
        while i < n:
            if content[i] == chr:
                match_index = i
                break
            i+=1
        return match_index
    def scan_content(self, content,line_number):
        exit_code = 0
        n =  len(content)
        i = 0
        while (i < n):
            if content[i] in  self.invalid_tokens:
                print(f"[line {line_number}] Error: Unexpected character: {content[i]}", file= sys.stderr)
                exit_code = 65
                i+=1
            elif i+1 < n and content[i]+content[i+1] in self.bi_character_token:
                ele = content[i] + content[i+1]
                if(ele == "//"):
                    break
                print(self.bi_character_token[ele]  , ele , "null")
                i+=2
            elif content[i] in self.uni_character_token:
                print(self.uni_character_token[content[i]] , content[i] , "null")
                i+=1
            elif content[i] == '"':
                index = self.find('"', i+1, content, n)
                if index != -1 :
                    print("STRING" ,content[i:index+1], content[i+1:index])
                    i = index+1
                else:
                    print(f"[line {line_number}] Error: Unterminated String.", file= sys.stderr)
                    break
            else:
                i+=1
        return exit_code

def main():
    # # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        print(sys.argv)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    scaner = Scanner()
    exit_code = scaner.scan_file(filename)
    exit(exit_code)    

if __name__ == "__main__":
    main()
