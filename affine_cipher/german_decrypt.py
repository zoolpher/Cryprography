# This problem deals with the affine cipher with the 
# key parameters  a = 17, b = 1
# Ä Ü ß W ß




letter_to_number = {
    'A': 0,  'B': 1,  'C': 2,  'D': 3,  'E': 4,
    'F': 5,  'G': 6,  'H': 7,  'I': 8,  'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
    'Z': 25,
    'Ä': 26,  # Umlaut A
    'Ö': 27,  # Umlaut O
    'Ü': 28,  # Umlaut U
    'ß': 29   # Sharp S
}

number_to_letter = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'Ä', 'Ö', 'Ü', 'ß'
]


def calc_a_inverse(a) :
    for i in range(1, 30) :
        if (a * i) % 30 == 1 :
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
            y = letter_to_number[char]
            x = (a_inverse * (y - b)) % 30
            pt += number_to_letter[x] 
        else : 
            pt += char
    return pt

plane_text = decrypt_affine()
print(plane_text)

