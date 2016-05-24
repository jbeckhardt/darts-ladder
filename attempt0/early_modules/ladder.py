from random import randrange, sample

def random_insert(lst, item):
    lst.insert(randrange(len(lst)+1), item)


class Ladder():
    '''Provides asn ordered ladder for datascience dart

    It has the following attributes: 
    - order (the order of the ladder)
    
    It has the following methods:
    - get_seeds
    - get_darter_seed
    - change_darter_seed

    Note: to distinct definitions you used here:
    - ORDER - the order of players in the ladder (represented as list)
    - SEEDS - the seed number of every darter in the ladder (represented as dictionary)

    '''

    def __init__(self):
        self.order=[]
        self.seeds=self.get_seeds() 

    def get_seeds(self):
        '''gets the seeds for all darters in the Ladder
        '''     
        inverse_dictionary= dict(enumerate(self.order)) 
        seeds = dict(zip(inverse_dictionary.values(),inverse_dictionary.keys()))
        return seeds

    def get_two_darters(self):
        '''This method finds two random players 2 spaces apart to challenge each other to challenge each other. 

            It returns a JSON object with the player names and their current seeds.

            #finds a random person
            #find collect two people above and below
            #from this group of people chooses an opponent
        '''
        darter_1 = random.choice(self.order)

        # find two people above or below
        # choose 
        # manage edge cases


    def add_darter(self, darter):
        '''This method adds a darter to the ladder.

            The darter is randomly seed into the ladder. 
            It also validates that no two darters are a like
        '''
        if darter not in self.order
            self.order.insert(randrange(len(self.order)+1), darter)
        else: 
            print "this darter already exists"
        return self.order


    def remove_darter(self, darter):
        '''This method removes the darter from the board. 
            As a result everyone sees increases by 1
        '''

NewLadder = Ladder()
NewLadder.add_darter("Colin")
NewLadder.add_darter("Jon")
NewLadder.add_darter("Jason")
NewLadder.add_darter("Nikita")
NewLadder.add_darter("Tom")
print NewLadder.order


inverse_dictionary = dict(enumerate(NewLadder.order)) 
print inverse_dictionary 
seeds = dict(zip(inverse_dictionary.values(), inverse_dictionary.keys()))

print seeds
