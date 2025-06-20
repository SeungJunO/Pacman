key = 'abcdefghijklmnopqrstuvwxyz'

def emncrypt(n,paintext):
    result=''

    for l in plaintext.lower():
        try:
            i=(key.index(l)+n)%26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()
