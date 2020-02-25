#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# POSSIBILITY 2 WITH FLAG "active"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#  POSSIBILITY 1

#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)
