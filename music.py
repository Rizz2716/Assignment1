# Name: Mohamed Rizwan S/O Rowthersa
# ID: 13559521
# Date: 09 December 2018
#
# This program is a simple song list that allows a user to track songs that they wish to learn and songs they have completed learning. The program reads and writes a list of songs in a file.
# Each song has:
# •	title, artist, year, whether it is required (y) or learned (n)
# Users can choose to see the list of songs, which should be sorted by artist then by title.
# Users can add new songs and mark songs as learned.
# They cannot change songs from learned to required.
#
# https://github.com/Rizz2716/Assignment1

def main():
    MENU = """ Menu:
        L - List songs
        A - Add new song
        C - Complete a song
        Q - Quit"""

    print("Welcome Rizwan")
    print(MENU)
    option = input("Enter your choice ").upper()
    temp_file = open("songs.csv", "r")
    songs_list = temp_file.readlines()
    final_list = []
    for song in songs_list:
        final_list.append(song.strip().split(","))

    temp_file.close()
    while option != "Q":
        num_y = 0
        num_n = 0
        num = 0
     # """
     # Read songs in CSV file
     # songs_list = Songs
     # Final_list = songs_list
     # if option = L
     #  for song in final list:
     #    if  song[3} == y (required )
     #        print (song with * in it)
     #    else
     #        print( song )
     # print( number of songs learned and number of song still to learn
     # """
        if option == "L":
            for song in final_list:
                if song[3] == 'y':
                    print("{:3}. * {:37} - {:29}  ({:4})".format(num + 1, song[0], song[1], song[2]))
                    num += 1
                    num_y += 1
                else:
                    print("{:3}.   {:37} - {:29}  ({:4})".format(num + 1, song[0], song[1], song[2]))
                    num += 1
                    num_n += 1
            print(num_n, "songs learned,",num_y,"songs still to learn")
        elif option == "A":
            print("Add new song")
            title = input("Enter Title:\n")
            while len(title) < 1:
                print("Input cannot be blank")
                title = input("Enter Title:\n")
                print(title)
            artist = input("Enter Artist name:\n")
            while len(artist) < 1:
                print("Input cannot be blank")
                artist = input("Enter Artist name:\n")
                print(artist)
            year = input("Enter Year:\n")
            while len(year) < 4 or len(year) > 4:
                if year != int:
                    print("Invalid input, enter a valid number")
                elif year < 0:
                    print("Number must be more than 0")
                elif year > 4:
                    print("Invalid input")
                elif year == str:
                    print("Invalid input, Enter numbers")
                else:
                    print(year)
                print("Input cannot be blank")
                year = input("Enter year:\n")
            new_song = []
            new_song.append(title)
            new_song.append(artist)
            new_song.append(year)
            new_song.append("y")
            final_list.append(new_song)
            print(title, "by", artist, "(",year,") added to song list")
# """
#     for song in final list:
#        if  song[3} == y (required )
#            print (song with * in it)
#        else
#            print( song )
#     prompt user for song_num that user wants to learn
#     get song_num
#     if song_num <0 or song_num > num of songs
#         print (Invalid input)
#     else
#       break
#     if num_y(requried song) == 0
#        print (no more song to learn)
#     elif final_list[song_num-1][3] == "n":
#                 print(song is already learned")
#     else:
#                 final_list[song_num-1][3] = "n"
#                 print(song is learned")
#     """
        elif option == "C":
            for song in final_list:
                if song[3] == 'y':
                    print("{:3}. * {:37} - {:29}  ({:4})".format(num + 1, song[0], song[1], song[2]))
                    num += 1
                    num_y += 1
                else:
                    print("{:3}.   {:37} - {:29}  ({:4})".format(num + 1, song[0], song[1], song[2]))
                    num += 1
                    num_n += 1
            while True:
                try:
                    song_num = int(input("Enter the number of the song to be marked as learned "))
                except ValueError:
                    print("Invalid input")
                    continue
                if song_num < 0:
                    print("Number must be more than 0")
                elif song_num > num:
                    print("Invalid song number")
                else:
                    break
            if num_y == 0:
                print("No more songs to learn")
            elif final_list[song_num-1][3] == "n":
                print(final_list[song_num-1][0],"by",final_list[song_num-1][1],"is already learned")
            else:
                final_list[song_num-1][3] = "n"
                print(final_list[song_num-1][0],"by",final_list[song_num-1][1],"learned")
        else:
            print("invalid option")
        print(MENU)
        option = input("Enter your choice ").upper()
    temp_file = open("songs.csv", "w")
    for song in final_list:
        print((",".join(song)), file=temp_file)
    temp_file.close()
    print(len(final_list), "songs saved to songs.csv")
    print("Have a nice day")


main()
