def lexer(code):
    keywords = ["int", "float", "if", "else", "for", "while"]
    delimiters = "*/(){};"
    operators = ["*", "-", "+", "/", "**", "||", "&&", "="]
    
    word = ""
    for ch in code + " ":  
        if ch.isalnum() or ch == "_":  
            word += ch
        else:
            if word != "":
                if word in keywords:
                    print(word, "→ KEYWORD")
                elif word.isdigit():
                    print(word, "→ NUMBER")
                else:
                    print(word, "→ IDENTIFIER")
                word = ""
            
            if ch in delimiters:
                print(ch, "→ DELIMITER")
            elif ch in operators:
                print(ch, "→ OPERATOR")

# مثال:
code = "int x = 5; if (x > 2) { x = x + 1; }"
lexer(code)
