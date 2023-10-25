#!/usr/bin/env python3
import os

choice = ""

while True:
    print("1) Install Alacritty")
    print("2) Install st")
    print("3) Install kitty")
    print("4) Install Gnome Terminal")
    print("5) Install Konsole")
    print("6) Install a Desktop")
    print("7) Exit")

    choice = input("Choice: ")

    choice = choice.strip()
    if (choice == "1"):
        print("Installing Alacritty")
        os.system("sudo apt-get install alacritty" or "sudo pacman -S alacritty" or "sudo dnf install alacritty")
        print("Alacritty Installed")
    elif (choice == "2"):
        print("Installing st")
        os.system("sudo apt-get install st" or "sudo pacman -S st" or "sudo dnf install st")
        print("st Installed")
    elif (choice == "3"):
        print("Installing kitty")
        os.system("sudo apt-get install kitty" or "sudo pacman -S kitty" or "sudo dnf install kitty")
        print("kitty Installed")
    elif (choice == "4"):
        print("Installing Gnome Terminal")
        os.system("sudo apt-get install gnome-terminal" or "sudo pacman -S gnome-terminal" or "sudo dnf install gnome-terminal")
        print("Gnome Terminal Installed")
    elif (choice == "5"):
        print("Installing Konsole")
        os.system("sudo apt-get install konsole" or "sudo pacman -S konsole" or "sudo dnf install konsole")
        print("Konsole Installed\n")
    elif (choice == "6"):
        desktopchoice = ""
        while True:
            print("\nDesktops:")
            print("1) Xorg Server")
            print("2) KDE Plasma")
            print("3) GNOME")
            print("4) Qtile")
            print("5) Hyprland")
            print("6) i3wm")
            print("7) bspwm + sxhkd")
            print("8) Exit")
            desktopchoice = input("Desktop Choice: ")
            desktopchoice = desktopchoice.strip()
            if (desktopchoice == "1"):
                print("Installing Xorg Server\n")
                os.system("sudo apt-get install xorg-server" or "sudo pacman -S xorg-server" or "sudo dnf install xorg-server")
                print("\nXorg Server Installed")
            elif (desktopchoice == "2"):
                print("Installing KDE Plasma\n")
                os.system("sudo apt-get install kde-plasma" or "sudo pacman -S kde-plasma" or "sudo dnf install kde-plasma")
                print("\nKDE Plasma Installed")
            elif (desktopchoice == "3"):
                print("Installing GNOME\n")
                os.system("sudo apt-get install gnome" or "sudo pacman -S gnome" or "sudo dnf install gnome")
                print("\nGNOME Installed")
            elif (desktopchoice == "4"):
                print("Installing Qtile\n")
                os.system("sudo apt-get install qtile" or "sudo pacman -S qtile" or "sudo dnf install qtile")
                print("\nQtile Installed")
            elif (desktopchoice == "5"):
                print("Installing Hyprland\n")
                os.system("sudo apt-get install hyprland" or "sudo pacman -S hyprland" or "sudo dnf install hyprland")
                print("\nHyprland Installed")
            elif (desktopchoice == "6"):
                print("Installing i3wm\n")
                os.system("sudo apt-get install i3" or "sudo pacman -S i3" or "sudo dnf install i3")
                print("\ni3wm Installed")
            elif (desktopchoice == "7"):
                print("Installing bspwm + sxhkd\n")
                os.system("sudo apt-get install bspwm sxhkd" or "sudo pacman -S bspwm sxhkd" or "sudo dnf install bspwm sxhkd")
                print("\nbspwm + sxhkd Installed")
            elif (desktopchoice == "8"):
                break
    elif (choice == "7"):
        break