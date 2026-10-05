# name = input("Enter a name: ")
# date = input("Enter a date: ")

# letter = f'''
#          Dear {name},
#          You are selected!
#          {date}
#          '''
# print(letter)

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Yash").replace("<|Date|>", "22nd December 2025"))