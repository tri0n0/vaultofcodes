take = input("Enter the word to check: ").lower()
if take == take[::-1]:
    print(f"{take} is palindrome.")
else: 
    print(f"{take} is not palindrome.")