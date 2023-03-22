import os

select = int(input("""Would you like single player or multiplayer
(1) multiplayer
(2) single player
(3) simulation play
"""))

if select == 1:
	os.system('cls')
	os.system('Main\connect4.py')
if select == 2:
	os.system('cls')
	os.system('Main\connect4BOT.py')
if select == 3:
	os.system('cls')
	os.system('Main\connect4BOTvBOT.py')