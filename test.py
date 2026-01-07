def calcul_occurrences(text, char):
    
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

text = "hello everyone i hope you are doing well"
char = "e"
print(calcul_occurrences(text, char))