# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 18:25:30 2025

@author: kaife
"""
from Game import *
import os
import json

game_dict = {}
game_name_set = set()

def prompt_new_game() -> Game:
    name = input("Enter the game name: ").lower()
    status = input("Enter status ( playing, watched, wishlist : ").lower()
    print("Game successfully created for log!")
    return Game(name=name, status=status)

def add_game(new_game:Game):
    '''Adds a game to the current game list'''
    game_dict[new_game._name] = new_game
    game_name_set.add(new_game._name)
    
def remove_game(game_name):
    '''Removes a game from the current game list'''
    del game_dict[game_name]
    
    
def full_export_txt(filename = "game_ratings.txt"):
    '''Exports *all* of the game rating log data into a .txt file in 
    a readable format'''
    try:    
        with open(filename, 'w', encoding="utf-8") as file:
            for item in game_dict.values():
                file.write(repr(item) + "\n\n")
    except Exception as e:
        print(f"Failed to export data due to error: {e}")
    else:
        print(f"Exported current game rating log to {filename}")

def full_export_json(filename = "game_ratings.json"):
    data = {}
    for name, item in game_dict.items():
        data[name] = {
            "name": item._name,
            "rating": item.rating,
            "console": item.console,
            "status": item.status,
            "notes": item.notes
        }
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Exported current game rating log to {filename}")

def full_import_json(filename="game_ratings.json"):
    global game_dict, game_name_set
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            game_dict.clear()
            game_name_set.clear()
            for game_data in data.values():
                g = Game(
                    name=game_data["name"],
                    status = game_data["status"],
                    rating=game_data["rating"],
                    console=game_data["console"]
                )
                g.notes = game_data["notes"]
                add_game(g)
    except Exception as e:
        print(f"Failed to import data due to error: {e}")
    else:
        print(f"Imported {len(game_dict)} games from {filename}")

#old sort function
# def sort_by_rating():
#     '''Returns the sorted list of games using the ratings'''
#     return sorted(game_dict, reverse=True)

def sort_by_name():
    temp_dict ={}
    sorted_keys = sorted(game_dict.keys())
    for key in sorted_keys:
        temp_dict[key] = game_dict[key]
    game_dict.clear()
    game_dict.update(temp_dict)
    return game_dict


def game_exists(game_to_check:str):
    if game_to_check in game_name_set:
        return True
    else: return False
    
if __name__ == "__main__":
    #print welcome banner
    print("Welcome to your game rating log!\n")
    finished = False
    
    #Start user input loop until terminated
    while not finished:
        print("~ "*24 )
        user_input = input('''What would you like to do?\n
               [add]    -   Add game 
               [remove] -   Remove game
               [edit]   -   Edit existing game
               [vg]     -   View game
               [vl]     -   View list of games
               [export] -   Export game log data
               [import] -   Import game log data
               [exit]   -   Exit Program \n
              Input command here: 
              ''')

        user_input = user_input.lower()
        #All non valid inputs reset the while loop
        
        if user_input == "add":
            #prompt for game info and add to game_dict
            next_game = prompt_new_game()
            add_game(next_game)
            continue
        
        elif user_input == "remove":
            #Check if game exists in list and remove it if it does
            key_to_check = input("What is the game "
                                "you would like to remove?: ").lower()
            if game_exists(key_to_check):
                remove_game(key_to_check)
            else: print(f"The game {key_to_check} "
                        "does not exist in your rating log...")
            
        elif user_input == "edit":
            #Check if game exists and update its rating, prompting
            #user until valid input
            key_to_check = input("What game would you "
                                 "like to edit? : ").lower()
            if game_exists(key_to_check):
                #Ask what they would like to update: status, rating, console, notes
                update_choice = input("Would you like to update the [s] status, [r] rating, [c] console, or [n] notes? : ").lower()
                if update_choice == 's':
                    new_status = input(f"Enter new status for {key_to_check} : ")
                    game_dict[key_to_check].update_status(new_status)
                if update_choice == 'r':
                    new_rating = input(f"Input new rating for {key_to_check} : ")
                    game_dict[key_to_check].update_rating(new_rating)
                if update_choice == 'c':
                    new_console = input(f"Input new console for {key_to_check} : ")
                    game_dict[key_to_check].update_console(new_console)
                if update_choice == 'n':
                    notes_done = False
                    while not notes_done:
                        note_input = input(f"Input new note for {key_to_check} or enter 'cancel' : ")
                        if note_input == 'cancel':
                            notes_done = True
                        else:
                            game_dict[key_to_check].add_note(note_input)
            else: print(f"The game {key_to_check} "
                        "does not exist in your rating log...")

        elif user_input == "vg":
            #Prints a single game review if game exists in log
            game_to_view = input("Which game "
                                 "would you like to view? : ").lower()
            if game_exists(game_to_view):
                print(game_dict[game_to_view])
            else: print(f"The game {game_to_view} "
                        "does not exist in your rating log...")

        elif user_input == "vl":
            #Prints the list of the names of current games in log
            sort_choice = input("Would you like to sort the list first? [y] or [n] : ").lower()
            if sort_choice == 'y':
                game_dict = sort_by_name()
            view_choice = input("Would you like simple [s] or detailed [d] list? : ").lower()
            if view_choice == 's':
                print("Current games in log: ")
                for key in game_dict:
                    print(f"\n {key}")
            elif view_choice == 'd':
                for game in game_dict:
                    print(game_dict[game])
            else:
                print("Sorry, you did not select a valid option...")

        elif user_input == "export":
            #Ask user how they would like to export the data and call
            #corresponding method
            confirm = input("Enter 'C' to confirm full .json export:")
            if confirm.upper()=='C':
                full_export_json()
            else:
                print("Canceling export...")
        elif user_input == "import":
            full_import_json()
                
        elif user_input == "exit program":
            #Exit the program
            confirm = input("Enter 'C' to confirm program exit:")
            if confirm.upper() == 'C':
                finished = True
                print("***Program Terminated***")

            else:
                print("Canceling exit...")

        else:
            print("Invalid option. Please try again.")
        
        
        