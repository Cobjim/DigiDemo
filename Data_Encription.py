#Base code taken from https://www.folkstalk.com/2022/10/how-to-make-an-encryption-program-in-python-with-code-examples.html
#Modified by Ian Coberly
#pip install pycrypto
#pip install base32hex  
#Encryptor
import random
text = input ( "Enter text: " )
entxt = ""
private_key =[]
detxt = ""
for i in text:
    rand = random.randint ( 1, 125 )
    en = rand + ord ( i )
    en = chr ( en )
    en = str ( en )
    private_key = private_key +[rand] 
    entxt = entxt + en
print ( "\nPublic key:", entxt )
print ( "Private key:", private_key )
#Desencryptor
for i in entxt:
    j = entxt.rfind(i)              #finds the position of the letter of the encryptor
    de = ord( i ) - private_key[j]  # subtracts the Private keys value to the Public Key received
    #print (de)
    de = chr( de )
    de = str( de )
    detxt = detxt + de              # Constructs the result
print("Desencypted Text: ", detxt)
