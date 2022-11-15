
alphabetUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabetLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    while True:
        choice = input("1.Encryption\n2.Decryption\n3.BruteForce\n4.Quit\n")
        if choice == "1":
            plaintext = input("Input plaintext: ")
            k = int(input("Enter key (1-25): "))
            print(encrypt(plaintext, k))
        elif choice == "2":
            ciphertext = input("Input ciphertext: ")
            k = int(input("Enter key (1-25): "))
            print(decrypt(ciphertext, k))
        elif choice == "3":
            ciphertext = input("Input ciphertext: ")
            print()
            bruteforce(ciphertext)
            print()
        elif choice == "4":
            exit()
        else:
            print("Invalid option")
    
def encrypt(plaintext, k):
    ciphertext = ""
    for c in plaintext:
        if c.isupper() == True:
            for i in range(len(alphabetUpper)):
                if c == alphabetUpper[i]:
                    ciphertext += alphabetUpper[(i+k) % 26]
        elif c.islower() == True:
            for i in range(len(alphabetLower)):
                if c == alphabetLower[i]:
                    ciphertext += alphabetLower[(i+k) % 26]
        else:
            ciphertext += c

    return ciphertext
    
def decrypt(ciphertext, k):
    plaintext = ""
    for c in ciphertext:
        if c.isupper() == True:
            for i in range(len(alphabetUpper)):
                if c == alphabetUpper[i]:
                    plaintext += alphabetUpper[(i-k) % 26]
        elif c.islower() == True:
            for i in range(len(alphabetLower)):
                if c == alphabetLower[i]:
                    plaintext += alphabetLower[(i-k) % 26]
        else:
            plaintext += c

    return plaintext

def bruteforce(ciphertext):
    for k in range(1, 26):
        plaintext = ""
        for c in ciphertext:
            if c.isupper() == True:
                for i in range(len(alphabetUpper)):
                    if c == alphabetUpper[i]:
                        plaintext += alphabetUpper[(i-k) % 26]
            elif c.islower() == True:
                for i in range(len(alphabetLower)):
                    if c == alphabetLower[i]:
                        plaintext += alphabetLower[(i-k) % 26]
            else:
                plaintext += c
        print(str(k) + ". " + plaintext)

if __name__ == '__main__':
    main()