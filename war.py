#welcome today we will code a simple war cards game
#this will be two player computer card game
#WAR

#variables here
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#value is dictonary of strings which will return a integer for us to compare 
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


#class of single card
class card:
	"""we will input a suit(shape) and a rank(number)"""
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
		self.value=values[rank]								#we will need value to compare as we cannot compare string with integers

	def __str__(self):										#__str__ is used to give thia class a print statment if anyone tries printing it
		return self.rank + 'of' +self.suit


#class of whole deck
class deck:
	"""we will input nothing in it 
		there will be three methods create deck,shuffle deck,deal one"""
	def __init__(self):
		self.all_cards=[]         #to hold the full deck

		#we iterate through for loop to create unique 52 cards using a list of all suits and ranks in general card system
		for suit in suits:
			for rank in ranks:
				self.all_cards.append(card(suit,rank))

	def shuffle(self):
		random.shuffle(self.all_cards)


	# we use this deal one method while distributing cards to players one by one
	def deal_one(self):
		return self.all_cards.pop()


#class to hold player attributes
class player:
	"""we will input a name of player 
		we  also will make methods for player to bring a card on table, to get a card from table """
	def __init__(self,name):
		self.name=name
		self.player_all_cards=[]  #this will be the cards a player has in his hand
	
	#this method will get the top most card from players hand and bring it on table
	def bring_on_table(self):
		return self.player_all_cards.pop(0)

	#this method will get all cards on table to the player 
	def get_from_table(self,new_cards):
		#if it is not a single card its a list of cards won by a player
		if type(new_cards)==type([]):
			self.player_all_cards.extend(new_cards)
		else:
			self.player_all_cards.append(new_cards)

	def __str__(self):
		return f'player {self.name} has {len(self.player_all_cards)} cards'



#GAME SETUP

#creating two players
player_one=player('one')
player_two=player('two')

#creating deck and shuffling it
new_deck=deck()
new_deck.shuffle()

#distributing 26 cards to each player i.e half half cards
for x in range(26):
	player_one.get_from_table(new_deck.deal_one())
	player_two.get_from_table(new_deck.deal_one())


#game logiic
round=0
game_on=True
while game_on:
	round+=1
	print(f'round{round}')

	#check if any player is lost
	if len(player_one.player_all_cards)==0:
		print("player 1 out of cards.")
		print("player two wins the game.")
		game_on=False
		break
	
	if len(player_two.player_all_cards)==0:
		print("player 2 out of cards.")
		print("player one wins the game.")
		game_on=False
		break

	#no one losses bring both players cards on table

	player_one_cards_on_table=[]
	player_one_cards_on_table.append(player_one.bring_on_table())

	player_two_cards_on_table=[]
	player_two_cards_on_table.append(player_two.bring_on_table())


	#now lets keep at_war true and if its not in war we will break out
	at_war=True

	while at_war:
		#i have player_one_cards_on_table[-1] here -1 reppresents the last card of a player if we have more than one card on table it will still compare the first card and the while loop wont stop

		#if p1 card is greater than p2 card
		if player_one_cards_on_table[-1].value>player_two_cards_on_table[-1].value:
			player_one.get_from_table(player_one_cards_on_table)
			player_one.get_from_table(player_two_cards_on_table)
			at_war=False

		#if p2 card is greater than p1 card
		elif player_two_cards_on_table[-1].value>player_one_cards_on_table[-1].value:
			player_two.get_from_table(player_one_cards_on_table)
			player_two.get_from_table(player_two_cards_on_table)
			at_war=False

		#if both have same value we get declare war
		else:
			print("war")

			if len(player_one.player_all_cards)<5:
				print("p1 has less cards ,unable to get into war")
				print("p2 wins")
				game_on=False
				break

			elif len(player_two.player_all_cards)<5:
				print("p2 has less cards ,unable to get into war")
				print("p1 wins")
				game_on=False
				break

			else:
				for num in range(5):
					player_one_cards_on_table.append(player_one.bring_on_table())
					player_two_cards_on_table.append(player_two.bring_on_table())
					


















