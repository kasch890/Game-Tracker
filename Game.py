# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 19:38:48 2025

@author: kaife
"""

class Game():
    '''This class holds a game review to be included in our game log. 
    Games have properties that may and may not be updated'''
    
    
    def __init__(self, name=None, status=None, rating=None, console=None):
        '''Instantiates a Game object and prompts user for the name and rating,
        adds an empty comment list attribute,
        and sets the attribute console="" '''
        #get a valid name input
        while True:
            try:
                if name==None:
                    name = input("Enter the game name: ").lower()
                if not isinstance(name, str):
                     raise TypeError("Name must be a string.")
                break
            
            except TypeError as e:
                print(e)
                name = None
        #get valid status input
        while True:
            try:
                if status == None:
                    status = input("Enter the status (Played, Watched, Wishlist): ").lower()
                if not isinstance(status, str):
                    raise TypeError("Status must be a string.")
                break

            except TypeError as e:
                print(e)
                status = None

        #[NO LONGER NECESSARY FOR GAME CREATION]
        #get a valid rating input
        # while True:
        #     try:
        #         if rating==None:
        #             rating_input = input(f"Enter your rating for {name}: ")
        #             try:
        #                 rating = float(rating_input)
        #             except ValueError:
        #                 raise ValueError("Rating must be a number between 0.0 and 5.0")
        #         if not (0.0 <= rating <=5.0):
        #             raise ValueError("Rating must be between 0.0 and 5.0")
        #         break
        #     except ValueError as e:
        #         print(e)
        #         rating=None

        #[NO LONGER NECESSARY FOR GAME CREATION]
        # get valid console input
        #
        # while True:
        #     try:
        #         if console==None:
        #             console = input("Enter the console you played on: ").lower()
        #         if not isinstance(console, str):
        #              raise TypeError("Console must be a string.")
        #         break
        #
        #     except TypeError as e:
        #         print(e)
        #         console = None
        #
        print("Game successfully created for log!")
        self._name = name
        self.status = status
        self.rating = rating
        self.console = console
        self.comments = []
        
    
    def add_comment(self,comment=None):
        '''Adds a comment to comments attribute of the Game 
        (which is a list) by asking for user input'''
        if comment == None:
            comment = input("Enter comment here: ")
        comment = str(comment)
        self.comments.append(comment)
    
    
    def update_rating(self, new_rating = None):
        '''Updates the rating of the game by taking user input and 
        validating that input using __validate__rating()'''
        self.rating = self.__validate__rating(new_rating)
            
    #private method
    def __validate__rating(self, new_rating=None):
        '''Validates the user input for a new rating by making sure it is a 
        number between 0 and 5'''
        while True:
            try:
                if new_rating==None:
                    rating_input = input("Enter your new rating: ")
                    try:
                        new_rating = float(rating_input)
                    except ValueError:
                        raise ValueError("Rating must be a number between 0.0 and 5.0")
                else:
                    try: 
                        new_rating = float(new_rating)
                    except ValueError:
                        raise ValueError("Rating must be between 0.0 and 5.0")
                if not (0.0 <= new_rating <=5.0):
                    raise ValueError("Rating must be between 0.0 and 5.0")
                
                return new_rating

            except ValueError as e:
                print(e)
                new_rating=None   
                
    
    def simple_game_info(self):
        '''returns a simple form of the game info only including the name\
            and the rating as a tuple'''
        return (self._name, self.rating) 
    
    def __gt__(self, other):
        '''Defines greater than for a Game by using the rating values'''
        if isinstance(other, Game):
            return self.rating > other.rating
        raise TypeError(f"Cannot compare Game with {type(other).__name__}")
        
    def __eq__(self, other):
        '''Defines equivalence comparison for a Game
        by using the rating values'''
        if isinstance(other, Game):
            return self.rating == other.rating
        raise TypeError(f"Cannot compare Game with {type(other).__name__}")
                
    def __repr__(self):
        '''returns a string with a border above and bwloe for readability,
        the game, rating, and console played on with their respective values,
        and each comment in a bullet point format'''
        border = "~ "*12
        body = f"\n Game: {self._name}\n Rating: {self.rating}\n"\
        f" Console played on: {self.console}\n"
        rep_comments = ' Comments: \n'
        for item in self.comments:
            rep_comments += "\t-" + item +"\n"
        return border+body+rep_comments+border
        
        

if __name__=="__main__":
    
    #Test 1 : Create a game and test simple_game_info output
    g1 = Game(name="firewatch", rating=4.5,console="PC")
    assert g1.simple_game_info() == ("firewatch",4.5), "Test 1 failed, \
        info does not match input"
    print("Test 1 Passed!")

    # Test 2: Testing comparison using __gt__
    g2 = Game(name="mario", rating=3.0, console="Switch")
    assert g1 > g2, "Test 2 Failed: g1 should be rated higher than g2"
    print("Test 2 Passed!")
    
  