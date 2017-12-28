# Setup 
you must aquire cream api steam_api.dll and steam_api64.dll and place in this folder

# WARNING
This will only tell the game you own the DLC it will not allow download of DLC content from steam.
If DLC download is required to use DLC then this will not help you unless you illegally aquire the DLC files.

# AUTOINSTALL.py usage
## 1 installing
run autoinstall.py
choose a game from the list printed (you must type it exactly the same)
paste the games dir (e.g. C:\Program Files (x86)\Steam\steamapps\common\Arma 3)
install complete

## 2 adding game configs
after you have made your config (configs\steampagegenerator.js) paste it in a folder of the games name (e.g. configs\Arma 3\cream_api.ini)
next time you run this config will be available

## 3 troubleshooting
Errors:
#### Game does not appear in list at start
- make sure you have made a directory in autoinstall.py dir\configs\
-  make sure this directory contains your config called cream_api.ini

#### Invalid game
-  check you have copied the name exactly from this list of games printed

#### Invalid game directory
-  check you have entered the correct directory (e.g. C:\Program Files (x86)\Steam\steamapps\common\Arma 3)
-  check this directory contains steam_api.dll and steam_api64.dll

#### Cream api is already installed for this game
-  check you have steam_api_o.dll and steam_api64_o.dll
-  delete steam_api.dll and steam_api64.dll
-  rename steam_api_o.dll to steam_api.dll and steam_api64_o.dll to steam_api64.dll
-  next time you run install should work

#### Error installing creamapi
-  try running autoinstall.py with administrator permissions
  
# HOW TO without script
1) Go to base folder of game (steamapps\common\<game>\)
2) Rename steam_api.dll to steam_api_o.dll & steam_api64.dll to steam_api64_o.dll
3) Copy steam_api.dll & steam_api64.dll from this folder into that games folder
4) Copy your games config into the same folder you put steam_api.dll in E.g. for arma3 copy config from configs/arma3/ to steamapps/common/Arma 3/
5) Launch your game
