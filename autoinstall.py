import os
import shutil

def comparefiles(file1,file2):
	same = False
	try:
		f = open(file1,"rb")
		f1 = f.read()
		f.close()
	except FileNotFoundError:
		f1 = ""
	try:
		f = open(file2,"rb")
		f2 = f.read()
		f.close()
	except FileNotFoundError:
		f2 = ""
	if f1 == f2:
		same = True
	return same

curdir = os.getcwd()
configdir = curdir + "\\configs\\"

games = []
for root, dirs, files in os.walk(configdir):
	for dir in dirs:
		if os.path.isfile(root+"\\"+dir+"\\cream_api.ini"):
			games.append(dir)
		
games.sort()
print("Please choose a game: ")
for a in games:
	print(a)
a = ""
while a not in games:
	a = input("Choose a game: ")
	if a not in games:
		print("Invalid game please re-enter")

cfgloc = configdir + a + "\\cream_api.ini"
apiloc = curdir + "\\steam_api.dll"
api64loc = curdir + "\\steam_api64.dll"

isgame = False
while isgame == False:
	gamedir = input("Enter game directory: ")
	apiacloc = gamedir + "\\steam_api.dll"
	api64acloc = gamedir + "\\steam_api64.dll"
	if os.path.isfile(apiacloc) and os.path.isfile(api64acloc):
		isgame  = True
	else:
		print("Invalid game directory please re-enter")

if comparefiles(apiloc,apiacloc) or comparefiles(api64loc,api64acloc) or os.path.isfile(gamedir + "\\steam_api_o.dll") or os.path.isfile(gamedir + "\\steam_api64_o.dll"):
	print("Cream API is already installed for this game.\nPlease remove it to install")
else:
	try:
		os.rename(apiacloc,gamedir + "\\steam_api_o.dll")
		try:
			os.rename(api64acloc,gamedir + "\\steam_api64_o.dll")
			try:
				shutil.copy(cfgloc,gamedir + "\\cream_api.ini")
				try:
					shutil.copy(apiloc,apiacloc)
					try:
						shutil.copy(api64loc,api64acloc)
						print("Cream API has been installed to " + gamedir)
					except:
						os.remove(api64acloc)
						os.remove(gamedir + "\\cream_api.ini")
						os.rename(gamedir + "\\steam_api_o.dll",apiacloc)
						os.rename(gamedir + "\\steam_api64_o.dll",api64acloc)
						print("Error installing creamapi")
				except:
					os.remove(gamedir + "\\cream_api.ini")
					os.rename(gamedir + "\\steam_api_o.dll",apiacloc)
					os.rename(gamedir + "\\steam_api64_o.dll",api64acloc)
					print("Error installing creamapi")
			except:
				os.rename(gamedir + "\\steam_api_o.dll",apiacloc)
				os.rename(gamedir + "\\steam_api64_o.dll",api64acloc)
				print("Error installing creamapi")
		except:
			os.rename(gamedir + "\\steam_api_o.dll",apiacloc)
			print("Error installing creamapi")
	except:
		print("Error installing creamapi")
	
	
