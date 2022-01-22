
# Online Python - IDE, Editor, Compiler, Interpreter
numeroPares = []

for i in range(10, 21):
    if i % 2 == 0:
        numeroPares.append(i)
    
numeroPares.sort(reverse = True)
print(numeroPares)
    
