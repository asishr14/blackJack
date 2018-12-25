
# coding: utf-8

# In[9]:


class Deck(object):
    #Object Deck Attributes
    def _init_ (self):
        #52 Cards
        self.fullDeck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4
        self.cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]*4
        
        #define bilt-in methods to be used
        def _len_ (self):
            return len (self.cards)
        
        #take a card out of the deck
        def takeCards (self):
            import random
            c = self.cards.pop(self.cards.index(random.choice(self.cards)))
            return c
        
        #reset deck
        def resetDeck(self):
            self.cards = self.fullDeck
            
class Player(object):
        def _init_(self, accBal = 1000, wins = 0, losses = 0, draws = 0, busts = 0, bets = 0, hand = []):
                self.accBal = accBal
                self.wins = wins
                self.losses = losses
                self.draws = draws
                self.busts = busts
                self.bets = bets
                
                #playsers hand at any given hand
                self.hand = hand
                
        #method to add or remove account money
        def changeBal(self, amt):
            self.accBal += amt

        #update count for wins etc
        def updateCount(self, typ):
            if typ == "Win":
                self.wins += 1

            elif typ == "Loss":
                self.losses += 1

            elif typ == "draw":
                self.draws += 1
            else:
                self.busts += 1


            #Print status
            def PrintStatus(self):
                Print (""" Account Balance ${}
                No. of Wins: {}
                No. of Losses: {}
                No. of draws: {}
                No. of busts: {}
                """. format(self.accBal, self.wins, self.losses, self.draws, self.busts))

                #Update playesrs hand when dealt a card
                def updateHand(self, card):
                    self.hand.append(card)

                def clearHand(self):
                    self.hand = []

                def showHand(self):
                    print(self.hand)

                #betting
                def betAmount(self, amt):
                    self.bet = amt


class GameStatus(object):
    def _init_(self, endGame=False, roundStatus=None):
        self.endGame = endgame
        self.roundStatus = roundStatus

    def CheckGameStatus(self, player): #player is object
    #check acctBal if won or amt is 0 to continue the game
        if player.accBal >= 3000:
            print("Congrats, you won the Game.")
            self.endGame = True
        elif player.accBal <= 0:
            print("Sorry, your dont have enough amt to continue")
            self.endGame = True
        else:
            self.endGame = False

    def updateRoundStatus(self,p): #p is the player.hand
    #have we won the tound to be replaced by AI logic
    #currently we have a dummy which says if we have over 17 we win

        A = p.count("A"); two = p.count("2"); three = p.count("3"); four = p.count("4"); five = p.count("5"); six = p.count("6");
        seven = p.count("7"); eight = p.count("8"); nine = p.count("9"); ten = p.count("10"); J = p.count("J"); Q = p.count("Q");
        K = p.count("K");

        total = two*2 + three*3 + four*4 + five*5 + six*6 + seven*7 + eight*8 + nine*9 + ten*10 + J*10 + Q*10 + K*10

        #Account ace being 1 or 11
        if(21>= total + A*1 > 16) or (21>= total + A*11 > 16):
            self.rondStatus = "Win"
        elif total == 16:
            self.roundStatus = "Draw"
        else:
            self.roundStatus = "Loss"


    def initalise():
        deck = Deck()
        player = Player()
        game = GameStatus()
        player.printStatus()

        return deck, player, game


    def checkYN(inp):
        while True:
            if inp.lower in ["y", "n", "Yes", "No"]:
                if inp.lower["y", "Yes"]:
                    return "y"
                    break
                else:
                    return "n"
                    break
            else:
                Print("Please enter y or n or Yes or No")
                inp = input()

    def checkBet(player):
        while True:
            inp = input()
            try:
                if inp.isdigit and 0<int(inp)<= player.accBal:
                    player.betAmount(int(inp))
                    break
                else:
                    print("Please enter a number whithin the acctBal")
            except:
                print("Please enter a number whithin the acctBal")

    def hitOrStand():
        while True:
            inp = input()
            if inp.lower in ["hit","stand"]:
                if inp.lower == "hit":
                    return "hit"
                    break
                else:
                    return "stand"
                    break
            else:
                print("Please enter hit or stand")
                continue

    def checkForBust(p):
        #input will be an array
        A = p.count("A"); two = p.count("2"); three = p.count("3"); four = p.count("4"); five = p.count("5"); six = p.count("6");
        seven = p.count("7"); eight = p.count("8"); nine = p.count("9"); ten = p.count("10"); J = p.count("J"); Q = p.count("Q");
        K = p.count("K");

        if (A*1 + two*2 + three*3 + four*4 + five*5 + six*6 + seven*7 + eight*8 + nine*9 + ten*10 + J*10 + Q*10 + K*10)>21:
            return True
        else:
            return False

    def checkHandOk(player):
        #check to see if the hand is ok as in not bust or over 5cards
        if len(player.hand) == 5:
            return "limit reached"
        elif checkForBust(player.hand):
            return "Bust"
        elif len(player.hand)==5 and checkForBust(player.hand):
            return "bust limit"
        else:
            return "ok"

    def updateWinLoss(status, player):
        if status == "win":
            #update tally count
            player.updateCount("win")
            print("Player has won this round")

            #update AccBal
            player.changeBal(player.bet*2)

        elif status == "draw":
            player.updateCount("draw")
            print("This game is draw")

            player.changeBal(player.bet)

        else:
            player.updateCount("loss")
            print ("Player lost this round")

    def aRound(deck, player, game):
        import time
        while True:
            #this is where blackJack round happens check hand in hand
            if checkHandOk(player) =="ok":
                print("Would you like to hit or stand")
                output = hitOrStand()

                if output == "hit":
                    print("Dealing you a card..")
                    #get card from Deck
                    card = deck.takeCard()
                    #put in players hand
                    player.updateHand(card)
                    player.showHand()

                else:
                    #player stand check for win cond
                    print("checking you hand")
                    game.updateRoundStatus(player.hand)
                    updateWinLoss(game.roundStatus, player)

                    break
            elif checkHandOk(player) =="Bust":
                    print("Bust...Updating your profile")
                    game.updateRoundStatus(player.hand)
                    updateWinLoss(game.roundStatus, player)
                    print.updateCount("bust")

                    break
            elif checkHandOk(player) =="limit reached":       
                    print("Limit of 5 is reached...checking status")
                    game.updateRoundStatus(player.hand)
                    updateWinLoss(game.roundStatus, player)

                    break

            elif checkHandOk(player) =="bust_limit":
                    print("Bust & Limit of 5...Updating your profile")
                    game.updateRoundStatus(player.hand)
                    updateWinLoss(game.roundStatus, player)
                    print.updateCount("bust")

                    break

            else:
                break

def gameSession(output, deck, player, game):
    import time
    while True:
        #betting
        print("How much you wnt to bet on this round?")
        checkBet(player)
        #takebet from Balance
        player.changeBal(-player.bet)

        #inital dealing on the first card
        card = deck.takeCard()
        #put in playes hand
        player.updateHand(card)
        player.showHand()

        aRound(deck, player,game)
        #wait 3sec before clearing the ground

        time.sleep(3)
        clear_output()
        player.printStatus()

        #reset hand & deck
        player.clearHand()
        deck.resetDeck()

        #check game Status
        game.checkGameStatus(player)

        if game.endGame == False:
            #need to end game
            print("Would you like to play another round? Y/N")
            output = checkYN(input())
            if output == "Y":
                continue
            else: 
                break
        else:
            break

                        
        
                
        
            


# In[14]:


from IPython.display import clear_output
print("welcome to BlackJack  To win reach $3k")

deck, player, game = initialise()

print("would you like to start now Y/N?")

output = checkYN(input())
clear_output()
if output == "y":
    print("Dealing you the first card")
    gameSession(output,deck,player,game)
    
print("Game Exiting")

