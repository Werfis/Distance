def main(): char = input("Which character do you want to replace?") 
string = input("Which line do you want to change?") 
result = "" for i in string: 
if i == char: result += "😎" 
else: result += i print(result) 
if name == "main": main()