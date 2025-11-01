from lexer import lexer
from parser import parser

def parse_rust(code):
    try:
        result = parser.parse(code, lexer=lexer)
        print("✅ Parsing successful!")
        return result
    except SyntaxError as e:
        print(f"❌ {e}")
        return None

test1 = "x = 10;\ny = 20;"
test2 = "fun main() {\n  x = 5;\n  y = 10;\n}"
test3 = "if condition {\n  print;\n} else {\n  print;\n}"
test4 = "while condition {\n  i = i;\n}"
test5 = "for i in 1..5 {\n  print;\n}"
test6 = "fun main() {\n x = 5;\n}"
test7 = "x : 18;\ny : 19;"

tests = [
    ("Variable declarations", test1),
    ("Function definition", test2),
    ("If statement", test3),
    ("While loop", test4),
    ("For loop", test5),
    ("Function with assignment", test6),
    ("Type declarations", test7)
]

print("RUST PARSER TEST")
print("=" * 50)

for name, test in tests:
    print(f"\n{name}:")
    print("-" * 20)
    print(f"Code:\n{test}")
    result = parse_rust(test)
    if result:
        print(f"AST: {result}")
