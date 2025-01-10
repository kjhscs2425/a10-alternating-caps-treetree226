coolphrase = input('Enter your word: ')
word = ""
for thingy, letter in enumerate(coolphrase):
    word += letter.upper() if thingy % 2 else letter
print(word)

#since i couldn't ask for help at schoolV (was sick), i found this
# https://www.reddit.com/r/learnpython/comments/n09o5r/program_to_capitalize_every_alternate_letter/?rdt=60401
#to help me. i used the same formatting for the code and made the variables different names. 