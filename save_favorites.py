import os

def saveFavorites(recommendations):
    if recommendations is None:
        print("No data available to save!")
        return
    
    try:
        fileName = input("Enter your preferred file name: (default: myFavorites.csv)")
        fileName = fileName.strip() if fileName else "myFavorites.csv"
    
    except ValueError:
        print("No valid file name found! Defaulting to 'myFavorites.csv'")
        fileName = 'myFavorites.csv'

    file_exists = os.path.isfile(fileName)

    recommendations.to_csv(f"{fileName}", 
                           columns = ['title' ,'release_year', 'genre'], 
                           mode = 'a', 
                           index = False,
                           header = not file_exists)
    
    print("Movies successfully added to your favorites!")
