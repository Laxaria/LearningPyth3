import plistlib

# To-use: Ensure a file named "iTunes Music Library.xml" is in the 
# same directory as this Python script

with open("iTunes Music Library.xml", "rb") as file:
    pl = plistlib.load(file)

# Pull out only the track name, duration, and play count
# Ignore all tracks without play count
def listingSongs():
    listSongs = []
    for i in pl['Tracks']:
        try:
            listSongs.append([str(pl['Tracks'][i]['Name']), pl['Tracks'][i]['Total Time'], pl['Tracks'][i]['Play Count']])
        except KeyError:
            pass
    return listSongs

# Calculate total listened-to time
def time_calc(a):
    songTotals = 0
    for i in a:
        songTotals += (i[1] * i[2])
    return songTotals

totalListened = time_calc(listingSongs())/86400000
print('Total iTunes listening time is {0:2.2f} days.'.format(totalListened))