

class Prng :
    
    def __init__(self, seed, a, b) :
        self.modulo = 2**31 
        self.seed = seed
        self.a = a
        self.b = b
        self.key_stream = []

    def next_key(self) :
        self.seed = (self.a * self.seed + self.b) % self.modulo
        return self.seed
    
    def next_alphabet_index(self):
        # Return a number between 0 and 25
        key_val = self.next_key()
        key_index = key_val % 26
        # print(f"PRNG raw value: {key_val}, key index (mod 26): {key_index}")
        self.key_stream.append(key_index)
        return key_index

    def next_asci_value(self) :
        # return chr(ord('a') + self.next_alphabet_index())
        return (ord('a') + self.next_alphabet_index())
    
    def get_key_stream(self) :
        return self.key_stream




class Encrypt(Prng):

    def __init__(self, seed, a, b, plane_text):
        super().__init__(seed, a, b)
        self.plane_text = plane_text
        self.dict_ = {chr(i + 97) : i for i in range(26)}
        self.list_ = [chr(i + 97) for i in range(26)] 
        self.cipher_text = ""

    def ciphered_text(self) :
        
        if (len(self.plane_text) == 0) :
            print("No input provided.")
            return
        
        for char in self.plane_text :
            if (char.isalpha()) :
                char = char.lower()
                plain_char_index = self.dict_[char]
                key_index = self.next_alphabet_index()
                cipher_index = (plain_char_index + key_index) % 26
                self.cipher_text += (self.list_[cipher_index])   
            else:
                self.cipher_text += char
        return self.cipher_text;
    

seed = int(input("Enter a seed value : "))
a = int(input("Enter a A value : "))
b = int(input("Enter a B value : "))
plane_text = input("Enter the plane text : ")

encrypt_obj = Encrypt(seed, a, b, plane_text)
cipher_text = encrypt_obj.ciphered_text()
key_stream = encrypt_obj.get_key_stream()
print(f"{cipher_text} \n{key_stream}")
