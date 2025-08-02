
# This code decrypt cipher text without and key stream or 
# without any value of 'a' and 'b' 

# This program is @incomplete
# I am so confused about this program 


dict_ = {chr(i + 97) : i for i in range(26)}
print(dict_)


def brute_force_decrypt() :
    pass

def key_stream_decrypt(list_) :
    pass

def decrypt_func () :
    c_t = input("Enter cipher text : ")
    list_ = list(input("Enter the key stream : "))
    if (list_ == []) :
        brute_force_decrypt()
        return()
    key_stream_decrypt(list_)
    



decrypt_func()