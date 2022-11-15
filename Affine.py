'''
Created on Feb 11, 2020

@author: Hayden H
'''
alphabetUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabetLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    choice = input("1.Encrypt\n2.Decrypt\n3.Exit\n")
    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    else:
        exit()
    
def encrypt():
    a = int(input("Key a: "))
    b = int(input("Key b: "))
    plaintext = input("Plaintext: ")
    ciphertext = ""
    for c in plaintext:
        if c.isupper() == True:
            for i in range(len(alphabetUpper)):
                if c == alphabetUpper[i]:
                    ciphertext += alphabetUpper[(a*i+b) % 26]
        elif c.islower() == True:
            for i in range(len(alphabetLower)):
                if c == alphabetLower[i]:
                    ciphertext += alphabetLower[(a*i+b) % 26]
        else:
            ciphertext += c

    print(ciphertext)

def decrypt():
    a = int(input("Key a: "))
    b = int(input("Key b: "))
    ciphertext = input("Ciphertext: ")
    plaintext = ""
    for x in range(0,25):
        if (a*x) % 26 == 1:
            inverseA = x
    for c in ciphertext:
        if c.isupper() == True:
            for i in range(len(alphabetUpper)):
                if c == alphabetUpper[i]:
                    plaintext += alphabetUpper[(inverseA*(i-b)) % 26]
        elif c.islower() == True:
            for i in range(len(alphabetLower)):
                if c == alphabetLower[i]:
                    plaintext += alphabetLower[(inverseA*(i-b)) % 26]
        else:
            plaintext += c

    print(plaintext)

if __name__ == '__main__':
    main()
