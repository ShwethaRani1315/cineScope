import pandas as pd
from mood_handler import GetGenreFromMood, moodToGenre
from movie_filter import getMoviesByGenre, getMoviesByKeyword, getMoviesByReleaseYear, getRandomMovies
from file_loader import loadMovies
from save_favorites import saveFavorites


#Main function
def main():
    cont = True
    
    while(cont):

        #Create a new dataframe to store the clean movies data
        movies_df = loadMovies()

        if(movies_df is not None):
            
            print("Welcome to CineScope! 🎬")
            print("How would you like your movie recommendations today?")

            print("\n1. Based on your mood")
            print("2. Based on genres")
            print("3. Based on keyword")
            print("4. Based on release year")
            print("5. Surprise me! (Random picks)")
            print("6. Exit")

            choice = input("\nEnter menu option to proceed: ")

            if choice == '1':
                user_mood = input("What's your mood right now? (You can type 'exit' to Exit)").strip()
                if user_mood.lower() == "exit":
                    break
                else:
                    genres = GetGenreFromMood(user_mood)
                    recommendations = getMoviesByGenre(genres, movies_df)

            elif choice == '2':
                user_genres = input("What are your preferred genre(s)? (Comma-seperated if multiple)")
                genres = [g.strip().capitalize() for g in user_genres.split(',')]
                recommendations = getMoviesByGenre(genres, movies_df)

            elif choice == '3':
                keyword = input("Enter a keyword to search from movie names and directors: (love, music, Frank, etc.)")
                recommendations = getMoviesByKeyword(keyword, movies_df)

            elif choice == '4':
                try:
                    year = int(input("Enter the year of release: "))
                except ValueError:
                    print("⚠️ Please enter a valid numeric year.")
                    continue
 
                recommendations = getMoviesByReleaseYear(year, movies_df)

            elif choice == '5':
                try:
                    count = input("How many random movies do you want?").strip()
                    count = int(count) if count else 3
                except ValueError:
                    print("Invalid number! Showing 3 movies by default!")
                    count = 3
                
                recommendations = getRandomMovies(count, movies_df)

            elif choice == '6':
                print("Thanks for using CineScope! See you later!")
                break

            #Sort the recommended movies to display the top rated movies
            recommendations = recommendations.sort_values(by='rating', ascending=False).reset_index(drop=True)

            #Formatting the output
            if not recommendations.empty:
                print("🎬 Top Movie Picks for You 🎬\n")
                for idx, row in recommendations.iterrows():
                    print(f"{idx + 1}. 🎞️  {row['title']}")
                    print(f"   📂 Genre(s): {row['genre']}")
                    print(f"   ⭐ IMDb Rating: {row['rating']}\n")

                save = input("\nDo you want to save these recommendations to your favorites? (y/n)")

                if save.strip().lower() == 'y':
                    saveFavorites(recommendations)

            else:
                print("Oops! 😕 Couldn't find any movies matching your criteria. Try a different input!")

        else:
            print("Cannot load movies dataset!")

        #Option to display the menu and process recommendations again
        user_cont = input("Do you want to try again? (y/n)")
        cont = user_cont.strip().lower() == 'y'
            

        

if __name__ == "__main__":
    main()