# This problem deals with the affine cipher with the 
# key parameters a=7,b=22
# Decrypt the text below:
# falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj
# falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj


def calc_a_inverse(a) :
    for i in range(1, 26) :
        if (a * i) % 26 == 1 :
            return i
    return 0



def decrypt_affine() :
    cipher_text = input("Enter the cipher text :\n")
    a = int(input("Enter value of 'A' : "))
    b = int(input("Enter value of 'B' : "))
    a_inverse = calc_a_inverse(a)
    pt = ""  
    if a_inverse == 0 :
        raise Exception("The inverse is 0; which is not possible !!!")
    
    for char in cipher_text :
        if char.isalpha() :
            y = ord(char.lower()) - ord('a')
            x = (a_inverse * (y - b)) % 26
            pt += chr(x + ord('a'))
        else : 
            pt += char
    return pt

plane_text = decrypt_affine()
print(plane_text)

# first the sentence and then the evidence said the queen
