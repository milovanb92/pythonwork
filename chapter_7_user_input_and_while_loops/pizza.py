prompt = "\nPlese enter topping you want on pizza: "
prompt += "\n(When you are done type 'quit'. "

#topping = ""

#while topping != 'quit':
#    topping = input(prompt)
#    if topping != 'quit':
#        print(topping)
 
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(topping)