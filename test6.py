def encrypt(words, key):
    literrals = ""
    for i in words:
        if (65 <= ord(i.upper()) <= 90):
            newPosition = ord(i.upper())+key
            print(i, " = > ", chr(newPosition), " | ", ord(i.upper()), " = > ", newPosition,
                  " | ", newPosition if (newPosition <= 90) else (newPosition-90+65))
            literrals += chr(newPosition) if (newPosition <=
                                              90) else chr(newPosition-90+65)
        else:
            literrals += i
    words = literrals
    return words

word = "Hello, World!"
print(encrypt(word, 10))
