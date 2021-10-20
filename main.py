
import pyautogui as pag
import os, os.path
import time as t
import cv2
from Functions import *
from numpy import random
 
#screen dimensions
xscreen = 1920
yscreen = 1080
 

cred =0
rval = 3
clickRate = 6
num_seconds = 1
mainloop = True
goalmet = False

#Infastructure paths
infapath = "Infastructure"
logins_doc = os.path.join(infapath,"Logins.xlsx")
artist_doc = os.path.join(infapath,"Artists.xlsx")
my_artist_doc = os.path.join(infapath,"my_artists.xlsx")

#initializing login 
logins = pd.read_excel(logins_doc)
emails = logins["email"]
passwords = logins["password"]


#initialize artists
artist_doc = pd.read_excel(artist_doc)
artists = artist_doc["artists"]

#import my artists
my_artist_doc = pd.read_excel(my_artist_doc)
my_artists = my_artist_doc["artists "]


def checkTime():
    t1 =t.clock()
    print("its been ",(t1-t0)/minute)
       
def checkPlays():
     if(plays >= int(clicks)):
         goalmet = True
         print(plays, "_plays")

# requirments set the character of the sequence
# req says i need plays amount of nodes between 0 and 5 (my songs)
# req2 says i need x amount of nodes valued 5           (humanizing actions)
# req3 says i need x amount of nodes between 5 and 10   (random songs)
# req4 says i need x amount of nodes between 10 and 15  (themed songs)

def perform(seq):
        if(seq ==1):
            #play my song
            playacrossairSong()
        elif(seq ==2):
            #play my artist
            playacrossairArtist()
            
        elif(seq ==3):
            #play my album
           playacrossairAlbum()
            
        elif(seq ==4):
            #play my liked
            playLiked()
            
        elif(seq ==5):
            # perform humanizing bahaviour ----- BIG ONE
            Humanizer()
            
        elif(seq ==6):
             #play random song
             playRandomSong()
             
        elif(seq ==7):
            #play random artist
             playRandomArtist()
             
        elif(seq ==8):
            #play random album
            playRandomAlbum()  
        elif(seq ==9):
            #play random playlist
             playRandomPlaylist()  
        elif(seq ==10):
            #play themed song
            print("themed")    
        elif(seq ==11):
            #play themed artist
             print("theme artist")   
        elif(seq ==12):
            #play themed album
             print("tavbum" )  
        elif(seq ==13):
            #play themed playlist
            print("playlist")
        else:
            return 0
                




    
listenTime  = 5   
test = 20
plays =0
minute = 60
hour = 3600
nodes = 100
goalmet = False
clicks =10



t0 = t.clock()
while(mainloop == True):
    
    clicks = 100
    goalmet = False
    sequence = generateSeq(138,clicks,7,30,0)
    for i in range(nodes):
        perform(sequence[i])
        t.sleep(random.randint(40,80))
       


       






