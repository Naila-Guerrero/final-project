import os
import csv
from movie import Movie

# Global list for the movies
movies = []
 
AFFIRMATION = ("Yes", "Y", "y", "YES", "yes")
REFUTATION = ("No", "N", "NO", "n", "no")

def load_movies(file_name): #Takes the name of the file containing movie data
   global display_menu
   movie_file = str(file_name) #Converts the file name into a string for better formatting
   exists = os.path.exists(file_name)

   if exists is False: 
         print ("The catalog file", file_name, "is not found")
         confirmation = input ("\nDo you want to continue without loading a file (Yes/Y, No/N))? ")
         if confirmation in (REFUTATION):
            print ("The Movie Library System will not continue...")
            display_menu = False
         elif confirmation in (AFFIRMATION):
             print("The Movie Library System is opened without loading catalog")
     
   else:
     file_name = open(file_name, 'r')
     line = file_name.readline()
     while line != '':
         line = line.rstrip() 
         parts = line.split(',') # This splits the line into a list of value

         # Creates a list of Movie objects: 
         # Id, title, director, genre, availabilty, price, rental_count
         movie = Movie(int(parts[0]), parts[1], parts[2], int(parts[3]), parts[4], float(parts[5]), int(parts[6])) 

         movies.append (movie)

         line = file_name.readline()
     number_of_movies = len(movies)
     file_name.close()
     print(("The catalog file \"") + movie_file + "\" successfully loaded", number_of_movies, "movies to the Movie Library System")
   
   # Returns a list of the movie objects
   return movies

def save_movies(file_name,movies): # Saves the list of Movie objects to a CSV file. 
   number_of_movies = len(movies)

   str (file_name)
   f = open (file_name, 'w') 
   for item in movies:
      line = ''.join(str(item))
      f.write(str(item) + '\n')

   # number of movie lines written to file  
   return  number_of_movies

def print_menu(): # Displays the main menu and prompts the user for a valid choice.
   global selection
   print ("\nMovie Library - Main Menu")
   print ("=" * 25)

   print ("1) Search for Movies")
   print ("2) Rent a movie")
   print ("3) Return a movie")
   print ("4) Add a movie")
   print ("5) Remove a movie")
   print ("6) Update movie details")
   print ("7) List movies by genre")
   print ("8) Find popular movies")
   print ("9) Check availability by genre")
   print ("10) Display library summary")
   print ("0) Exit the system")
   selection = input("Enter your selection: ")
   print()

   return selection

def search_movies(movies,search_term): # Searches for movies that match the search term. 
   searching = search_term.upper()
   print ("Searching for \"" + search_term + "\" in title, director, or genre...")
   matched_movies = []
   for movie in movies:
      title = movie.get_title().upper()
      director = movie.get_director().upper()
      genre = movie.get_genre_name().upper()

      if searching in title or searching in director or searching in genre:
         matched_movies.append(movie)
   
   print_movies(matched_movies)
  
def find_movie_by_id(movies, movie_id): #Searches for movies that match the search term. 
   found_id = -1
   for movie in movies:
      if movie.get_id() == movie_id:
         movie_id = found_id 
   return found_id

def rent_movie(movies,movie_id): #Rents a movie by its ID if it is available.
   message = '' # Initializes the message
   found = False # Flag for while loop
   index = 0
   while  index < len(movies) and found != True: # while the index is lower than the amount of movies and the movie_id hasn't been found
      film = movies[index] 
      if film.get_id() == movie_id: #check if the current ID is in the list
         if film.get_availability() == True: # If it is and is available
            film.borrow_movie() #Change the availability to false
            message = f"'{film.get_title()}' rented successfully." 
            found = True 
         else: #If the availability is already false
            message = f"'{film.get_title()}' is already rented - cannot be rented again" 
            found = True
      else: # In case that the movie id is not found
            message = f'Movie with ID {movie_id} not found in library.'
      index += 1
   return message # Return the message depending on the result

def return_movie(movies, movie_id):  #Returns a rented movie by its ID.  Cannot return a movie that has not been rented.
   message = ''
   found = False
   index = 0
   while index <len(movies) and found != True: # while the index is lower than the amount of movies and the movie_id hasn't been found
      film = movies[index]
      if film.get_id() == movie_id:
         if film.get_availability() == False:
            film.return_movie() #Change the availability to True
            message = f"'{film.get_title()}' was returned successfully."
            found = True 
         else: #If the availability is already true
            message = f"'{film.get_title()}' was not rented - cannot be returned."
            found = True
      else: # In case that the movie id is not found
         message = f'Movie with ID {movie_id} not found in library.'
      index += 1
   return message

def add_movie(movies): #Adds a new movie to the library after prompting the user for details.  Cannot add a movie if a movie with that ID already exists in the list. 
   movie_id = int(input("Enter movie ID: "))

   film = find_movie_by_id(movies, movie_id)

   if film != -1:
      result = f"A movie with this ID {movie_id} already exists - cannot be added to the library"
   else:
      title = input("Enter title: ")
      director = input("Enter director: ")
      genre = get_genre()
      price = float(input("Enter price: "))
      new_movie = Movie(movie_id, title, director, genre, price = price)
      movies.append(new_movie)
      result = f"Movie '{title}' added successfully."
   return result # A string indicating the result of the add attempt. 

def remove_movie(movies): #Removes a movie from the library by its ID.  Cannot remove a movie if a movie with ID does not exist in the list. 
   movie_id = int(input("Enter the movie ID to remove: "))

   film = find_movie_by_id(movies, movie_id)

   if film == -1:
      result = f"Movie with ID {movie_id} does not exist."
   else:
      movies.remove(film)
      result = f"Movie '{film.get_title()}' has been removed from library successfully."
   return result #  A string indicating the result of the remove attempt. 

def update_movie_details(movies): # Updates the details of a movie by its ID.  Cannot edit a movie if a movie with ID does not exist in the list.
   movie_id = int(input("Enter the movie ID to update: "))
   movie = find_movie_by_id(movies, movie_id)
   if movie == -1:
      message ="Movie with this ID does not exist."
   else: 
      print("Leave a field blank to keep the current values.")
      new_title = input(f"Enter new title (current: {movie.get_title()}): ")
      if new_title != '':
         movie.set_title(new_title)

      new_director = input(f"Enter new director (current: {movie.get_director()}): ")
      if new_director != '':
         movie.set_director(new_director)

      genre_input = input(f"Enter new genre (current: {movie.get_genre()}) (Yes/Y, No/N))? ")
      if genre_input != '':
         if genre_input in AFFIRMATION:
            genre = get_genre()
            movie.set_genre(genre)

      price_input = input(f"Enter new price (current: {movie.get_price()}): ")
      if price_input != '':
         movie.set_price(float(price_input))

      rental_input = input(f"Enter new rental count (current: {movie.get_rental_count()}): ")
      if rental_input != '':
         movie.set_rental_count(int(rental_input))
      message = f"Movie with ID {movie_id}' is updated successfully"

   #A string indicating the result of the update attempt. 
   return message

def get_genre(): #Displays the genre codes and descriptions and prompts the user for a valid choice. 
   print()
   print('  Genres')
   for key, values in Movie.GENRE_NAMES.items():
      print(f'  {key}) {values}')
   genre = int(input('   Choose genre(0-9): '))
   #  The user's valid menu choice as a string. 
   return genre

def list_movies_by_genre(movies): # Lists all movies of a specified genre. Displays a list of movies in the specified genre, or no movies found 
   same_genre = []
   genre = get_genre()
   while genre not in Movie.GENRE_NAMES:
      print("Invalid Genre: Enter a valid genre (0-9)")
      genre = input('Choose genre(0-9): ')
   else: 
      for movie in movies:
         if movie.get_genre() == genre:
            same_genre.append(movie)
      print_movies(same_genre)

def check_availability_by_genre(movies): # Checks and displays the availability of movies in a specified genre. Displays a list of movies that are available in the specified genre
   same_available_genre = []
   genre = get_genre()
   while genre not in Movie.GENRE_NAMES:
      print("Invalid Genre: Enter a valid genre (0-9)")
      genre = input('Choose genre(0-9): ')
   else: 
      for movie in movies:
         if movie.get_genre() == genre:
            if movie.get_availability() == 'Available':
               same_available_genre.append(movie)
      print_movies(same_available_genre)
         
def display_library_summary(movies): #  Displays a summary of the library, including the total number of movies, number of available movies, and number of rented movies. 
   total_movies = len(movies)
   available_movies = []
   rented_movies = []

   for movie in movies:
      if movie.get_availability() == 'Available':
         available_movies.append(movie)
      else: 
         rented_movies.append(movie)

   total_available = len(available_movies)
   total_rented = len(rented_movies)

   print(f'{"Total movies":<16}:{total_movies:>6}')
   print(f'{"Available movies":<16}:{total_available:>6}')
   print(f'{"Rented movies":<16}:{total_rented:>6}')

def popular_movies(movies): #Displays all the movies that have a rental_count >= to the entered value
   rentals = int(input('Enter the minimum number of rentals for the movies you want to view: '))
   popular_films = []
   for movie in movies:
      if movie.get_rental_count() >= rentals:
         popular_films.append(movie)
   print_movies(popular_films)

def print_movies(movies): #  Prints a list of movies in a formatted table. 
   if len(movies) == 0:
      print('No movies found.')
   else:
      print(f'{'ID':<10}{'Title':<30}{'Director':<25}{'Genre':<12}{'Availability':<19}{'Price':<9}{'# Rentals':<9}')
      print('-'*113)
      for movie in movies:
         str_genre = Movie.GENRE_NAMES[movie.get_genre()]
         print(f'{movie.get_id():<10}{movie.get_title():<30}{movie.get_director():<25}{str_genre:<12}{movie.get_availability():<19}{movie.get_price():<9}{movie.get_rental_count():>9}')

def main ():
  global display_menu
  global file_name
  global movie_id
  movie_id = "0"
  display_menu = True
  file_name = input("Enter the movie catalog filename: ")

  load_movies (file_name)

  while display_menu is True:
   selection = print_menu ()
   match selection:
      case "1":
         search_term = input("Enter your search term: ")
         search_movies(movies, search_term)
      case "2":
         input_id = int(input('Enter the movie ID to rent: '))
         rent_result = rent_movie(movies,input_id)
         print(rent_result)
      case "3":
         input_id = int(input('Enter the movie ID to return: '))
         rent_result = return_movie(movies,input_id)
         print(rent_result)
      case "4":
         new_movie = add_movie(movies)
         print(new_movie)
      case "5":
         deleted_movie = remove_movie(movies)
         print(deleted_movie) 
      case "6":
         update = update_movie_details(movies)
         print(update)
      case "7":
         list_movies_by_genre(movies)
      case "8":
         popular_movies(movies)
      case "9":
         check_availability_by_genre(movies)
      case "10":
         display_library_summary(movies)
      case "0":
         user_input = input ("Would you like to update the catalog (Yes/Y, No/N))? ")
         if user_input in (AFFIRMATION):
            number_of_movies = save_movies (file_name, movies)
            print(f'{number_of_movies} movies have been written to Movie Catalog.')

         display_menu = False
  print ("Movie Library System Closed Successfully")
     

if __name__=="__main__":
   main () 