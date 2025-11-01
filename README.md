# 🦀 Rust Syntax Validator

A simple Rust-like syntax validator built using **PLY (Python Lex-Yacc)**.  
This project demonstrates how to tokenize and parse a subset of Rust’s syntax using Python.

---

## 📘 Features

- Lexical analysis using **PLY’s lexer**
- Grammar parsing with **PLY’s yacc**
- Supports basic Rust-like constructs:
  - Variable declarations and assignments  
  - Type declarations (`x : 10;`)
  - `if` / `else` blocks  
  - `while` loops  
  - `for` loops with ranges (`for i in 1..5 {}`)
  - Function definitions (`fun main() { ... }`)

---