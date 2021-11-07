import rsa
import json
from des import DesKey

class Crypt_data:

    def __init__(self, data):
        """Constructor"""
        self.data = data

    def encrypt_key_rsa(self):
        """Шифрование ключа ассиметричным шифрованием rsa"""
        (pubkey, privkey) = rsa.newkeys(512)
        #message = self.data.encode('utf8')
        message = self.data
        crypto_key = rsa.encrypt(message, pubkey) # Зашифровка
        return crypto_key, privkey

    def decrypt_key_rsa(self, crypto, privkey):
        """Расшифрование ключа ассиметричным шифрованием rsa"""
        key = rsa.decrypt(crypto, privkey) # Расшифровка
        print(key.decode('utf8'))
        return key.decode('utf8')

    def encrypt_data_des(self, key):
        """шифрование данных при помощи ключа симметричного шифрования (DES)"""
        key0 = DesKey(str.encode(key))
        data = json.dumps(self.data).encode('utf-8')
        #data = self.data.encode('utf8')
        crypto = key0.encrypt(data, padding=True)
        return crypto, key0

    def decrypt_data_des(self, crypto, key):
        """Расшифрока данных при помощи ключа ассиметричного шифрования (DES)"""
        decrypto = key.decrypt(crypto, padding=True) 
        decrypto = json.loads(decrypto.decode('utf-8'))
        print(decrypto)
        return decrypto
    
    