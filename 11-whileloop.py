#!/usr/bin/env python3
# Day 11

# While loop
# With use of two built-in functions 
# len() to get the total number of items in a list 
# count() to count the occurrences of an element in a list

players = ['Horvath','Osho','Lockyer','Bell','Drameh','Mpanzu','Nakamba','Doughty','Campbell','Morris','Adebayo']
eleven = len(players)

print ("Here we use an object type of:")
print (type(players))
print ()

print ()
print ("Luton " + str(eleven) + " team to face Watford")
index = 0
while index < len(players):
    print(players[index])
    index = index + 1

print ()
print ("C'mon you Hatters!!!!")
print ()

# A count of occurrences in the players list
marvelous = players.count('Nakamba')
print ("There's only " + str(marvelous) + " Marvelous " + (players[6]) + "!!! :)")

