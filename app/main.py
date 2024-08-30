import sys
from enum import Enum, auto
import re 
ERROR = False


class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    DOT = auto() 
    COMMA = auto()
    PLUS = auto()
    STAR = auto()
    MINUS = auto()
    SSEMICOLON = auto()
    EQUAL = auto()
    BANG = auto()
    LESS = auto()
    GREATER = auto()
    SLASH = auto()

    EQUAL_EQUAL=auto()
    BANG_EQUAL=auto()
    LESS_EQUAL=auto()
    GREATER_EQUAL=auto()
    COMMENT=auto()

    IDENTIFIER=auto()
    STRING=auto()
    NUMBER=auto()

    AND=auto()
    CLASS=auto()
    ELSE=auto()
    FALSE=auto()
    FUN=auto()
    FOR=auto()
    IF=auto()
    NIL=auto()
    OR=auto()
    PRINT=auto()
    RETURN=auto()
    SUPER=auto()
    THIS=auto()
    TRUE=auto()
    VAR=auto()
    WHILE=auto()

    EOF=auto()


class Token:

    def __init__(self, token_type:TokenType, lexeme:str, literal:object,  line:int):
        self.type  = token_type
        self.lexeme  = lexeme
        self.literal = literal
        self.line = line
    def __str__(self) -> str:
        return self.type.name + " " + self.lexeme + " " + str(self.literal)

class Scanner1():

    def __init__(self,source) -> None:
        self.source = source
        self.tokens = []
        self.start = 0 
        self.current = 0
        self.line  = 1
    
    def is_at_end(self):
        return self.current >= len(self.source)
    
    def advance(self):
        chr = self.source[self.current]
        self.current += 1
        return chr
    
    def match(self, ch:str) -> bool:
        if self.is_at_end():
            return False
        if self.source[self.current] != ch :
            return False
        self.current+=1
        return True
    
    def peek(self) -> str:
        if not self.is_at_end():
            return self.source[self.current]

    def scan_tokens(self):
        while(not self.is_at_end()):
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, "" ,"null" ,self.line))
        return self.tokens
    
    def add_token(self, token_type , literal="null"):
        lexeme = self.source[self.start:self.current]
        self.tokens.append(Token(token_type,lexeme ,literal,self.line))
    
    def handle_string(self):
        while not self.is_at_end() and self.peek() != '"':
            if self.peek() == "\n":
                report_error(self.line , "Unterminated string.")
                break
            else:
                self.advance()
        if self.is_at_end():
            report_error(self.line , "Unterminated string.")
        else:
            self.advance()
            self.add_token(TokenType.STRING , self.source[self.start+1: self.current-1])
            
    def handle_number(self):
        pattern = re.compile("[0-9]")
        while not self.is_at_end() and pattern.match(self.peek()):
            self.advance()
        if self.is_at_end() or self.peek()!= ".":
            self.add_token(TokenType.NUMBER, float(self.source[self.start:self.current]))
        else:
            self.advance()
            if self.is_at_end() or not pattern.match(self.peek()):
                 self.add_token(TokenType.NUMBER, float(self.source[self.start:self.current-1]))
                 self.start = self.current-1
                 self.add_token(TokenType.DOT)
            else:
                while not self.is_at_end() and pattern.match(self.peek()):
                    self.advance()
                self.add_token(TokenType.NUMBER , float(self.source[self.start:self.current]))
        

    def scan_token(self):
        digits  = re.compile("[0-9]")
        chr = self.advance()
        match chr:
            case "\n":
                self.line += 1
            case '(' :
                self.add_token(TokenType.LEFT_PAREN )
            case ')':
                self.add_token(TokenType.RIGHT_PAREN)
            case '{':
                self.add_token(TokenType.LEFT_BRACE)
            case '}':
                self.add_token(TokenType.RIGHT_BRACE)
            case ",":
                self.add_token(TokenType.COMMA)
            case ".":
                self.add_token(TokenType.DOT)
            case "-" :
                self.add_token(TokenType.SSEMICOLON)
            case "*":
                self.add_token(TokenType.STAR)
            case "+":
                self.add_token(TokenType.PLUS)
            case "=":
                if self.match("="):
                    self.add_token(TokenType.EQUAL_EQUAL)
                else:
                    self.add_token(TokenType.EQUAL)
            case "!":
                if self.match("="):
                    self.add_token(TokenType.BANG_EQUAL)
                else:
                    self.add_token(TokenType.BANG)
            case "<":
                if self.match("="):
                    self.add_token(TokenType.LESS_EQUAL)
                else:
                    self.add_token(TokenType.LESS)
            case ">":
                if self.match("="):
                    self.add_token(TokenType.GREATER_EQUAL)
                else:
                    self.add_token(TokenType.GREATER)
            case chr if digits.match(chr):
                self.handle_number()
            case '"':
                self.handle_string()
            case " ":
                pass
            case "\t":
                pass
            case "/":
                if self.match("/"):
                    while not self.is_at_end()and self.peek() != "\n":
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case _:
                report_error(self.line , f"Unexpected character:{chr}")

                        
            

    


def runFile(filename) -> None:
    with open(filename) as f:
        source  = f.read()
        run(source=source)


def runPrompt():
    while 1:
        src = input(">")
        if src == "exit":
            break
        run(src)


def run(source: str) -> None:
    scanner  = Scanner1(source)
    tokens = scanner.scan_tokens()
    for t in tokens:
        print(t)

def report_error(line:int , message:str , where=""):
    global ERROR
    print(f"[line {line}] Error {where}: {message}", file=sys.stderr)
    ERROR = True

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

    runFile(filename=filename)

    if ERROR:
        exit(65)
    else:
        exit(0)

    # scaner = Scanner()
    # exit_code = scaner.scan_file(filename)
    # exit(exit_code)    

if __name__ == "__main__":
    main()
