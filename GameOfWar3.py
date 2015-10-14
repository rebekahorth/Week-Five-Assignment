#Rebekah Orth- with help from Dr. Neumann and collaboration from Marisa Gross, Alicia Williams, Evan Sauers
#CIS 125
#Week 5- Game of War 1


#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.

This is the shell copy. Fill this out to get it to work

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter > 1000:
			print("Game is a draw")
			break
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	print("Player A has " + str(len(PlayerAHand)) + " cards, Player B has " + str(len(PlayerBHand)) + " cards")
	
def playRound(PlayerA, PlayerB):
	
	Acard= PlayerA.pop()
	Bcard= PlayerB.pop()
	
	rankA= getRank(Acard)
	rankB= getRank(Bcard)
	
	if rankA > rankB:
		#a wins
		PlayerA.insert(0,Acard)
		PlayerA.insert(0,Bcard)
	elif rankB > rankA:
		#b wins
		PlayerB.insert(0,Bcard)
		PlayerB.insert(0,Acard)
	else:
		PlayerA.append(Acard)
		PlayerB.append(Bcard)
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
	
	
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	print("War")
	Astack = []
	Bstack = []

	if len(PlayerA) > 5 and len(PlayerB) > 5:
	
# pull 4 cards off
		for x in range(5):
			Astack.append(PlayerA.pop())
			Bstack.append(PlayerB.pop())

	
		if getRank(Astack[4]) > getRank(Bstack[4]):
			#a wins
			PlayerA = Astack + Bstack + PlayerA
		elif getRank(Bstack[4]) > getRank(Astack[4]):
			#b wins
			PlayerB = Bstack + Astack + PlayerB
		else:
			pass
		# if tie toss all 10 cards

	return PlayerA, PlayerB



	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

