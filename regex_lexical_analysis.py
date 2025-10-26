"""
الكود ده بيحلل الكود وبيعمله سكان عشان يعرف نوع كل جزء فيه من أنواع التوكنز الخمس
وهم مكتوبين بشكل صح Identifier و Keyword و Number و Operator و Delimiter
وبيستخدم ال regex
عشان يتاكد ان ال identifiers مكتوبه صح  
"""

import re

def lexer(code):
    keywords = ["int", "float", "if", "else", "for", "while", "return"]
    delimiters = ["(", ")", "{", "}", ";", ","]
    operators = ["==", "<=", ">=", "=", "+", "-", "*", "/", "<", ">"]
    
    identifier_pattern = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*$')
    number_pattern = re.compile(r'^\d+(\.\d+)?$')
    
    tokens = []
    word = ""
    i = 0
    length = len(code)
    
    while i < length:
        ch = code[i]
        
        if ch.isalnum() or ch == "_":
            word += ch
        else:
            if word != "":
                if word in keywords:
                    tokens.append((word, "KEYWORD"))
                elif re.match(number_pattern, word):
                    tokens.append((word, "NUMBER"))
                elif re.match(identifier_pattern, word):
                    tokens.append((word, "IDENTIFIER"))
                else:
                    tokens.append((word, "INVALID_IDENTIFIER"))
                word = ""
            
            if i + 1 < length and code[i:i+2] in operators:
                tokens.append((code[i:i+2], "OPERATOR"))
                i += 1
            elif ch in operators:
                tokens.append((ch, "OPERATOR"))
            elif ch in delimiters:
                tokens.append((ch, "DELIMITER"))
            elif ch in [' ', '\t', '\n']:
                pass
            else:
                tokens.append((ch, "UNKNOWN"))
        
        i += 1
    
    return tokens


code = "int x1 = 5; float _y = 2.3; int 1num = 10; if (x1 > _y) { total = x1 + _y; }"
tokens = lexer(code)

for token in tokens:
    print(token[0], "→", token[1])
