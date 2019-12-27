players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[0:3])
print(players[1:4])

# print all players from beggining of the list to index before specified (3)
print(players[:4])

# print all players from index 3 to the end of the list
print(players[3:])

# print last three playes from the end
print(players[-3:])

print("Here are the first three playes on my team:")
for player in players[:3]:
    print(player.title())
