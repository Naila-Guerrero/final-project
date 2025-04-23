# Create the class called movies
class Movie: 
    GENRE_NAMES = {
        0: 'Action', 1:'Comedy', 2:'Drama', 3:'Horror',
        4: 'Sci-fi', 5:'Romance', 6:'Thriller', 7:'Animation', # Animation is not a genre! Is a medium to tell stories
        8: 'Documentary', 9:'Fantasy'    
    }


    def __init__(self, id, title, director, genre, available = True, price = 0.0, rental_count = 0 ): #Initialize attributes, and make 'available', 'price' and 'rental_count' optional 
        self.__id = id
        self.__title = title 
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__rental_count = rental_count


# Standard getters 
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_director(self):
        return self.__director
    
    def get_genre(self):
        return self.__genre
    
    def get_available(self):
        return self.__available
    
    def get_price(self):
        return self.__price
    
    def get_rental_count(self):
        return self.__rental_count
    
# an additional getter method that retuns the name of the genre as a string
    def get_genre_name(self):
        for key,value in Movie.GENRE_NAMES.items():
            if key == self.__genre:
                return value
            
# Displays a message depending on the availabity of the movie         
    def get_availability(self):
        if self.__available == True:
            message = 'Available'
        else:
            message = 'Rented'
        return message


# setters except for available and rental count
    def set_id(self,id):
        self.__id = id
    
    def set_title(self, title):
        self.__title = title
    
    def set_director(self, director):
        self.__director = director

    def set_genre(self,genre):
        self.__genre = genre

    def set_price(self,price):
        self.__price = price

# When borrowing a movie, it sets its available attribute to False and increases the rental count attribute by 1. 
    def borrow_movie(self):
        if self.__available == True:
            self.__available = False
            self.__rental_count += 1

    def return_movie(self):
        if self.__available == False:
            self.__available = True        

    def __str__(self):
        movie_str = f'{self.__id:<10}{self.__title:<30}{self.__director:<25}{self.get_genre_name():<12}{self.get_availability():<19}{self.__price:<9}{self.__rental_count:<9}'
        return movie_str