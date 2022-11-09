key = 'abcdefghijklmnopqrstuvwxyz'

# 평문을 받아서 암호화하고 암호문을 반환
def encrypt(n, plaintext):
    result = ''
    for i in plaintext.lower():
        try:
            a = (key.index(i) + n) % 26
            # z같은건 +n을 해주면 26을 초과하기 때문에 % 26을 써준다.
            result += key[a]
        except ValueError:
            result += i
    return result.lower()

# 암호문을 받아서 복호화하고 평문을 반환
def decrypt(n, ciphertext):
    result = ''
    for i in ciphertext:
        try:
            a = (key.index(i) - n) % 26
            result += key[a]
        except ValueError:
            result += i
    return result

n = 3
text = 'The language of truth is simple. xyz'
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)
print('평문 : ', text)
print('암호문 : ', encrypted)
print('복호문 : ', decrypted)
