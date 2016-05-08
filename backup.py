import os

def getFolders(path):
	templist = os.listdir(path)

	for item in templist:
		if (os.path.isfile(item) == True):
			templist.remove(item)
	return templist

def getBackuplist(llist, hlist):
	blist = []
	for item in llist:
		if item not in hlist:
			blist.append(item)
	return blist

laptop_list = getFolders("G:\\Movies")
harddrive_list = getFolders("I:\\Movies")

backup_list = getBackuplist(laptop_list, harddrive_list)

count = 0
for movie in backup_list:
	print(movie)
	count += 1

print ("Laptop = {0} \nHard drive = {1}".format(len(laptop_list), len(harddrive_list)))

print ("There are {movie_count} movies that are not backed up!".format(movie_count = count))

# move watched movies to hard drive prompt
# show progress bar
# while moving, check substrings, if found, prompt user which file to keep