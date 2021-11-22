#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from crypt import encrypt, decrypt, encrypt_key, decrypt_key
from config_crypt import config_ctypt
import json

def main():
    conf = config_ctypt()
    password = conf['crypt']['password']   
    
    text = {"kros": 'крос'}
    
    # First let us encrypt secret message
    encrypted = encrypt(text, password)
    #encrypted = {"cipher_text": "O0DrgpipZDyLMPMH2k1ZZ/IOa3mooa//3r+X3r+x25gZlteRep02uQtTGTFJLG6J0+qXkiEVt2X2jmhVyz1RRID6JNyMV5MKwHdQ7tHEHMswVfjNhd4asO9ZJlAtspqfQKg/x9ZN39yT7gR6FdiD6iLFoDefq9OAS2nRogcX/jKr1OBmArrxShh58H3YiSRZLPdjg6mkzALVJ+p6j24mGONAAHpLeUmIvpRK9knn+2ZfX0rl4OMU2YC/S97QbsUF8ulFa1c6h0NIyaPCcJzuqZsLpl0bdRrhuIgAraZ1F1gn6gS+VylZGJw6nylydbYuw3hrUt5sSYpc6VpXAV0fPukZb6U114NDH/G/FZ9KfHNd4zTXOcHhfIyeIibC90Q/ShyWmKIUGfI+VlvvD783+hPcLVLZZ75sF16dR4+GDfiYxUe+hoYcqU3tfX2Ax07F3Mquf5VCkaXqeB0JI415ktfY/yvvqXuHENwAdEe9nhjfmMmYPM7m5Fnh/aSpDrcMzhByJo17TFrV8z3zNTQV9uH2PwRf9QkHZ5PbQHjRznRlacZ0rhN6pI9BpqAPAUqgQPqu+n9eNVCzmzMpxftEp1/HMx3BqHBj2dRWvfUVPKaLX0hZ/SUg7cA1MXPCiQ==", "salt": "ukUSQYwm0ptHMhCwnq+VOA==", "nonce": "JE1AuThvx9s++vPagnoIRQ==", "tag": "5C/YD24myYj6NpmY950cMQ=="}
    #encrypted = encrypted
    print(encrypted)
    
    #crypto, privkey = encrypt_key(password)
    #print(type(crypto), type(privkey))
    #passw = decrypt_key(crypto, privkey)
    #print(passw)

    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, password)
    print(json.loads(decrypted.decode('utf-8')))

main()