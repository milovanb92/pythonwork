guests = ['kico', 'sreco', 'stupar']
print(f"{guests[0]} would you like to come to dinner?")
print(f"{guests[1]} would you like to come to dinner?")
print(f"{guests[2]} would you like to come to dinner?")
print(f"\n{guests[2]} wont make to come to dinner, I need to invite someone else")

del guests[2]
guests.insert(2, 'daco')

print(f"\n{guests[2]} would you like to come to dinner?")

print("\n I found bigger table for diner, now I will invite more people.")
guests.insert(3, 'sasa')
guests.insert(4, 'marko')
guests.append('nemanja')

print(f"\n{guests[0]} would you like to come to dinner?")
print(f"{guests[1]} would you like to come to dinner?")
print(f"{guests[2]} would you like to come to dinner?")
print(f"{guests[3]} would you like to come to dinner?")
print(f"{guests[4]} would you like to come to dinner?")
print(f"{guests[5]} would you like to come to dinner?")

print("\n Sorry I can invite only 2 people...")
guests.pop()
guests.pop()
guests.pop()
guests.pop()

print(f"\n{guests[0]} would you like to come to dinner?")
print(f"{guests[1]} would you like to come to dinner?")

del guests[1]
del guests[0]

print(guests)
