bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # print whole list with a square brackets

print(bicycles[0])  # print list item 
print(bicycles[0].title()) # format list item
print(bicycles[-1])  # with -1 you access last item in the list
print(bicycles[-2])  # access second from the end item in the list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

