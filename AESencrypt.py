import math #import math module to use function such as ceiling
from BitVector import * #use BitVector class created by Avinash Kak (kak@purdue.edu) at https://engineering.purdue.edu/kak/dist/BitVector-3.4.4.html

#subbyte function takes in a hex string to puts it through the lookup table to ouput a converted hex string
def subbyte(myhexstring):
    loop2 = 0
    temp=""
    temp2=""
    part0 = ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76']
    part1 = ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0']
    part2 = ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15']
    part3 = ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75']
    part4 = ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84']
    part5 = ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf']
    part6 = ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8']
    part7 = ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2']
    part8 = ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73']
    part9 = ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db']
    part10 = ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79']
    part11 = ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08']
    part12 = ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a']
    part13 = ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e']
    part14 = ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df']
    part15 = ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']


    lookuptable=[part0,part1,part2,part3,part4,part5,part6,part7,part8,part9,part10,part11,part12,part13,part14,part15]

    #print("The string size is ", len(myhexstring), " and the loop will run", math.ceil(len(myhexstring)/2), " times." )
    for loop in range(0, math.ceil(len(myhexstring)/2) ):
        x = ""
        y = ""
        x=myhexstring[loop2]
        y=myhexstring[loop2+1]
        #convert character to integer
        if(x=='0'):
            x=0
        elif (x=='1'):
            x=1
        elif (x=='2'):
            x=2
        elif (x=='3'):
            x=3
        elif (x=='4'):
            x=4
        elif (x=='5'):
            x=5
        elif (x=='6'):
            x=6
        elif (x=='7'):
            x=7
        elif (x =='8'):
            x=8
        elif (x=='9'):
            x=9
        elif(x=='a'):
            x=10
        elif(x=='b'):
            x=11
        elif (x=='c'):
            x=12
        elif (x=='d'):
            x=13
        elif (x=='e'):
            x=14
        elif (x=='f'):
            x=15

        if(y=='0'):
            y=0
        elif (y=='1'):
            y=1
        elif (y=='2'):
            y=2
        elif (y=='3'):
            y=3
        elif (y=='4'):
            y=4
        elif (y=='5'):
            y=5
        elif (y=='6'):
            y=6
        elif (y=='7'):
            y=7
        elif (y =='8'):
            y=8
        elif (y=='9'):
            y=9
        elif(y=='a'):
            y=10
        elif(y=='b'):
            y=11
        elif (y=='c'):
            y=12
        elif (y=='d'):
            y=13
        elif (y=="e"):
            y=14
        elif (y=="f"):
            y=15
        temp=lookuptable[x][y]
        loop2=loop2+2
        temp2 = temp2 + temp
    return temp2

#mix column takes in an a 128 bit string, performs a series of matrix multiplication to output a hex string
def mixcolumn(bv3):
        bv01 = (bv3[0:8])
        bv23 = (bv3[8:16])
        bv45 = (bv3[16:24])
        bv67 = (bv3[24:32])
        bv89 = (bv3[32:40])
        bv1011 = (bv3[40:48])
        bv1213 = (bv3[48:56])
        bv1415 = (bv3[56:64])
        bv1617 = (bv3[64:72])
        bv1819 = (bv3[72:80])
        bv2021 = (bv3[80:88])
        bv2223 = (bv3[88:96])
        bv2425 = (bv3[96:104])
        bv2627 = (bv3[104:112])
        bv2829 = (bv3[112:120])
        bv3031 = (bv3[120:128])

        eightlim = BitVector(bitstring='100011011')
        one = BitVector(bitstring='0001')
        two = BitVector(bitstring='0010')
        three = BitVector(bitstring='0011')

        tempbv1 = bv01.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv23.gf_multiply_modular(three, eightlim, 8)
        newbv01 = tempbv1 ^ tempbv2 ^ bv45 ^ bv67

        tempbv2 = bv23.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv45.gf_multiply_modular(three, eightlim, 8)
        newbv23 = bv01 ^ tempbv2 ^ tempbv3 ^ bv67

        tempbv3 = bv45.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(three, eightlim, 8)
        newbv45 = bv01 ^ bv23 ^ tempbv3 ^ tempbv4

        tempbv1 = bv01.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(two, eightlim, 8)
        newbv67 = tempbv1 ^ bv23 ^ bv45 ^ tempbv4

        tempbv1 = bv89.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv1011.gf_multiply_modular(three, eightlim, 8)
        newbv89 = tempbv1 ^ tempbv2 ^ bv1213 ^ bv1415

        tempbv2 = bv1011.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv1213.gf_multiply_modular(three, eightlim, 8)
        newbv1011 = bv89 ^ tempbv2 ^ tempbv3 ^ bv1415

        tempbv3 = bv1213.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(three, eightlim, 8)
        newbv1213 = bv89 ^ bv1011 ^ tempbv3 ^ tempbv4

        tempbv1 = bv89.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(two, eightlim, 8)
        newbv1415 = tempbv1 ^ bv1011 ^ bv1213 ^ tempbv4

        tempbv1 = bv1617.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv1819.gf_multiply_modular(three, eightlim, 8)
        newbv1617 = tempbv1 ^ tempbv2 ^ bv2021 ^ bv2223

        tempbv2 = bv1819.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv2021.gf_multiply_modular(three, eightlim, 8)
        newbv1819 = bv1617 ^ tempbv2 ^ tempbv3 ^ bv2223

        tempbv3 = bv2021.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(three, eightlim, 8)
        newbv2021 = bv1617 ^ bv1819 ^ tempbv3 ^ tempbv4

        tempbv1 = bv1617.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(two, eightlim, 8)
        newbv2223 = tempbv1 ^ bv1819 ^ bv2021 ^ tempbv4

        tempbv1 = bv2425.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv2627.gf_multiply_modular(three, eightlim, 8)
        newbv2425 = tempbv1 ^ tempbv2 ^ bv2829 ^ bv3031

        tempbv2 = bv2627.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv2829.gf_multiply_modular(three, eightlim, 8)
        newbv2627 = bv2425 ^ tempbv2 ^ tempbv3 ^ bv3031

        tempbv3 = bv2829.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(three, eightlim, 8)
        newbv2829 = bv2425 ^ bv2627 ^ tempbv3 ^ tempbv4

        tempbv1 = bv2425.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(two, eightlim, 8)
        newbv3031 = tempbv1 ^ bv2627 ^ bv2829 ^ tempbv4

        newbv = newbv01 + newbv23 + newbv45 + newbv67 + newbv89 + newbv1011 + newbv1213 + newbv1415 + newbv1617 + newbv1819 + newbv2021 + newbv2223 + newbv2425 + newbv2627 + newbv2829 + newbv3031
        newbvashex = newbv.get_bitvector_in_hex()
        return newbvashex

#shiftrow takes in a hex string of the size 8 or 32, then performs a shifting operation to output the a converted hex string
def shiftrow(temp2):

    if(len(temp2)==8):
        temp3=temp2[2]+temp2[3]+temp2[4]+temp2[5]+temp2[6]+temp2[7]+temp2[0]+temp2[1]
        return temp3
    else:
        temp3=temp2[0]+temp2[1]+temp2[10]+temp2[11]+temp2[20]+temp2[21]+temp2[30]+temp2[31]+temp2[8]+temp2[9]+temp2[18]+temp2[19]+temp2[28] + temp2[29] + temp2[6] + temp2[7] + temp2[16] + temp2[17] + temp2[26] + temp2[27] + temp2[4] + temp2[5] + temp2[14] + temp2[15] + temp2[24] + temp2[25] + temp2[2] + temp2[3] + temp2[12] + temp2[13] + temp2[22] + temp2[23]
        return temp3

#xor takes in two hex strings of the same size, then peforms an xor on these operands to produce a singular hex string
def xor(temp1,temp2):
        temp1=BitVector(hexstring=temp1)
        temp2=BitVector(hexstring=temp2)
        temp3=temp1^temp2
        return temp3.get_bitvector_in_hex()

#findroundkey takes in the hex pass string of the size 32 and an integer value between 1-10 for the round number. After operations are performed, a hex pass string of the size 32 is generated
def findroundkey(temp1, case):
    w0=temp1[0:8]
    w1=temp1[8:16]
    w2=temp1[16:24]
    w3=temp1[24:32]
    temp2=temp1[24:32]
    temp2=shiftrow(temp2)
    temp2=subbyte(temp2)
    if(case==1):
        temp2=xor(temp2,'01000000')
    elif(case==2):
        temp2 = xor(temp2, '02000000')
    elif (case == 3):
        temp2 = xor(temp2, '04000000')
    elif (case == 4):
        temp2 = xor(temp2, '08000000')
    elif (case == 5):
        temp2 = xor(temp2, '10000000')
    elif (case == 6):
        temp2 = xor(temp2, '20000000')
    elif (case == 7):
        temp2 = xor(temp2, '40000000')
    elif (case == 8):
        temp2 = xor(temp2, '80000000')
    elif (case == 9):
        temp2 = xor(temp2, '1b000000')
    elif (case == 10):
        temp2 = xor(temp2, '36000000')
    w4=xor(w0, temp2)
    w5=xor(w1, w4)
    w6=xor(w2, w5)
    w7=xor(w3, w6)
    temp3=w4+w5+w6+w7
    return temp3

def setPassPhrase (PassPhrase):
    if(len(PassPhrase)<16):#check if less than 16 characters, if so add one space character until 16 chars
        while(len(PassPhrase)!=16):
            PassPhrase=PassPhrase+"\00"
    if(len(PassPhrase)>16):#check if bigger than 16 characters, if so then truncate it to be only 16 chars from [0:16]
        print("Your passphrase was larger than 16, truncating passphrase.")
        PassPhrase=PassPhrase[0:16]
    return PassPhrase   

def EncryptFile (passphrase, filein, fileout):  

    #open plaintext.txt file to read and encrypt
    file=open(filein, "r")
    message=(file.read())
    # print("Plaintext message is:\n%s\n" % message)
    file.close()

    message=BitVector(textstring=message)
    message=message.get_bitvector_in_hex()
    replacementptr=0
    while(replacementptr<len(message)):
        if(message[replacementptr:replacementptr+2]=='0a'):
            message=message[0:replacementptr]+'0d'+message[replacementptr:len(message)]
            replacementptr=replacementptr+4
        else:
            replacementptr=replacementptr+2

    message=BitVector(hexstring=message)
    message=message.get_bitvector_in_ascii()
    #set up some parameters
    start=0#set starting pointer for the part to encrypt of the plaintext
    end=0#set ending pointer for the part to encrypt of the plaintex
    length=len(message)#check the entire size of the message
    loopmsg=0.00#create a decimal value
    loopmsg=math.ceil(length/16)+1#use formula to figure how long the message is and how many 16 character segmentss must be encrypted
    outputhex=""#setup output message in hex

    #need to setup roundkeys here
    passphrase=BitVector(textstring=passphrase)

    roundkey1=findroundkey(passphrase.get_bitvector_in_hex(),1)
    roundkey2=findroundkey(roundkey1,2)
    roundkey3=findroundkey(roundkey2,3)
    roundkey4=findroundkey(roundkey3,4)
    roundkey5=findroundkey(roundkey4,5)
    roundkey6=findroundkey(roundkey5,6)
    roundkey7=findroundkey(roundkey6,7)
    roundkey8=findroundkey(roundkey7,8)
    roundkey9=findroundkey(roundkey8,9)
    roundkey10=findroundkey(roundkey9,10)
    roundkeys=[roundkey1,roundkey2,roundkey3,roundkey4,roundkey5,roundkey6,roundkey7,roundkey8,roundkey9,roundkey10]

    #set up FILEOUT to write
    FILEOUT = open(fileout, 'w')

    # set up the segement message loop parameters
    for y in range(1, loopmsg): # loop to encrypt all segments of the message
        if(end+16<length): #if the end pointer is less than the size of the message, then set the segment to be 16 characters
            plaintextseg = message[start:end + 16]
        else: #or else if the end pointer is equal to or greator than the size of the message
            plaintextseg = message[start:length]
            for z in range(0,((end+16)-length),1): #run a while loop to pad the message segement to become 16 characters, if it is 16 already the loop will not run
                plaintextseg = plaintextseg+"\00"
                #plaintextseg2=BitVector(textstring=plaintextseg)
                #print(plaintextseg2.get_bitvector_in_hex())

        #add round key zero/ find round key one
        bv1 = BitVector(textstring=plaintextseg)
        bv2 = passphrase
        resultbv=bv1^bv2
        myhexstring = resultbv.get_bitvector_in_hex()

        for x in range(1, 10):  # loop through 9 rounds
            # sub byte
            myhexstring = resultbv.get_bitvector_in_hex()
            temp1=subbyte(myhexstring)

            # shift rows
            temp2=shiftrow(temp1)

            # mix column
            bv3 = BitVector(hexstring=temp2)
            newbvashex=mixcolumn(bv3)
            newbv=BitVector(hexstring=newbvashex)

            #add roundkey for current round
            bv1 = BitVector(bitlist=newbv)
            bv2 = BitVector(hexstring=roundkeys[x-1])
            resultbv = bv1 ^ bv2
            myhexresult = resultbv.get_bitvector_in_hex()

        #start round 10
        # sub byte round 10
        myhexstring = resultbv.get_bitvector_in_hex()
        temp1=subbyte(myhexstring)

        # shift rows round 10
        temp2=shiftrow(temp1)

        # add round key round 10
        newbv = BitVector(hexstring=temp2)
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkeys[9])
        resultbv = bv1 ^ bv2
        myhexstring = resultbv.get_bitvector_in_hex()

        #set encrypted hex segement of message to output string
        outputhextemp = resultbv.get_hex_string_from_bitvector()
        FILEOUT.write(outputhextemp)
        start = start + 16 #increment start pointer
        end = end + 16 #increment end pointer

    # encrypted output hex string to specified cipherhex file
    FILEOUT.close()

##    file2=open(fileout, "r")
##    print("The encrypted message is:\n%s\n" % file2.read())
##    file2.close()

def main():
    if len(sys.argv) !=4:#takes in three arguments for the plaintext.txt, ciphertext file names and "passphrase"
        sys.exit("Error, EncryptFile takes three arguments for the inputfile, outputfile names and passphrase")
    EncryptFile (setPassPhrase(sys.argv[3]), sys.argv[1], sys.argv[2])

if __name__ == "__main__": main()
