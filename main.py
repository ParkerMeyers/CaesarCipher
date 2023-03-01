class CaeserCipher:
    """
    A class to handle caesar cipher encryption and decryption.

    ...

    Methods
    -------
    decode_key(text, key)
        Decodes a string using a caesar cipher with a given key.
    decode(text)
        Decodes a string using a caesar cipher with all possible keys.
    encode(text, key)
        Encodes a string using a caesar cipher with a given key.
    """

    def __init__(self):
        pass

    def decode_key(self, text, key):
        """Decodes a string using a caesar cipher with a given key.

        Keyword arguments:
        text -- the string to decode
        key -- the key to decode the string with
        """
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

    def decode(self, text):
        """Decodes a string using a caesar cipher with all possible keys.

        Keyword arguments:
        text -- the string to decode
        """
        new_string = ""
        key = 1
        while key <= 25:
            new_string += "Hacking key " + str(key) + ": " + self.decode_key(text, key) + "\n"
            key += 1
        return new_string

    def encode(self, text, key):
        """Encodes a string using a caesar cipher with a given key.

        Keyword arguments:
        text -- the string to encode
        key -- the key to encode the string with
        """
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

caeser_cipher = CaeserCipher()
print(caeser_cipher.decode(caeser_cipher.encode("Hello World", 1)))