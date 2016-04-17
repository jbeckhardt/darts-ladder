class Completed_Match():
    '''' This screates a dart thrower 

    Attributes  (*asterisks mean not yet includeed)
    - players
    - winner 
    - loser
    - location*
    - game scores*
    - score*
    '''

    def __init__(self, winner, loser):
            self.winner = winner
            self.loser = loser
            self.outcome = {winner:1, loser:0}
