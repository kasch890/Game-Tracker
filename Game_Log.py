# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 18:25:30 2025

@author: kaife
"""
from Game import *
import os

game_list = {}
game_name_set = set()


def add_game(new_game:Game):
    '''Adds a game to the current game list'''
    game_list[new_game._name] = new_game
    game_name_set.add(new_game._name)
    
def remove_game(game_name):
    '''Removes a game from the current game list'''
    del game_list[game_name]
    
    
def full_export(filename = "game_ratings.txt"):
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
#         COMMENTED OUT SIMPLE EXPORT, MAY NOT NEED FOR MY OWN USE
# def simple_export(filename = "simple_game_ratings.txt"):
#     '''Exports just the name and rating pairs for each game in rating log'''
#     try:
#         with open(filename, 'w', encoding="utf-8") as file:
#             for game in game_list.values():
#                 simp = game.simple_game_info()
#                 file.write(f"{simp[0]}: {simp[1]}\n")
#     except Exception as e:
#         print(f"Failed to export data due to error: {e}")
#     else:
#         print(f"Exported current game rating log to {filename}")

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
              (1) Add game rating
              (2) Remove game rating
              (3) Update existing rating
              (4) Add comment to game
              (5) View list of existing games
              (6) View single game 
              (7) View all games
              (8) Export game rating log data
              (9) Exit Program \n
              Input number here: 
              ''')
        #All non valid inputs reset the while loop
        
        if user_input == "1":
            #prompt for game info and add to game_list
            next_game = Game()
            add_game(next_game)
            continue
        
        elif user_input == "2":
            #Check if game exists in list and remove it if it does
            key_to_check = input("What is the game "
                                "you would like to remove?: ").lower()
            if game_exists(key_to_check):
                remove_game(key_to_check)
            else: print(f"The game {key_to_check} "
                        "does not exist in your rating log...")
            
        elif user_input == "3":
            #Check if game exists and update its rating, prompting
            #user until valid input
            key_to_check = input("What game would you "
                                 "like to update the rating of? : ").lower()
            if game_exists(key_to_check):
                new_rating = input(f"Input your new rating for "
                                   f"{key_to_check} here: ")
                game_list[key_to_check].update_rating(new_rating)
            else: print(f"The game {key_to_check} "
                        "does not exist in your rating log...")
            
        elif user_input == "4":
            game_to_check = input("What game would you like to add a"
                                  " comment to?:")
            if game_exists(game_to_check):
                print("game exists, adding comment now")
                game_list[game_to_check].add_comment()
            else: print(f"The game {game_to_check} "
                        "does not exist in your rating log...")
                
        elif user_input == "5":
            #Prints the list of the names of current games in log 
            print("Current games in log: ")
            for item in game_name_set:
                print(f"\n {item}")
                
        elif user_input == "6":
            #Prints a single game review if game exists in log
            game_to_view = input("Which game "
                                 "would you like to view? : ").lower()
            if game_exists(game_to_view):
                print(game_list[game_to_view])
            else: print(f"The game {game_to_view} "
                        "does not exist in your rating log...")
            
        elif user_input == "7":
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
            
        elif user_input == "8":
            #Ask user how they would like to export the data and call
            #corresponding method
            confirm = input("Enter 'C' to confirm full export:")
            if confirm.upper()=='C':
                full_export()
            else:
                print("Canceling export...")
                
        elif user_input == "9":
            #Exit the program
            finished = True
            print ("***Program Terminated***")
        else:
            print("Invalid option. Please try again.")
        
        
        