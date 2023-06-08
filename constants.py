OPPONENT__TWITTER_HANDLE_DICT = {'ohioState' : 'OhioStateFB','pennState' : 'PennStateFball', 'georgia':'GeorgiaFootball', 'alabama':'AlabamaFTBL',
                  'LSU':'LSUfootball', 'tennessee':'Vol_Football', 'Texas': 'TexasFootball', 'Oklahoma': 'OU_Football' }
#url pattern: https://twitter.com/TWITTER_HANDLE

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


