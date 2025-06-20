key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n,plaintext):
    result = ' '

    for l in plaintext.lower():
        try:
            i = (key.index(l) +n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n,ciphertext):
    result = ' '

    for l in ciphertext:
        try:
            i = (key.index(l) -n) % 26
            result += key[i]

        except ValueError:
            result += l

    return result

n = 3
text = 'The language of truth is simple'
encrypted = encrypt(n,text)
decrypted = decrypt(n,encrypted)
print(text)
print(encrypted)
print(decrypted)


        
            
