import os
import csv
movies = []

AFFIRMATION = ("Yes", "Y")
REFUTATION = ("No", "N")

def get_availability(available):
   if available == "True":
      available = "Available"
   elif available == "False":
      available = "Rented"
   return available

def get_genre_name (genre):
   match genre:
      case "0":
         genre = "Action"
      case "1":
         genre = "Comedy"
      case "2":
         genre = "Drama"
      case "3":
         genre = "Horror"
      case "4":
         genre = "Sci-Fi"
      case "5":
         genre = "Romance"
      case "6":
         genre = "Thriller"
      case "7":
         genre = "Animation"
      case "8":
         genre = "Documentary"
      case "9":
         genre = "Fantasy" 
   
   return genre
 


def search_movies(movies,search_term):
   item_found = False
   title_printed = False
   search_term = input("Enter your search term: ")
   searching = search_term.upper()
   print ("Searching for \"" + search_term + "\" in title, director, or genre...")

   
   for item in movies:
     movie_instance = item.split (",")
     translated_genre = get_genre_name(movie_instance[3])
     translated_rent = get_availability(movie_instance[4])
    
     
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
   




def load_movies(file_name):
 movie_file = str(file_name)
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
          movies.append (line)
          line = file_name.readline()
     number_of_movies = len(movies)
     file_name.close()
     print(("The catalog file \"") + movie_file + "\" successfully loaded", number_of_movies, "movies to the Movie Library System")



def save_movies(file_name,movies):
 number_of_movies = len(movies)

 str (file_name)
 f = open (file_name, 'w') 
 for item in movies:
    line = ''.join(str(item))
    f.write(item + '\n')  
 print (number_of_movies, "movies have ben written to Movie catalog.")   
 

def print_menu():
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


def main ():
  global display_menu
  global file_name
  display_menu = True
  file_name = input("Enter the movie catalog filename: ")

  load_movies (file_name)
  while display_menu is True:
    print_menu ()
    match selection:
       case "1":
          search_movies(movies, search_term = '')
       case "2":
          pass
       case "3":
          pass
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