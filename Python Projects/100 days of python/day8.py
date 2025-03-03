print("Ceaser Cypher, Day 8!")

def encode(message):
    message_list=list(message)
    shift_encode=int(input("Enter the shift amount: "))%26;
    encoded_message=""
    for letter in message_list:
        if(letter.isupper()and (ord(letter)+shift_encode)<=ord("Z")):
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
    decode_message_list=list(message_to_decode)
    decoded_message=""
    for letter in decode_message_list:
        if(letter.isupper() and (ord(letter)-shift_decode)>=ord("A")):
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