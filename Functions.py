
import pyautogui as pag
import os, os.path
import time as t
import cv2
import pandas as pd
from numpy import random

#screen dimensions
xscreen = 1920
yscreen = 1080
 

cred =0
rval = 0
clickRate = 6
num_seconds = 1
mainloop = True
goalmet = False
#image paths
#spotify paths 
path = "Reference_images\Spotify"
playButton = os.path.join(path,"play_button.png")
desktop_icon = os.path.join(path,"desktop_icon.png")
login_but = os.path.join(path,"login_cred_button.png")
username_bar = os.path.join(path,"mail_icon.png")
password_bar = os.path.join(path,"password_bar.png")
search_button = os.path.join(path,"search_button.png")
search_bar = os.path.join(path,"search_bar.png")
artist_label = os.path.join(path,"artist_label.png")
playlist_label = os.path.join(path,"playlist_label.png")
follow_button = os.path.join(path,"follow_button.png")
start_SB = os.path.join(path,"start_searchB.png")
selected_SB = os.path.join(path,"selected_searchB.png")
search_bar = os.path.join(path,"search_bar.png")
artist_playB = os.path.join(path,"artist_play.png")
clear_search_bar = os.path.join(path,"clear_search_bar.png")
account_but = os.path.join(path,"account_button.png")
profile_but = os.path.join(path,"profile_button.png")
pic_but = os.path.join(path,"profile_pic.png")
play_button = os.path.join(path,"A_play_button.png")
skip_button = os.path.join(path,"next_button.png")
x_icon = os.path.join(path,"close_button.png")
home_button = os.path.join(path,"home_button.png")
song_label = os.path.join(path,"songs_label.png")
album_label = os.path.join(path,"album_label.png")
playlist_label = os.path.join(path,"playlist_label.png")
liked_label = os.path.join(path,"liked_label.png")
devices_button = os.path.join(path,"devices_button.png")
library_button = os.path.join(path,"library_button.png")
selected_library_button = os.path.join(path,"selected_library_button.png")
que_button = os.path.join(path,"que_button.png")
back_button = os.path.join(path,"back_button.png")
selected_home_button = os.path.join(path,"selected_home_button.png")


#Infastructure paths
infapath = "Infastructure"
logins_doc = os.path.join(infapath,"Logins.xlsx")
artist_doc = os.path.join(infapath,"Artists.xlsx")
my_artist_doc = os.path.join(infapath,"my_artists.xlsx")
my_songs_doc = os.path.join(infapath,"My_songs.xlsx")
random_songsexe = os.path.join(infapath,"random_songs.xlsx")
random_albumsexe = os.path.join(infapath,"random_albums.xlsx")
random_playlistsexe = os.path.join(infapath,"random_playlists.xlsx")

#initialize my artist details
songs = pd.read_excel(my_songs_doc)
MySongsArtists = songs["artist"]
MySongsName = songs["song"]
MyAlbums = songs["album"]


#initializing login 
logins = pd.read_excel(logins_doc)
emails = logins["email"]
passwords = logins["password"]

#initialize random songs excel
random_songs= pd.read_excel(random_songsexe)
random_Songs_artist = random_songs["artist"]
random_Songs_song = random_songs["song"]

#initialize random albums
random_albums = pd.read_excel(random_albumsexe)
random_Albums = random_albums["album"]

#initialize random playlist
random_playlists = pd.read_excel(random_playlistsexe)
random_Playlist = random_playlists["playlists"]

#initialize artists
artist_doc = pd.read_excel(artist_doc)
artists = artist_doc["artists"]

#import my artists
my_artist_doc = pd.read_excel(my_artist_doc)
my_artists = my_artist_doc["artists "]

#setup, this include opening the app loggin in and following some people




#/////////////////////////////////restart below ///////////////////////////////////

def openSpotify():
    iconCenter = pag.center(pag.locateOnScreen(desktop_icon,confidence = 0.9))
    pag.moveTo(iconCenter[0],iconCenter[1])
    pag.click(clicks=2)
    t.sleep(2)
    
def closeSpotify():
    xCenter = pag.center(pag.locateOnScreen(x_icon,confidence = 0.9))
    pag.moveTo(xCenter[0],xCenter[1])
    pag.click(clicks=1)
    t.sleep(2)
    
#/////////////////////////////////restart above ///////////////////////////////////







#login sequence 
def login(username,password):
    #entering username
    usernameCenter = pag.center(pag.locateOnScreen(username_bar,confidence = 0.9))
    pag.moveTo(usernameCenter[0],usernameCenter[1])
    pag.moveRel(-50,0)
    pag.click(clicks=1)
    pag.press('backspace',presses = 40)
    pag.write(username)
    #entering password
    pwordCenter = pag.center(pag.locateOnScreen(password_bar,confidence=0.8))
    pag.moveTo(pwordCenter[0],pwordCenter[1])
    pag.click(clicks=1)
    pag.write(password)      
    #clicking login
    loginCenter = pag.center(pag.locateOnScreen(login_but))
    pag.moveTo(loginCenter[0],loginCenter[1])
    pag.click(clicks=1)
    t.sleep(3)

def setprofilepic():
    #not working
    accountCenter = pag.center(pag.locateOnScreen(account_but, 0.7))
    pag.moveTo(accountCenter[0],accountCenter[1],0.5,pag.easeInElastic)
    pag.click(clicks=1)
    
    profileCenter = pag.center(pag.locateOnScreen(profile_but, 0.8))
    pag.moveTo(profileCenter[0],profileCenter[1],0.5,pag.easeInElastic)
    pag.click(clicks=1)


    picCenter = pag.center(pag.locateOnScreen(pic_but, 0.8))
    pag.moveTo(picCenter[0],picCenter[1],0.5,pag.easeInElastic)
    pag.click(clicks=1)

    
def clearSearchBar(artist):
    if (pag.locateOnScreen(clear_search_bar, confidence=0.9)!= None):
        clearButCenter = pag.center(pag.locateOnScreen(clear_search_bar, confidence=0.7))
        pag.moveTo(clearButCenter[0],clearButCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks=1)
        print("cleared test")
        pag.click(clicks =1)
        t.sleep(1)
        pag.write(artist)
        print(artist," Written in")
        t.sleep(2)
        return 1
    else:
        print("no text to remove found")
        return 0
    
def search(artist):
    if(clearSearchBar(artist)==1):
        return 1
    #click search button
    if(pag.locateOnScreen(search_button,0.75) != None):
        searchbuttonCenter = pag.center(pag.locateOnScreen(search_button,0.8))
        pag.moveTo(searchbuttonCenter[0],searchbuttonCenter[1],0.5, pag.easeInElastic)
        print("found search button")
        pag.click(clicks =1)
        t.sleep(1)
        pag.write(artist)
        print(artist," Written in")
        t.sleep(2)
        return 1
    elif(pag.locateOnScreen(start_SB,0.9) !=None):
        startupsbCenter = pag.center(pag.locateOnScreen(start_SB,0.9))
        pag.moveTo(startupsbCenter[0],startupsbCenter[1],0.5,pag.easeInElastic)
        print("found startup search button")
        pag.click(clicks =1)
        t.sleep(1)
        pag.write(artist)
        print(artist," Written in")
        t.sleep(2)
        return 1
    elif(pag.locateOnScreen(selected_SB,0.8) !=None):
        selectedsbCenter = pag.center(pag.locateOnScreen(selected_SB,0.7))
        pag.moveTo(selectedsbCenter[0],selectedsbCenter[1],0.5,pag.easeInElastic)
        print("found selected search button")
        pag.click(clicks =1)
        t.sleep(1)
        pag.write(artist)
        print(artist," Written in")
        t.sleep(2)
        return 1

    else:
        print("failed to find search button")
        return 0
        #searchbarCenter = pag.center(pag.locateOnScreen(search_bar,0.7))
        #pag.moveTo(searchbarCenter[0],searchbarCenter[1])



def followArtist():
    print("looking to follow")
    clickArtist()
    if (pag.locateOnScreen(follow_button,confidence=0.8)!=None):
        fbCenter = pag.center(pag.locateOnScreen(follow_button,confidence=0.8))
        pag.moveTo(fbCenter[0],fbCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        t.sleep(1)
        print("followed")
    else:
        print("already following")
        
def clickPlay():
    if (pag.locateOnScreen(play_button,confidence=0.8)!=None):
        PBCenter = pag.center(pag.locateOnScreen(play_button,confidence=0.8))
        pag.moveTo(PBCenter[0],PBCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        t.sleep(1)
        print("play clicked")
        return 1
    else:
        print("was already playing")

        
        
def calculateClickRate(clicks,time):
    clickRate  = int(clicks)/int(time)
    print("youll being doing about ",clickRate ," clicks per hour")

def skip():
    if (pag.locateOnScreen(skip_button,confidence=0.8)!=None):
        skipCenter = pag.center(pag.locateOnScreen(skip_button,confidence=0.8))
        pag.moveTo(skipCenter[0],skipCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        t.sleep(1)
        print("skipped")
        return 1
    else:
        print("could locate skip button")
        return 0


def restart():
    closeSpotify()
    t.sleep(4)
    openSpotify()
    t.sleep(4)
    

def clickHome():
    if (pag.locateOnScreen(home_button,confidence=0.8)!=None):
        hmCenter = pag.center(pag.locateOnScreen(home_button,confidence=0.8))
        pag.moveTo(hmCenter[0],hmCenter[1],0.5)
        pag.click(clicks =1)
        print("Home button clicked")

    elif(pag.locateOnScreen(selected_home_button,confidence=0.8)!=None):
        ShmCenter = pag.center(pag.locateOnScreen(selected_home_button,confidence=0.8))
        pag.moveTo(ShmCenter[0],ShmCenter[1],0.5)
        pag.click(clicks =1)
        print("slected Home button clicked")
        
    else:
        print("could not locate home button, restarting...")
        restart()


def cycle(skips,x,y):
    for i in range(skips):
            listenTime = random.randint(x,y)
            print("listen time->",listenTime)
            t.sleep(listenTime)
            if (skip() == 1):
                return 1

def adjustVolume():
      if (pag.locateOnScreen(devices_button,confidence=0.9)!=None):
        DevCenter = pag.center(pag.locateOnScreen(devices_button,confidence=0.8))
        pag.moveTo(DevCenter[0],DevCenter[1],0.5,)
        rval = random.randint(50,150)
        pag.moveRel(rval,0)
        pag.click(clicks =1)
        pag.moveRel(-100,-200)
        print("volume adjusted to " + str(rval-50))
      else:
        print("could not locate devices button, ")
      

def checkDevices():
    if (pag.locateOnScreen(devices_button,confidence=0.9)!=None):
        DevCenter = pag.center(pag.locateOnScreen(devices_button,confidence=0.8))
        pag.moveTo(DevCenter[0],DevCenter[1],0.5,)
        pag.click(clicks =1)
        pag.moveRel(-100,-200)
        print("Devices clicked")
    else:
        print("could not locate devices button, ")
      


def clickLibrary():
    if (pag.locateOnScreen(library_button,confidence=0.9)!=None):
        libCenter = pag.center(pag.locateOnScreen(library_button,confidence=0.8))
        pag.moveTo(libCenter[0],libCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        print("library clicked")

    elif(pag.locateOnScreen(selected_library_button,confidence=0.9)!=None):
        SlibCenter = pag.center(pag.locateOnScreen(selected_library_button,confidence=0.8))
        pag.moveTo(SlibCenter[0],SlibCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        print("selected library clicked")


    else:
        print("could not locate library button ")
      


def clickQue():
     if (pag.locateOnScreen(que_button,confidence=0.9)!=None):
        QCenter = pag.center(pag.locateOnScreen(que_button,confidence=0.8))
        pag.moveTo(QCenter[0],QCenter[1],0.5)
        pag.click(clicks =1)
        pag.moveRel(-100,-200)
        print("que clicked")
     else:
        print("could not locate que button, ")
      


        
def clickBack():
    if (pag.locateOnScreen(back_button,confidence=0.9)!=None):
        BCenter = pag.center(pag.locateOnScreen(back_button,confidence=0.8))
        pag.moveTo(BCenter[0],BCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        print("backed clicked")
    else:
        print("could not locate back button, ")
      


def action(action):

    if(action == 1):
        adjustVolume()
        return 1
    elif(action == 2):
        #devices
        checkDevices()
        return 1
    elif(action == 3):
        #que
        clickQue()
        return 1
    elif(action == 4):
        #library
        clickLibrary()
        return 1
    elif(action == 5):
        #back
        clickBack()
        return 1
    elif(action == 6):
        #restart
        print("wouldve restarted")
       # restart()
        return 1
    elif(action == 7):
        #home
        clickHome()
        return 1
    else:
        return 0
    
def Humanizer():
      failedsearches = 0
      rval = random.randint(7)
      while(action(rval) != 1):
            rval = random.randint(7)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()
                break

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#////////////////////////////////////////click by section///////////////////////////////////////////////

def clickArtist():
    pag.moveRel(300,125)
    if(pag.locateOnScreen(artist_label,confidence=0.9) != None):
        artistlabelCenter = pag.center(pag.locateOnScreen(artist_label,confidence=0.8))
        pag.moveTo(artistlabelCenter[0],artistlabelCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        t.sleep(1)
        return 1
    else:
        print("couldnt find artist label")
        t.sleep(1)
        
def clickPlaylist():
    pag.moveRel(0,200)
    if(pag.locateOnScreen(playlist_label,confidence=0.9) != None):
        playlistlabelCenter = pag.center(pag.locateOnScreen(playlist_label,confidence=0.8))
        pag.moveTo(playlistlabelCenter[0],playlistlabelCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        t.sleep(1)
    else:
        print("couldnt find playlist label")

def clickAlbum():
    pag.moveRel(0,200)
    if(pag.locateOnScreen(album_label,confidence=0.8) != None):
        albumlabelCenter = pag.center(pag.locateOnScreen(album_label,confidence=0.9))
        pag.moveTo(albumlabelCenter[0],albumlabelCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        t.sleep(1)
        return 1
    else:
        print("couldnt find albumt label")
        t.sleep(1)
        

def clickSong():
    if (pag.locateOnScreen(song_label,confidence=0.8)!=None):
        SlabelCenter = pag.center(pag.locateOnScreen(song_label,confidence=0.8))
        pag.moveTo(SlabelCenter[0],SlabelCenter[1],0.5,pag.easeInElastic)
        pag.moveRel(0,45)
        pag.click(clicks =1)
        return 1
    else:
        print("couldnt locate song label")
        return 0

def clickLiked():
    if (pag.locateOnScreen(liked_label,confidence=0.9)!=None):
        LlabelCenter = pag.center(pag.locateOnScreen(liked_label,confidence=0.8))
        pag.moveTo(LlabelCenter[0],LlabelCenter[1],0.5,pag.easeInElastic)
        pag.click(clicks =1)
        return 1
    else:
        print("couldnt locate liked label")
        return 0

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#///////////////////////////////////////////////////////////////////////////////////////////////////////



#/////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Play by section\\\\\\\\\\\\\\\\\\\
    
def playByArtist(artist):
    if (search(artist)==1):
        t.sleep(1)
        if(clickArtist()==1):
                t.sleep(1)
                if(clickPlay()==1):
                    t.sleep(1)
                    return 1
                else:
                    return 0
        else:
                    return 0
    else:
                    return 0


def playByAlbum(album):
    if (search(album)==1):
        t.sleep(1)
        if(clickAlbum()==1):
                t.sleep(1)
                if(clickPlay()==1):
                    t.sleep(1)
                    return 1
                else:
                    return 0
        else:
                    return 0
    else:
                    return 0
                
def playByPlaylist(playlist):
    if (search(playlist)==1):
        t.sleep(1)
        if(clickPlaylist()==1):
                t.sleep(1)
                if(clickPlay()==1):
                    t.sleep(1)
                    return 1
                else:
                    return 0
        else:
                    return 0
    else:
                    return 0

def playBySong(song,artist):
    if (search(song+" "+artist)==1):
        t.sleep(1)
        if(clickSong()==1):
            return 1     
        else:
            return 0
    else:
            return 0

def playLiked():
    
    if (clickLiked()==1):
        t.sleep(1)
        if(clickPlay()== 1):
            return 1     
        else:
            return 0
    else:
            return 0    
    
  



#/////////////////////////////////////////////////////////////////////
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Play by section above \\\\\\\\\\\\\\\\\\\

    


#////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////full play with certainty below//////////////////////////////////////

def getartistplays(artist):
      failedsearches = 0
      while(playByArtist(artist)!= 1):
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()


def playRandomArtist():
      failedsearches = 0
      rval = random.randint(999)
      while(playByArtist(artists[rval])!= 1):
            rval = random.randint(999)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()
                
def playRandomSong():
      failedsearches = 0
      rval = random.randint(600)
      while(playBySong(random_Songs_song[rval],random_Songs_artist[rval])!= 1):
            rval = random.randint(600)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()

def playRandomAlbum():
      failedsearches = 0
      rval = random.randint(500)
      while(playByAlbum(random_Albums[rval])!= 1):
            rval = random.randint(500)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()

def playRandomPlaylist():
      failedsearches = 0
      rval = random.randint(500)
      while(playByPlaylist(random_Playlist[rval])!= 1):
            rval = random.randint(500)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()
    
def playacrossairSong():
      failedsearches = 0
      rval = random.randint(65)
      while(playBySong(MySongsArtists[rval],MySongsName[rval])!= 1):
            rval = random.randint(65)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()

def playacrossairArtist():
      failedsearches = 0
      rval = random.randint(65)
      while(playByArtist(MySongsArtists[rval])!= 1):
            rval = random.randint(65)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()

def playacrossairAlbum():
      failedsearches = 0
      rval = random.randint(65)
      while(playByAlbum(MyAlbums[rval])!= 1):
            rval = random.randint(65)
            failedsearches = failedsearches +1
            if (failedsearches >=2):
                clickHome()
                


#//////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////full play with certainty above\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\






#generator\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            
# requirments set the character of the sequence
# req says i need plays amount of nodes between 0 and 5 (my songs)
# req2 says i need x amount of nodes valued 5           (humanizing actions)
# req3 says i need x amount of nodes between 5 and 10   (random songs)
# req4 says i need x amount of nodes between 10 and 15  (themed songs)
def generateSeq(nodes,plays,humans,rand,theme):
    satisfied = False
    seq =[0]*nodes
    req1 = False
    req2 = False
    req3 = False
    req4 = False
    i = 0
    seq[i] =1
    val = 0
    print(seq)
    while(satisfied!= True):
        print("starting cycles",i)
        print(seq)
        if(req1 != True):
            seq[i] = random.randint(1,4)
            i = i+1
        if(req2 != True):
            seq[i] = 5
            i = i+1
        if(req3 != True):
            seq[i] = random.randint(6,9)
            i = i+1
        if(req4 != True):
            seq[i] = random.randint(10,13)
            i = i+1

            
        val = 0
        for x in range(len(seq)):
            if(req1 == True):
                break
            if(seq[x] ==1 or seq[x] ==2 or seq[x] ==3 or seq[x] ==4):
                val = val+1
            if(val == plays):
                req1 = True
                break
        val = 0
        for x in range(len(seq)):
            if(req2 == True):
                break
            if(seq[x] ==  5):
                val = val+1
            if(val == humans):
                req2 = True
                break
        val = 0
        for x in range(len(seq)):
            if(req3 == True):
                break
            if(seq[x] ==6 or seq[x] ==7 or seq[x] ==8 or seq[x] ==9):
                val = val+1
            if(val == rand):
                req3 = True
                break
        val = 0
        for x in range(len(seq)):
            if(req4 == True):
                break
            if(seq[x] ==10 or seq[x] ==11 or seq[x] ==12 or seq[x] ==13 ):
                val = val+1
            if(val == theme):
                req4 = True
                break
        if (req1 & req2& req3 &req4 == True):
             satisfied = True
             print(seq)
             return seq
    
