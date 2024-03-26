import random
import math

def generate_random_superincreasing_sequence(n):
    sequence = [ ]
    sequence.append(random.randint(1,10))
    i =  len(sequence)
    for i in range(n):
        additionalElement = sum(sequence)+random.randint(1,10)
        sequence.append(additionalElement) 
    return sequence

def generate_q(superIncreasing_sequence):
    q = sum(superIncreasing_sequence) + random.randint(1,10)
    return q

def generate_r(qValue):
    r = random.randint(1,10)
    while(math.gcd(r, qValue) != 1):
        r = random.randint(1,10)
    return r

def generate_private_key(superIncreasing_sequence, qValue, rValue):
    privateKey = []
    for i in superIncreasing_sequence:
        privateKey.append(i)
    privateKey.append(qValue)
    privateKey.append(rValue)
    return privateKey

def generate_public_key(superIncreasing_sequence,qValue,rValue):
    publicKey = []
    for i in superIncreasing_sequence:
        publicKey.append((rValue*i)%qValue)
    return publicKey

def knapsack_encryption(textToEncrypt, publicKey):
    encryptedMessage = 0
    for i in range(len(textToEncrypt)):
        if textToEncrypt[i]=='1':
            encryptedMessage += publicKey[i]
    return encryptedMessage

def knapsack_decryption(encryptedMessage, privateKey, qValue, rValue):
    r_inversed = pow(rValue, -1, qValue)
    c_prime = (encryptedMessage * r_inversed) % qValue
    X = []
    remaining_c = c_prime
    wElements = []
    wElements = privateKey[:-2]
    while(remaining_c>0):
        highestValue = max(wElements)
        if(highestValue>remaining_c):
            wElements.remove(highestValue)
        else:
            remaining_c -= highestValue
            X.append(wElements.index(highestValue))
            wElements.remove(highestValue)
    decryptedMessage = 0
    for i in X:
        decryptedMessage += pow(2,8-i)
    return decryptedMessage

def decimal_to_binary(decryptedMessage):
    binaryMessage = ""
    if decryptedMessage == 0:
        return "0"
    while decryptedMessage > 0:
        binaryMessage = str(decryptedMessage % 2) + binaryMessage
        decryptedMessage //= 2
    return binaryMessage


superIncreasing_sequence = generate_random_superincreasing_sequence(9)
print("Superincreasing sequence", superIncreasing_sequence)       
q = generate_q(superIncreasing_sequence)
print("q", q)    
r = generate_r(q)
print("r",r)
privateKey = generate_private_key(superIncreasing_sequence,q,r)
print("Private key", privateKey)
publicKey =  generate_public_key(superIncreasing_sequence,q,r)
print("Public key", publicKey)
originalMessage = '111101110'
print("Original Message", originalMessage)
encryptedMessage = knapsack_encryption(originalMessage, publicKey)
print("Encrypted Message", encryptedMessage)
decryptedMessage = knapsack_decryption(encryptedMessage, privateKey,q,r)
binaryMessage = decimal_to_binary(decryptedMessage)
print("Decrypted Message", binaryMessage)
