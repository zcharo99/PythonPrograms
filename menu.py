import os
import json

# loads in the data from data.json
# also the commands have been stored outside of the python file as it makes the code way more readable
with open("./data.json", "r") as F:
	reading = F.read()
	data = json.loads(reading)
	options1 = data["options1"]
	options2 = data["options2"]

# you can use """""" for big strings and have tabs in them without needing to call the print fuction twice or more
text = """
1) Install Alacritty
2) Install st
3) Install kitty
4) Install Gnome Terminal
5) Install Konsole
6) Install a Desktop
7) Exit
"""

text2 = """
Desktops:
1) Xorg Server
2) KDE Plasma
3) GNOME
4) Qtile
5) Hyprland
6) i3wm
7) bspwm + sxhkd
8) Exit
"""

# gets the keys from the dicts that were loaded in from the json file
# aka the choices for text1 (1-5) and for text2 (1-7)
max_option1 = options1.keys(); max_option1 = list(max_option1)
max_option2 = options2.keys(); max_option2 = list(max_option2)

while True:
	print(text)
	choice = input("Choice: ")
	# when dealing with operations where you have multiple options it's better to use a dicts
	# instead of using if and elif all the time
	if choice in max_option1:
		# when looking at the code before it was done like os.system("command1" or "command2" or "command3")
		# what i'm guessing what the idea was is that it would run those three commands but os.system() doesn't see the "or"
		# instead it sees it like this os.system("command1") it doesn't see "command2" and "command3"
		# so the best way to deal with this is making a for loop and making it loop trough a list with the commands
		# what has been done here
		for I in options1[choice]:
			os.system(I)
		print("package/application installed!")
	# i've done the same thing here as above
	# you can write a if statement like you did as if (desktopchoice == "1"): what will work but python takes it with the () the same way
	# and is how most people write their if statements
	elif choice == "6":
		print(text2)
		desktopchoice = input("Desktop Choice: ")
		if desktopchoice in max_option2:
			for I in options2[desktopchoice]:
				os.system(I)
			print("package/application installed!")
		elif desktopchoice == "8":
			break
	elif choice == 7:
		exit(0)