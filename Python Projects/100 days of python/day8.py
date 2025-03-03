print("Ceaser Cypher, Day 8!")

#A=65, Z=90, a=97, z=122

def encode(message):
    message_list=list(message)
    shift_encode=int(input("Enter the shift amount: "))
    encoded_message=""
    for letter in message_list:
        if(letter.isupper()):
            if((ord(letter)+shift_encode)<=ord("Z") and (ord(letter)+shift_encode)>=ord("A")):
                encoded_message+=chr((ord(letter)+shift_encode))
            else:
                encoded_message+=chr((ord(letter)+shift_encode)-(24+shift_encode))
        elif(letter.islower()):
            if((ord(letter)+shift_encode)<=ord("z") and (ord(letter)+shift_encode)>=ord("a")):
                encoded_message+=chr((ord(letter)+shift_encode))
            else:
                encoded_message+=chr((ord(letter)+shift_encode)-(24+shift_encode))
        else:
            print("Invalid Character!")
        
    print("Encoded Message: "+encoded_message)



def decode(message_to_decode):
    shift_decode=int(input("Enter the shift amount "))
    decode_message_list=list(message_to_decode)
    decoded_message=""
    for letter in decode_message_list:
        if(letter.isupper()):
            if((ord(letter))<=ord("Z") and (ord(letter))>=(ord("A")+shift_decode)):
                decoded_message+=chr((ord(letter)-shift_decode))
            else:
                decoded_message+=chr((ord(letter)-shift_decode)+26)
        elif(letter.islower()):
            if((ord(letter)<=ord("z")) and (ord(letter)>=(ord("a")+shift_decode))):
                decoded_message+=chr((ord(letter)-shift_decode))
            else:
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