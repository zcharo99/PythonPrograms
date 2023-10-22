#!/usr/bin/env python3
from simple_term_menu import TerminalMenu

def main():
    options = ["option 1", "option 2", "option 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You selected option {options[menu_entry_index]}")


if __name__ == "__main__":
    main()