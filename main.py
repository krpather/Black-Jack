from random import shuffle

'''
	Player Class:
		interacts with dealer class
'''

class Player:
	def __init__(self, balance=0, cards=[], table_bet=0, count=0):
		self.balance = balance
		self.cards = cards
		self.table_bet = table_bet
		self.count = count

	# adds funds
	def add_funds(self,amt):
		self.balance += amt

	# places bet
	def bet(self,amt):
		if amt > 50:
			self.balance-=amt
			self.table_bet+=amt
		else:
			print("Minimun bet is R50")


class Dealer:
	def __init__(self,cards=[], count=0, deck=[], players=0):
		self.cards = cards
		self.deck = deck
		self.players = 0
		self.count = count


	def shuffle(self):
		# generate deck
		'''
			rank: A = 1 or 11
				  10, J, Q, K = 10
				  2 - 9 = itself
			suit:(13) Spades, Clubs, Hearts, Diamonds
		'''
		rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		suit = ["Spades", "Clubs", "Hearts", "Diamonds"]
		for x in range(5):
			for r in rank:
				for s in suit:
					self.deck.append((r,s))

		# shuffle deck
		shuffle(self.deck)



