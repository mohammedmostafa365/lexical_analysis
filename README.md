# Lexical Analyzer

This project performs **lexical analysis** on simple C-like code.  
It scans the input source code and splits it into tokens, identifying the type of each element.

---

## Project Idea

A **lexer** is the first stage of a compiler.  
Its job is to **scan the code** and recognize every word or symbol based on its type.

The main token types recognized by this program are:

1. **Keyword** — reserved words like `int`, `float`, `if`, `else`, `while`, `return`  
2. **Identifier** — variable names starting with a letter or `_`  
3. **Number** — integer or floating-point numbers  
4. **Operator** — arithmetic and logical operators like `+`, `-`, `*`, `/`, `==`, `>=`  
5. **Delimiter** — separators like `(`, `)`, `{`, `}`, `;`, `,`  
6. **Invalid Identifier** — variable names that don’t follow valid naming rules (e.g., `1num`)  
7. **Unknown** — any unrecognized symbol  

---

## Features

- Uses **regular expressions (regex)** to validate identifiers and numbers.  
- Prints clear, organized output showing each token and its type.  
- Easy to modify or extend with new token types.  

---

## Example

Input code:

```c
int x1 = 5;
float _y = 2.3;
int 1num = 10;
if (x1 > _y) { total = x1 + _y; }
