def main():
    global songsInfo, songLine, MENU, userInputChoice

    """Main Program"""
    songsFileLocation = open("songs.csv")
    songsAuthenticInfo = songsFileLocation.readlines()
    songsInfo = []
    for songLine in songsAuthenticInfo:
        song_string = songLine.strip().split(",")
        songsInfo.append(song_string)
    print("Songs need to be completed 1.0 - by Arvin kosasih\n"  
          "{} songs loaded".format(len(songsAuthenticInfo)))

    MENU = """Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""
    print(MENU)
    userInputChoice = input(">>> ").upper()
    while userInputChoice != "Q":
        if userInputChoice == "L":
            List()
        elif userInputChoice == "A":
            addSong()
        elif userInputChoice == "C":
            completeSong()
        else:
            print("Invalid menu userInputChoice")
        print(MENU)
        userInputChoice = input(">>> ").upper()
    Quit()

def List():
    global uncompleteSongs, songLine, title, artist, year
    """display list of songs"""
    totalAmountofSongs = 0
    songsHasBeenCompleted = 0
    uncompleteSongs = 0
    for songLine in songsInfo:
        title = songLine[0]
        artist = songLine[1]
        year = int(songLine[2])
        if songLine[3] == "y":
            complete = "*"
            uncompleteSongs += 1
        else:
            complete = " "
            songsHasBeenCompleted += 1
        print("{}. {:<1} {:<24} - {:<24} ({})".format(totalAmountofSongs, complete, title, artist, year))
        totalAmountofSongs += 1
    print("{} songs learnt, {} songs still to learn".format(songsHasBeenCompleted, uncompleteSongs))

def addSong():
    global title, artist, validInput, year
    """add new song into songs_new_data"""
    new_song = []
    title = input("Title: ").strip()
    while title == "":
        print("Input can not be blank")
        title = input("Title: ").strip()
    new_song.append(title)
    artist = input("Artist: ").strip()
    while artist == "":
        print("Input can not be blank")
        artist = input("Artist: ").strip()
    new_song.append(artist)
    while True:
        try:
            year = int(input("Year: "))
            while year < 0:
                print("Number must be >= 0")
                year = int(input("Year: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    new_song.append(year)
    new_song.append("y")
    songsInfo.append(new_song)
    print("{} by {} ({}) added to song list".format(title, artist, year))

def completeSong():
    global uncompleteSongs, songLine, validInput
    """complete song that have not been learnt"""
    uncompleteSongs = 0
    for songLine in songsInfo:
        if songLine[3] == "y":
            uncompleteSongs -= 1
    if uncompleteSongs != 0:
        while True:
            try:
                songsNeedToBeLearnt = int(input("Enter the number of a song to mark as learned: "))
                while not 0 <= songsNeedToBeLearnt <= len(songsInfo) - 1:
                    if songsNeedToBeLearnt > len(songsInfo) - 1:
                        print("Invalid song number")
                        songsNeedToBeLearnt = int(input("Enter the number of a song to mark as learned: "))
                    elif songsNeedToBeLearnt < 0:
                        print("Number must be >= 0")
                        songsNeedToBeLearnt = int(input("Enter the number of a song to mark as learned: "))
                break
            except ValueError:
                print("Invalid input; enter a valid number")
        if songsInfo[songsNeedToBeLearnt][3] == "y":
            songsInfo[songsNeedToBeLearnt][3] = "n"
            print("'{}' by '{}' learned".format(songsInfo[songsNeedToBeLearnt][0],
                                                songsInfo[songsNeedToBeLearnt][1]))
        elif songsInfo[songsNeedToBeLearnt][3] == "n":
            print("You have already completed '{}'".format(songsInfo[songsNeedToBeLearnt][0]))
    else:
        print("No more songs to complete")

def Quit():
    global fileOutput
    """quit program and save new data to csv file"""
    fileOutput = open("songs.csv", "w")
    for saved_data in songsInfo:
        new_data = "{},{},{},{}".format(saved_data[0], saved_data[1], saved_data[2], saved_data[3]) + "\n"
        fileOutput.write(new_data)
    print("{} total songs has been saved to {}".format(len(songsInfo), "songs.csv"))
    print("Thank you for using our app, we hope to see you again!")
    fileOutput.close()

main()