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