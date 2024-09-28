'''
card game between two computer players
suit: symbols on card clubs-diamonds-hearts-spades
value: Ace-2-..10-joker-queen-king
deck:52 unique cards
player:holds random cards
'''
import random
suitsTuple=("Clubs","Diamonds","Hearts","Spades") #suits definition tuple
valuesTuple=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Joker","Queen","King","Ace") #value definition tuple
cardScore={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Joker":11,"Queen":12,"King":13,"Ace":14} #real value of cards dictionary
isGameRunning=True
#global variables
class Card: #class to define cards
    def __init__(self,suit,value): #initialize cards with suit and values both are expected to be string
        self.suit=suit #cards suit -diamonds hearts etc.
        self.value=value #cards shown values
        self.inGameScore=cardScore[value] #get cards game score
        
    def __str__(self): # built in function to use with print
        return self.value + " of " + self.suit 
    
class Deck(): #classto define deck
    def __init__(self):
        self.allCards=[] #empty card deck
        for val in valuesTuple: #to generate cards
            for su in suitsTuple: #to generate cards
                self.allCards.append(Card(su, val)) #assign cards to card deck
                
    def shuffleCards(self): #to shuffle orderly deck
        random.shuffle(self.allCards) #call shuffle function from random library
        
    def giveCard(self):#to give away a card from deck
        return self.allCards.pop()
    
class player: #player class
    def __init__(self,name):
        self.name =name
        self.playerHand= [] #players cards in hand
    def __str__(self): #to print player 
            return f'Player {self.name} has {len(self.playerHand)} cards'
    def removeCard(self): #remove a card from player
            return self.playerHand.pop(0)
        
    def addCardtoHand(self,newCards): #to add cards 
        if type(newCards)==type([]):
                self.playerHand.extend(newCards) #multiple cards
        else:
                self.playerHand.append(newCards) #single card

#game setup
playerOne=player("One") #create players
playerTwo=player("Two") #create players
startDeck=Deck() #starting deck
startDeck.shuffleCards() #shuffle deck

for x in range(26): #give 26 cards to each player
    playerOne.addCardtoHand(startDeck.giveCard()) #26 card for player one
    playerTwo.addCardtoHand(startDeck.giveCard()) #26 card for player two
    
playedRounds=0 #rounds counter
while isGameRunning: #game start loop
    playedRounds+=1
    print(f"This is Round {playedRounds}")
    
    if len(playerOne.playerHand) == 0: #victory check
        print(f"Player {playerOne.name} is out of Cards")
        isGameRunning = False
        break
    if len(playerTwo.playerHand) == 0: #victory check
        print(f"Player {playerTwo.name} is out of Cards")
        isGameRunning = False
        break

    playerOnePlayedCard=[] 
    playerOnePlayedCard.append(playerOne.removeCard()) #take a card from player one
    
    playerTwoPlayedCard=[]
    playerTwoPlayedCard.append(playerTwo.removeCard()) #take a card from player two
    
    comparing=True
    while comparing:
        if playerOnePlayedCard[-1].inGameScore > playerTwoPlayedCard[-1].inGameScore: #player 1 wins
            playerOne.addCardtoHand(playerOnePlayedCard) #winner takes both cards
            playerOne.addCardtoHand(playerTwoPlayedCard) 
            comparing=False
        elif playerOnePlayedCard[-1].inGameScore < playerTwoPlayedCard[-1].inGameScore: #player 2 wins
            playerTwo.addCardtoHand(playerOnePlayedCard) #winner takes cards
            playerTwo.addCardtoHand(playerTwoPlayedCard)
            comparing=False
        else:
            print("This is a WAR!") #if ingame card scores is equal we enter war state
            if len(playerOne.playerHand) < 5: #if player one has less than 5 cards he loses
                print("Player One cant declare war and loses")
                isGameRunning=False
                break
            elif len(playerTwo.playerHand) < 5: #player two like above
                print("Player Two cant declare war and loses")
                isGameRunning=False
                break
            else: #if they have cards they put it on table
                for num in range(5):
                    playerOnePlayedCard.append(playerOne.removeCard())
                    playerTwoPlayedCard.append(playerTwo.removeCard())
        
        
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    