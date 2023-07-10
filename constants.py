class DIRECTORY:
    """A class to store all the twitter handles and IDs for important accounts"""
    def __init__(self, schoolList):
        for school in schoolList:
            setattr(self, school.name, {'handle': school.handle, 'id': school.id})

    def __repr__(self) -> str:
        return str(self.__dict__)
    
class SCHOOL:
    def __init__(self, name, handle, id):
        self.name = name
        self.handle = handle
        self.id = id



OPPONENT__TWITTER_HANDLE_DICT = {'ohioState' : 'OhioStateFB','pennState' : 'PennStateFball', 'georgia':'GeorgiaFootball', 'alabama':'AlabamaFTBL',
                  'LSU':'LSUfootball', 'tennessee':'Vol_Football', 'Texas': 'TexasFootball', 'Oklahoma': 'OU_Football' }
#url pattern: https://twitter.com/TWITTER_HANDLE

OPPONENT_INFORMATION_LIST = [('ohioState', 'OhioStateFB', 723239605823107072), ('pennState', 'PennStateFball', 53103297), ('georgia', 'GeorgiaFootball', 321586997), 
 ('alabama', 'AlabamaFTBL', 350508156), ('LSU', 'LSUfootball', 137396575), ('tennessee', 'Vol_Football', 181180906), ('Texas', 'TexasFootball', 34286487), 
 ('Oklahoma', 'OU_Football', 407208905)]

OPPONENT_OBJECT_LIST  = [SCHOOL(name = school[0], handle = school[1], id = school[2]) for school in OPPONENT_INFORMATION_LIST]


      

IMPORTANT_LOCATIONS = {'nyc': (	40.730610,-73.935242),'la': (34.052235, -118.243683), 'chicago':(41.881832, -87.623177), 'dc': (38.89511, -77.03637), 'MI':()}
#{cityName: (lat,long)}, Center of city for latitude and longitude to make circle for tweet geolocation.
#MI radius needs to cover all of michigan, at least Lower Peninsula, maybe not UP if difficult

TROLL_USERNAME_ELEMENTS = []
#filter out any tweets with these in username or handle

SPAM_CONTENT_ELEMENTS = []
#fitler out any replies that are in this list.
#list includes links to shops or other types of ads, unrelated posts, etc.

DATABASE_PATH = ""
#path to database, make flexible. Search for database name? os.path stuff


OPPONENT_DIRECTORY = DIRECTORY(OPPONENT_OBJECT_LIST)
