logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

def encode(message):
    shift_encode=int(input("Enter the shift amount: "))%26;
    encoded_message=""

    for letter in list(message):

        if(not(letter.isalpha())):
             encoded_message+=letter

        elif(letter.isupper()and (ord(letter)+shift_encode)<=ord("Z")):
             encoded_message+=chr((ord(letter)+shift_encode))
        
        elif(letter.isupper()):
             encoded_message+=chr((ord(letter)+shift_encode)-26)
        
        elif(letter.islower() and ord(letter)+shift_encode)<=ord("z"):
             encoded_message+=chr((ord(letter)+shift_encode))
        
        elif(letter.islower()):
             encoded_message+=chr((ord(letter)+shift_encode)-26)
        else:
            print("Invalid Character!")
        
    print("Encoded Message: "+encoded_message)



def decode(message_to_decode):
    shift_decode=int(input("Enter the shift amount "))%26;
    decoded_message=""

    for letter in list(message_to_decode):
        
        if(not(letter.isalpha())):
             decoded_message+=letter
        
        elif(letter.isupper() and (ord(letter)-shift_decode)>=ord("A")):
            decoded_message+=chr((ord(letter)-shift_decode))

        elif(letter.isupper()):
            decoded_message+=chr((ord(letter)-shift_decode)+26)

        elif(letter.islower() and (ord(letter)-shift_decode)>=(ord("a"))):
            decoded_message+=chr((ord(letter)-shift_decode))

        elif(letter.islower()):
            decoded_message+=chr((ord(letter)-shift_decode)+26)

        else:
            print("Invalid Character!")
            
    print(f"Decoded Message: {decoded_message}")


run=True
while(run):
    choice=input("Type \'encode\' for encrypt, \'decode\' for decrypt:\n ").lower()
    if(choice=='encode'):
        message_to_encode=input("Enter message to encode: ")
        encode(message_to_encode)
    elif(choice=='decode'):
        message_to_decode=input("Enter message to decode: ")
        decode(message_to_decode)
    else:
        print("Invalid Choice!")
    
    try_again_counter=True
    while(try_again_counter):
        try_again=input("Run Again? Type yes or no:\n ").lower()

        if(try_again=='yes'):
            run=True
            try_again_counter=False
        elif(try_again=='no'):
            print("Thank You! Exiting...")
            run=False
            try_again_counter=False
        else:
            print("Invalid Input!")
            try_again_counter=True