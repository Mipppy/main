import base64




def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

encode_decode = input("\n\nWould you like to encrypt or decrypt\n")

if encode_decode == "encrypt":
    key = input("\nEnter the key\n")
    message = input("\n\nEnter the message to encrypt\n")
    print(Encode(key, message))
if encode_decode == "decrypt":
    key = input("\nEnter the key\n")
    message = input("\n\nEnter the message to decrypt\n")
    print(Decode(key, message))