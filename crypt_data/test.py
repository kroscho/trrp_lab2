from crypt import encrypt, decrypt, encrypt_key, decrypt_key
from config_crypt import config_ctypt

def main():
    conf = config_ctypt()
    password = conf['crypt']['password']   
    
    text = {"kros": 'krosss'}
    # First let us encrypt secret message
    encrypted = encrypt(text, password)
    print(encrypted)
    
    #crypto, privkey = encrypt_key(password)
    #print(type(crypto), type(privkey))
    #passw = decrypt_key(crypto, privkey)
    #print(passw)

    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, password)
    print(bytes.decode(decrypted))

main()