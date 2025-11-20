# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 18:25:30 2025

@author: kaife
"""
from Game import *
import os
import json

game_list = {}
game_name_set = set()


def add_game(new_game:Game):
    '''Adds a game to the current game list'''
    game_list[new_game._name] = new_game
    game_name_set.add(new_game._name)
    
def remove_game(game_name):
    '''Removes a game from the current game list'''
    del game_list[game_name]
    
    
def full_export_txt(filename = "game_ratings.txt"):
    '''Exports *all* of the game rating log data into a .txt file in 
    a readable format'''
    try:    
        with open(filename, 'w', encoding="utf-8") as file:
            for game in game_list.values():
                file.write(repr(game) + "\n\n")
    except Exception as e:
        print(f"Failed to export data due to error: {e}")
    else:
        print(f"Exported current game rating log to {filename}")

def full_export_json(filename = "game_ratings.json"):
    data = {}
    for name, game in game_list.items():
            data[name] = {
                "name": game._name,
                "rating": game.rating,
                "console": game.console,
                "notes": game.notes
            }
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Exported current game rating log to {filename}")

def full_import_json(filename="game_ratings.json"):
    global game_list, game_name_set
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            game_list.clear()
            game_name_set.clear()
            for game_data in data.values():
                g = Game(
                    name=game_data["name"],
                    rating=game_data["rating"],
                    console=game_data["console"]
                )
                g.notes = game_data["notes"]
                add_game(g)
    except Exception as e:
        print(f"Failed to import data due to error: {e}")
    else:
        print(f"Imported {len(game_list)} games from {filename}")


def sort_by_rating():
    '''Returns the sorted list of games using the ratings'''
    return sorted(game_list, reverse=True)

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
            #prompt for game info and add to game_list
            next_game = Game()
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
                    new_status = input(f"Enter new status for [key_to_check] : ")
                    game_list[key_to_check].update_status(new_status)
                if update_choice == 'r':
                    new_rating = input(f"Input new rating for {key_to_check} : ")
                    game_list[key_to_check].update_rating(new_rating)
                if update_choice == 'c':
                    new_console = input(f"Input new console for {key_to_check} : ")
                    game_list[key_to_check].update_console(new_console)
            else: print(f"The game {key_to_check} "
                        "does not exist in your rating log...")
            
        elif user_input == "note":
            game_to_check = input("What game would you like to add a"
                                  " note to?:")
            if game_exists(game_to_check):
                print("game exists, adding note now")
                game_list[game_to_check].add_note()
            else: print(f"The game {game_to_check} "
                        "does not exist in your rating log...")
                
        elif user_input == "view list":
            #Prints the list of the names of current games in log 
            print("Current games in log: ")
            for item in game_name_set:
                print(f"\n {item}")
                
        elif user_input == "view game":
            #Prints a single game review if game exists in log
            game_to_view = input("Which game "
                                 "would you like to view? : ").lower()
            if game_exists(game_to_view):
                print(game_list[game_to_view])
            else: print(f"The game {game_to_view} "
                        "does not exist in your rating log...")
            
        elif user_input == "view all games":
            #Asks user if they want to view the list in order of 
            #input or rating and prints the game log
            choice = input("Enter '1' if you want the log in order of when "\
                           "they were added and '2' if you want them"\
                               " sorted by rating: ")
            if choice=='1':
                print("Here is your game rating log in order of input:")
                for game in game_list:
                    print(game_list[game])
            elif choice=='2':
                sorted_list = sort_by_rating()
                for game in sorted_list:
                    print(game_list[game])
            else:
                print("Sorry, you did not select a valid option...")
            
        elif user_input == "export":
            #Ask user how they would like to export the data and call
            #corresponding method
            confirm = input("Enter 'C' to confirm full export:")
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
        
        
        