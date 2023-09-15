alphabet = list("abcdefghijklmnopqrstuvwxyz")
def caezarize(text:str):
    try:
        a = [alphabet[alphabet.index(i.lower())-23] for i in list(text.split(" ")[0]+text.split(" ")[1])] if " " in text else [alphabet[alphabet.index(i.lower())-23] for i in list(text)]
        return "".join(a).upper()
    except ValueError:
        return "You entered a wrong value"

a = True
while a:
    user_input = input("Enter String to change to a caesar cipher (0 to terminate): ")
    if user_input == "0": break
    print(caezarize(user_input))

# from time import sleep

# def decrypt(encryption:str):
#     """This function uses brute-force to decrypt ciphertexts"""
#     for i in range(1, 26):
#         res = "".join([alphabet[alphabet.index(a.lower())-i] for a in list(encryption)])
#         print(f"Key {i}: {res}")
#         sleep(1)
#     return

# decrypt("OVDTHUFWVZZPISLRLFZHYLAOLYL")