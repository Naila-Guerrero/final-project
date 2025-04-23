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
      f.write(item + '\n')

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

   return selection

def search_movies(movies,search_term): # Searches for movies that match the search term. 
   item_found = False
   title_printed = False
   search_term = input("Enter your search term: ")
   searching = search_term.upper()
   print ("Searching for \"" + search_term + "\" in title, director, or genre...")

   
   for item in movies:
     movie_instance = item.split (",")
     translated_genre = Movie.get_genre_name(movie_instance[3])
     translated_rent = Movie.get_availability(movie_instance[4])
    
     
     for attribute in movie_instance:
       attribute_search = attribute.upper()
       search = attribute_search.find(searching)

       if search > -1:
         if title_printed is False:
            print(format("ID", "<5"),format ("Title", "<25"),format("Director", "<20"),\
            format("Genre","<12"),format("Availability","<15"),format("Price",">7"), format("# Rentals",">15"))
            print("-" * 105)
            title_printed = True
             
         item_found = True
         print(format(movie_instance[0], "<5"),format (movie_instance[1], "<25"),format(movie_instance[2], "<20"),\
              format(translated_genre,"<12"),format(translated_rent,"<12"),format(movie_instance[5],">10"), format(movie_instance[6],">15"))
      
     else:
       pass
     
   if item_found is False: 
    print("No matching movies found")
   
def find_movie_by_id(movies, movie_id): #Searches for movies that match the search term. 
   id_search = movie_id
   for item in movies:
     movie_instance = item.split (",")
     
     for attribute in movie_instance:
      id_number = attribute.find(id_search[0])
      if id_number > -1:
         movie_id = movie_instance
      else:
         movie_id = id_number  
      
   return movie_id # the matched Movie object or 1 if not found

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
         search_movies(movies, search_term = '')
      case "2":
         input_id = int(input('Enter the movie ID to rent: '))
         rent_result = rent_movie(movies,input_id)
         print(rent_result)
      case "3":
         input_id = int(input('Enter the movie ID to return: '))
         rent_result = return_movie(movies,input_id)
         print(rent_result)
      case "4":
         pass
      case "5":
         pass
      case "6":
         pass
      case "7":
         pass
      case "8":
         pass
      case "9":
         pass
      case "10":
         pass
      case "0":
         user_input = input ("Would you like to update the catalog (Yes/Y, No/N))? ")
         if user_input in (AFFIRMATION):
            save_movies (file_name, movies)
         display_menu = False



  print ("Movie Library System Closed Successfully")
     





if __name__=="__main__":
   main () 