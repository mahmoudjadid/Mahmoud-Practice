
def swapcases(s):
    result = ""
    for char in s:
        if char.islower():
         result += char.upper()
        elif char.isupper():
         result+=char.lower()
        else :
         result += char
    return result
    
word = input("enter a word: ")
print(swapcases(word))
