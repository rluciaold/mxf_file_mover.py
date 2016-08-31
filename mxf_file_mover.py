import os, shutil

### This script will search ALL local files and subfolders except folders with "newscratch" in the prefix and move all .MXF video files into
### a newly created "newscratch" folder. Can be run multiple times, will not create empty folders and will move .MXF files
### into a new folder numbered accordingly (ex: newscratch2 if newscratch1 is taken.)

######
## to do:
## add userinput for folder name?
## add userinput for filetype to move
## add compat for python 2
## make this executable? how do you even do that

def mxf_mover(x):
	foldernumber = x
	folderprefix = "newscratch"
	folderfullname = (folderprefix + str(foldernumber))

	### try to create folder newscratch1
	### if taken, try newscratch2, and so on.
	### this directory will be deleted at end of script if it is still empty

	try:
		os.mkdir(folderfullname)
		print("Created directory named " + folderfullname)
	except:
		print("Directory already exists! Couldn't make: " + folderfullname)
		mxf_mover(foldernumber+1)
		return


	### check all files and subfolders that this script is located in locally
	for root, dirs, files in os.walk("./"):
		###  skip any folders that start with newscratch
		if root.startswith("./"+folderprefix):
			pass
			# print("___Skipping " + folderfullname)
		else:
			for name in files:
				### If the file ends with .mxf, move it to the new folder
				if name.endswith((".MXF")):
					quicktest = os.path.abspath(name)
					print("MOVED: " + name)
					xfile = root+("/")+name
					# print(xfile)
					shutil.move(xfile,os.path.abspath(folderfullname +'/'))
				else:
					print("NOT MOVED: " + name)



	### last part. check if there are files in new folder. if not, delete the empty folder.
	counter = 0
	for files in os.scandir(folderfullname):
		# print (files)
		counter +=1
		break
	if counter >= 1:
		print("SCRIPT COMPLETED. All .MXF files in this folder and its subfolders have been moved to the newly created directory named: " + folderfullname)
		# print(counter)
	else:
		print("No .MFX files found! The empty directory created has been automatically deleted.")
		os.rmdir(folderfullname)


mxf_mover(1)

