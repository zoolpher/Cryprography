

class Decrypt():
    def __init__(self, cipher_text, key_stream):
        self.cipher_text = cipher_text
        self.key_stream = key_stream
        self.plain_text = ""
        self.list_ = [chr(i + ord('a')) for i in range(26)]
        self.dict_ = {chr(i + 97) : i for i in range(26)}

    def decrypt_cipher_text(self) :
            if (len(self.cipher_text) == 0) :
                print("No input provided.")
                return
            
            for i in range(len(self.cipher_text)) :
                char = self.cipher_text[i]
                if (char.isalpha()) :
                    char = char.lower()
                    cipher_index = self.dict_[char]
                    key_index = self.key_stream[i]
                    plain_text_index = (cipher_index - key_index)  % 26
                    self.plain_text += self.list_[plain_text_index]
                else:
                    self.plain_text += char
            return self.plain_text;
    

cipher_text = input("Enter the cipher text : ")
key_stream = input("Enter key stream : ") # Enter spaced values
numbers = list(map(int, key_stream.split()))

decrypt_obj = Decrypt(cipher_text, numbers)
plain_text = decrypt_obj.decrypt_cipher_text()
print(plain_text)


# Problem in type of key_stream 
# somewhere it is list,
# somewhere it is string,
# somewhere it is string of list 

# iqwrp 
# [1, 12, 11, 6, 1]