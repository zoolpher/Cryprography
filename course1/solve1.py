
# 1.1. The ciphertext below was encrypted using a substitution 
# cipher. Decrypt the ci phertext without knowledge of the key.


#  lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
#  bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
#  ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
#  yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
#  lmird jk xjubt trmui jx ibndt
#  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
#  iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
#  vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
#  wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
#  jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
#  ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
#  mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
#  bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
#  wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
#  riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb



_dict = {}
frequency_dict = {}

english_letter_freq = {
    'A': 0.0817,'B': 0.0150,'C': 0.0278,'D': 0.0425,
    'E': 0.1270,'F': 0.0223,'G': 0.0202,'H': 0.0609,
    'I': 0.0697,'J': 0.0015,'K': 0.0077,'L': 0.0403,
    'M': 0.0241,'N': 0.0675,'O': 0.0751,'P': 0.0193,
    'Q': 0.0010,'R': 0.0599,'S': 0.0633,'T': 0.0906,
    'U': 0.0276,'V': 0.0098,'W': 0.0236,'X': 0.0015,
    'Y': 0.0197,'Z': 0.0007
}

cipher_text = input("Enter the cipher text: ")

def print_dict(d) :
    if d == "_dict": 
        for k, v in sorted(_dict.items()) :
            print(f'{k} -> {v:.4f}')
    else :
        for k, v in sorted(_dict.items()) :
            print(f'{k} -> {v:.4f}')


def filling_cipher_dict() :
    for i in range(len(cipher_text)) :
        if cipher_text[i].isalpha():  # only count A-Z characters
            if cipher_text[i] in _dict.keys() :
                _dict[cipher_text[i]] += 1
            elif cipher_text[i] == ' ' :
                pass
            else :
                _dict[cipher_text[i]] = 1
        else :
            pass

# print_dict(_dict)



print("-------------------------------------------")

def frequency_calc() :
    total = 0
    for v in _dict.values() :
        total += v

    for k in sorted(_dict) :
        frequency_dict[k] = _dict[k] / total
# print_dict(frequency_dict)



print("--------------------------------------")


sorted_frequency_desc = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
frequency_sorted_dict_desc = dict(sorted_frequency_desc)
# print(f"Sorted by value (descending): {frequency_sorted_dict_desc}")
freqenccy_key_list = frequency_sorted_dict_desc.keys()

sorted_english_letter_frequency_desc = sorted(english_letter_freq.items(), key=lambda item: item[1], reverse=True)
letter_sorted_dict_desc = dict(sorted_english_letter_frequency_desc)
# print(f"Sorted by value (descending): {letter_sorted_dict_desc}")
englis_letter_key_list = letter_sorted_dict_desc.keys()

replacement_dict = dict(zip(freqenccy_key_list, englis_letter_key_list))
for k, v in replacement_dict.items() :
    # print(f"{k} -> {v}")
    pass


decrypted_text = ''
for ch in cipher_text:
    if ch.lower() in replacement_dict:
        decrypted_text += replacement_dict[ch]
    else:
        decrypted_text += ch
print(decrypted_text)































# a -> 
# b -> t
# c ->
# d -> d !
# e ->
# f ->
# g ->
# h ->
# i ->
# j ->
# k -> n
# l ->
# m -> a
# n -> 
# o ->
# p -> h
# q ->
# r -> e
# s ->
# t ->
# u ->
# v ->
# w ->
# x ->
# y ->
# z ->


# 1at plane text
# YECAWSE THE FRACTNCE IU THE YASNC MIJEMEOTS IU BATA NS THE UICWS AOD 
# MASTERG IU SELU NS THE ESSEOCE IU MATSWYAGASHN RGW BARATE DI N SHALL 
# TRG TI ELWCNDATE THE MIJEMEOTS IU THE BATA ACCIRDNOP TI MG NOTERFRETATNIO 
# YASED IO UIRTG GEARS IU STWDG NT NS OIT AO EASG TASB TI EVFLANO EACH 
# MIJEMEOT AOD NTS SNPONUNCAOCE AOD SIME MWST REMANO WOEVFLANOED TI PNJE A 
# CIMFLETE EVFLAOATNIO IOE KIWLD HAJE TI YE XWALNUNED AOD NOSFNRED TI SWCH 
# AO EVTEOT THAT HE CIWLD REACH THE STATE IU EOLNPHTEOED MNOD CAFAYLE IU 
# RECIPONQNOP SIWODLESS SIWOD AOD SHAFELESS SHAFE N DI OIT DEEM MGSELU THE 
# UNOAL AWTHIRNTG YWT MG EVFERNEOCE KNTH BATA HAS LEUT OI DIWYT THAT THE 
# UILLIKNOP NS THE FRIFER AFFLNCATNIO AOD NOTERFRETATNIO N IUUER MG THEIRNES 
# NO THE HIFE THAT THE ESSEOCE IU IBNOAKAO BARATE KNLL REMANO NOTACT