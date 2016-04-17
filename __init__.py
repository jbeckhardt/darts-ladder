
from ladder import Ladder
from match import Match
from darter import Darter



New_Ladder = Ladder


New_Match = Match(('Jon','Colin'))
print New_Match.players




# class Ladder():
#     '''Provides asn ordered ladder for datascience dart

#     It has the following attributes: 
#     - order (the order of the ladder)
    
#     It has the following methods:
#     - get_seeds
#     - get_darter_seed
#     - change_darter_seed'''

#     def __init__(self, order):
#         self.order=order

#     def get_seeds(self):
#         '''gets the seeds for all darter in the Ladder'''

#     def get_two_players(self):
#         """This method finds two random plaers within 3 spaces of each other to challenge each other. 

#             It returns a JSON object with the player names and their current seeds.

#             #find a random person
#             #find collect two people above or below"""


# class Match():
#     '''' This screates a dart thrower 

#     Attributes  (*asterisks mean not yet includeed)
#     - players
#     - winner 
#     - loser
#     - location*
#     - game scores*
#     - score*
#     '''

#     def __init__(self, players):
#             self.players = players   
#             self.winner = None
#             self.loser = None


# class Darter():
#     '''' This creates a dart thrower 

#     Attributes follow
#     - name
#     - games_played
#     - games_won
#     - games_lost
#     - games_tied
#     - wlr
#     '''

#     def __init__(self, name):
#             self.name = name
#             matches_played = 0  
#             matches_lost = 0 
#             matches_won = 0