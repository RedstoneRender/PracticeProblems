text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

characters = {}

for i in text:
    if i in characters:
        characters[i] += 1
    else:
        characters[i] = 1

for i in characters:
    print("The character '" + i + "' appears in the text " + str(characters[i]) + " times. It makes up " + str(float(characters[i])/float(len(text))) + "% of the text.")
