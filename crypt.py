#! /usr/bin/env python3
##################################################################################################
##The program takes four command line arguments: a single flag (-e or -d) indicating whether the 
##program will encrypt or decrypt a message, the name of the public or private key file to use 
##(generated by keygen.py), the name of the file to encrypt or decrypt, and the name of the output 
##file.
##
## For example, the following command will encrypt the file secret.txt using Alice’s public key 
## file alice.pub to produce the cipher text file secret.cip:
## ./crypt.py -e alice.pub secret.txt secret.cip
## Then the following command would decrypt the file secret.cip:
## ./crypt.py -d alice.prv secret.cip secret.txt
##################################################################################################
import sys
import genkeys
import AESdecrypt
import AESencrypt

from random import randrange
from Crypto.Util.number import long_to_bytes, bytes_to_long

def generaterandomkey():
    # print("Begin generate random key")
    rndint = randrange(int(0x0FFFFFFFFFFFFFFF), int (0xFFFFFFFFFFFFFFFF))
    # return random integer string
    # print (str(rndint)[:16])
    return (str(rndint)[:16])

def main():
    print ("CRYPT MAIN")
    inputstring = sys.argv
    print("Input", inputstring)
    if (len(sys.argv)) !=5:
        print ("This program takes four command line arguments: a single flag (-e or -d), the name of the public or private key file to use, the name of the file to encrypt or decrypt, and the name of the output file.")
        raise ValueError("Not enough arguments")
        
    if sys.argv[1] == "-e":
        encrypt = True
    else:
        encrypt = False
    keyfilename=sys.argv[2].strip()
    if encrypt:
        decryptfilename="NA"
        encryptfilename=sys.argv[3].strip()
    else:
        encryptfilename="NA"
        decryptfilename=sys.argv[3].strip()
    outputfile=sys.argv[4]
    # print("Arguments ENCRYPT =",encrypt,keyfilename, decryptfilename,encryptfilename,outputfile)

    # read RSA key
    print ("Open key file",keyfilename)
    f = open(keyfilename,'rb')
    rkey=genkeys.RsaKey(p=0,q=0,n=0,d=0,e=65537)
    rkey.readkey(f)    
    f.close()
    # print ("Key=", rkey)
    
    aeskeyfile = ".aeskey"   

    if encrypt:
        # generate the aes passphrase
        passphrase = generaterandomkey()
        print ("Random AES Key", passphrase)

        #store the passphrase in a file    
        f=open(aeskeyfile+".txt","w")
        f.write(passphrase)
        f.close()

        # write the encrypted data to a file
        f=open(aeskeyfile+".cip","wb")
        encryptedkey = rkey.encrypt(int(passphrase))
        f.write(long_to_bytes(encryptedkey))
        f.close()

        # read the encrypted key from the file
        f=open(aeskeyfile+".cip","rb")        
        print("AES Key Encrypted\n", bytes_to_long(f.read()),"stored in",aeskeyfile+".cip") 
        f.close()
        
        AESencrypt.EncryptFile (AESencrypt.setPassPhrase(passphrase), encryptfilename, outputfile)

        #append the encrypted paasphrase to the encrypted file
        f=open(outputfile,"ab")
        f.write(long_to_bytes(encryptedkey))
        f.close()

        f=open(outputfile, "rb")
        print("ENCRYPTED: Message + AES Key\n", bytes_to_long(f.read()),"Stored in",outputfile) 
        f.close()

    else:

        # verify the passphrase equals the phrase in the saved file
        f=open(aeskeyfile+".txt","r")
        testpassphrase=f.read()
        f.close()
        # print("Read in passphrase",testpassphrase)

        # read K' from the encrypted file (last 128 bytes)
        f=open(decryptfilename,"rb")
        databytes = f.read()
        f.close()

        encryptedkey = bytes_to_long(databytes[-128:])
        try:
            decrypted = rkey.decrypt(encryptedkey)
            if str(decrypted) == testpassphrase:
                print ("DECRYPTED RSA Key", str(decrypted),"MATCHES", testpassphrase )
                passphrase=str(decrypted)
            else:
                passphrase=testpassphrase
        except ValueError:
            print ("DECRYPTION FAILED: ValueError")
            passphrase=testpassphrase

        ciphertext = databytes[:-128]
        # remove the key from the file to decrypt the remainder
        f=open(decryptfilename,"wb")
        f.write(ciphertext)
        f.close()
        
        AESdecrypt.DecryptFile (AESdecrypt.setPassPhrase(passphrase), decryptfilename, outputfile)
        f=open(outputfile, "r")
        print("The decrypted message is.\n", f.read(),"\nStored in",outputfile) 
        f.close()

        # save the key to the file for later
        f=open(decryptfilename,"ab")
        f.write((long_to_bytes(encryptedkey)))
        f.close()
   
if __name__ == "__main__":
    main()
