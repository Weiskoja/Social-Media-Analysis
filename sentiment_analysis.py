#https://www.nltk.org/api/nltk.sentiment.vader.html

def scoreVADER(tweets):
    # function should be mapped to each tweet in passed dataframe
    # input should be pandas dataframe with [tweet text] column and blank VADER score column
    # 




    #   take in tweets dataframe object
    #   iterate through each tweet and get normalized sentiment value. 
    #   create 2 new columns, sentiment_score & sentiment_magnitude
    #   score is normalized numberical representation of tweet -1 to 1,  
    #   magnitude is bucketed score (likert scale). 
    # strong neg      neg       neutral       pos         strong pos
    # (-1,-0.9)    [0.9,0.05) [-0.05,0.05]  (0.05,0.9]     (0.9,1)
    return None

#analyze function should add vader score column to input data frame
#psuedocode: tweetsDataFrame['Vaderscore'] = tweetsDataFrame.map(scoreVader)

#needs to be called by analyze functions. 

