# As I am participating in the Junior Competition, the following challenge is the 
# only one that this program tackles:
# 
# Process through given voter data and count and display valid votes* on a GUI*Valid vote: voter has
# only voted once and for a single candidateParty names: 
#'Socks and Crocs Reform League', 'Pineapple Pizza Party', 'Pronounced JiffUnion'

# Import necessary packages
import pandas as pd
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

# Read the excel data and tranfer the data to a 2-dimensional arra y
votesData = pd.read_excel("MEC Competition Voting Data.xls").to_numpy()

# Initialize the unique name array and the vote count values
uniqueNames = []
pppVoteCount = 0
pjuVoteCount = 0
scrlVoteCount = 0

# Iterate through the numpy array containing the excel data
for dataEntry in votesData:
    
    # Assign suitable variables for each data entry/vote
    fullName = dataEntry[0] + " " + dataEntry[1]
    vote = dataEntry[2]
    
    # Check if the name is found in a a seperate list of unique names (is a duplicate)
    if not(fullName in uniqueNames):
        # Add the new name to the list of unique names
        uniqueNames.append(fullName)
        # Check if the vote is done just for one party
        if (vote.find(",") == -1):

            # Increment vote count once the vote has been validated
            if (vote == "Pineapple Pizza Party"):
                pppVoteCount += 1
            elif (vote == "Pronounced Jiff Union"):
                pjuVoteCount += 1
            else:
                scrlVoteCount += 1

    # With this verification system, if a name has initially made a valid vote to one party
    # and then has made another vote to multiple parties, 
    # THE SYSTEM COUNTS THE FIRST, VALID VOTE AND IGNORES THE SECOND, INVALID VOTE.

# Function to display the parties and their respective votes
def showScores():
    pppLabel = Label(root, text="Pineapple Pizza Party Vote Count: " +str(pppVoteCount), font=("Helvetica", 20), bd=1, relief="sunken")
    pppLabel.pack(pady=20, padx=20)

    pjuLabel = Label(root, text="Pronounced Jiff Union Count: " +str(pjuVoteCount), font=("Helvetica", 20), bd=1, relief="sunken")
    pjuLabel.pack(pady=20, padx=20)

    scrlLabel = Label(root, text="Socks and Crocs Reform League Vote Count: " +str(scrlVoteCount), font=("Helvetica", 20), bd=1, relief="sunken")
    scrlLabel.pack(pady=20, padx=20)

# Function to display a visual representation of the data in the form of a pie-chart 
def graph():
    sliceValues = [pppVoteCount, pjuVoteCount, scrlVoteCount]
    partyLabels = ['Pineapple Pizza Party', 'Pronounced Jiff Union', 'Socks and Crocs Reform League']
    plt.pie(sliceValues, labels=partyLabels, shadow=True, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    plt.title("Votes for each party as a % of the total votes")
    plt.show()


# Create main window for GUI
root = Tk()
root.title("Voting Results")

showScores()
showGraphButtton = Button(root, text="Show Graph", command=graph)
showGraphButtton.pack()

root.mainloop()
            

    

