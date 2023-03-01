def decode_key(text, key):
    new_string = ""
    for char in text:
        if char != " ":
            new_char = chr(int(((ord(char.lower()) - 97) - key) % 26) + 97)
        else:
            new_char = " "
        if char.isupper():
            new_char = new_char.upper()
        new_string += new_char
    return new_string

def decode(text):
    new_string = ""
    key = 1
    while key <= 25:
        new_string += "Hacking key " + str(key) + ": " + decode_key(text, key) + "\n"
        key += 1
    return new_string

def encode(text, key):
    new_string = ""
    for char in text:
        if char != " ":
            new_char = chr(int(((ord(char.lower()) - 97) + key) % 26) + 97)
        else:
            new_char = " "
        if char.isupper():
            new_char = new_char.upper()
        new_string += new_char
    return new_string

print(decode(encode("hello world", 5)))