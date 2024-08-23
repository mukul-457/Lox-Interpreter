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
        print("EOF" , "null") 
        return exit_code