#! /usr/bin/env python3
# This file handles querying of data by patients or auditors.

import sys
import genkeys
import AESdecrypt
import AESencrypt

from random import randrange
from Crypto.Util.number import long_to_bytes, bytes_to_long


def decryptLog (logfile, keyfile):
    # locally decrypts the encrypted audit log file `audit_log.csv.enc` and stores the temporary results in a temporary file `temp_dec.csv` which is used for calculating the queried data results, and is deleted by the os once the operation is finished.
    print ("Open Public key file",keyfile)
    f = open(keyfile,'rb')
    rkey=genkeys.RsaKey(p=0,q=0,n=0,d=0,e=65537)
    rkey.readkey(f)    
    f.close()
    f=open(logfile,"rb")
    databytes = f.read()
    f.close()
    passphrase = "1112223334445550"
    outputfile = "auditlog.txt"
    encryptedkey = bytes_to_long(databytes[-128:])
    try:
        decrypted = rkey.decrypt(encryptedkey)
        if str(decrypted) == passphrase:
            print ("DECRYPTED RSA Key", str(decrypted),"MATCHES", passphrase )
            passphrase=str(decrypted)
    except ValueError:
        print ("DECRYPTION FAILED: ValueError")

    ciphertext = databytes[:-128]
    # remove the key from the file to decrypt the remainder
    f=open(logfile,"wb")
    f.write(ciphertext)
    f.close()
        
    AESdecrypt.DecryptFile (AESdecrypt.setPassPhrase(passphrase), logfile, outputfile)
    f=open(outputfile, "r")
    print("The decrypted message is.\n", f.read(),"\nStored in",outputfile) 
    f.close()
    return

def encryptLog (logfile,keyfile):
    # locally decrypts the encrypted audit log file `audit_log.csv.enc` and stores the temporary results in a temporary file `temp_dec.csv` which is used for calculating the queried data results, and is deleted by the os once the operation is finished.
    print ("Open Public key file",keyfile)
    f = open(keyfile,'rb')
    rkey=genkeys.RsaKey(p=0,q=0,n=0,d=0,e=65537)
    rkey.readkey(f)    
    f.close()
    # write the encrypted RSA Key to a file
    passphrase = "1112223334445550"
    encryptedkey = rkey.encrypt(int(passphrase))
    outputfile = "auditlog.enc"
    AESencrypt.EncryptFile (AESencrypt.setPassPhrase(passphrase), logfile, outputfile)
    #append the encrypted paasphrase to the encrypted file
    f=open(outputfile,"ab")
    f.write(long_to_bytes(encryptedkey))
    f.close()
##    f=open(outputfile, "rb")
    print("ENCRYPTED: Message + AES Key stored in",outputfile) 
##    f.close()    
    return

def queryLog (logfile, auditor=False):
    f=open(logfile,r)
    f.close()
    return
  
def updateLog (logfile, auditor=False):
    f=open(logfile,'w')
    f.close()
    return

def createLog (logfile):
    f=open(logfile,'w')
    f.close()
    return

if __name__ == "__main__":
    print ("MAIN")
    auditlog = "auditlog.csv"
    publickey="zak.pub"
    privatekey="zak.prv"
    f = open(auditlog, 'r')
    print("The audit log contains.\n", f.read(),"records in",auditlog)
    encryptLog(auditlog, publickey)
    auditlog="auditlog.enc"
    decryptLog(auditlog, privatekey)
    f.close()
