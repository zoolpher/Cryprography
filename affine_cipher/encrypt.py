def encrypt_affine():
    plain_text = input("Enter the text you want to encrypt : ")
    a = int(input("Enter value of 'A' : "))
    b = int(input("Enter value of 'B' : "))
    ct = ""
    for char in plain_text:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')
            y = (a * x + b) % 26
            ct += chr(y + ord('a'))
        else:
            ct += char
    return ct

cipher = encrypt_affine()
print("Encrypted:", cipher)
