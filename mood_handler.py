from difflib import get_close_matches

#Create a dictionary to map basic moods to appropriate genres
moodToGenre = {
    'happy' : ['Comedy', 'Adventure', 'Family', 'Animation'],
    'sad' : ['Drama', 'Romance'], 
    'excited' : ['Thriller', 'Horror', 'Action', 'Crime'],
    'angry' : ['Action', 'Thriller'],
    'curious' : ['Sci-Fi', 'Suspense', 'Thriller', 'Crime', 'Fantasy'],
    'reflective' : ['Biography', 'History', 'Drama', 'Classic', 'Documentary'],
    'adventurous' : ['Adventure', 'Action', 'Sci-Fi', 'Fantasy'],
    'nostalgic' : ['Classic', 'Animation', 'Children', 'Family'],
    'romantic' : ['Romance', 'Love'],
    'emotional' : ['Drama', 'Romance']
}


#Create a dictionary to map mood synonyms to base moods
synonymToBaseMood = {
    'joyful' : 'happy',
    'cheerful' : 'happy',
    'delighted' : 'happy',
    'elated' : 'happy',
    'pleasant' : 'happy',
    'peppy' : 'happy',
    'depressed' : 'sad',
    'unhappy' : 'sad',
    'sorrowful' : 'sad',
    'distressed' : 'sad',
    'eager' : 'excited',
    'enthusiastic' : 'excited',
    'thrilled' : 'excited',
    'nervous' : 'excited',
    'charged' : 'excited',
    'annoyed' : 'angry',
    'furious' : 'angry',
    'irritated' : 'angry',
    'mad' : 'angry',
    'pissed' : 'angry',
    'meditative' : 'reflective',
    'studious' : 'reflective',
    'speculative' : 'reflective',
    'thoughtful' : 'reflective',
    'bold' : 'adventurous',
    'brave' : 'adventurous',
    'courageous' : 'adventurous',
    'passionate' : 'romantic',
    'corny' : 'romantic',
    'dreamy' : 'romantic',
    'erotic' : 'romantic',
    'whimsical' : 'romantic',
    'loving' : 'romantic',
    'hysterical' : 'emotional',
    'sentimental' : 'emotional',
    'sensitive' : 'emotional',
    'disturbed' : 'emotional'
}


#Get close matches of the given mood
def getCloseMoodMatches(mood):
    allMoods = list(moodToGenre.keys()) + list(synonymToBaseMood.keys())
    closeMatch = get_close_matches(mood, allMoods, n=1, cutoff=0.6)
    return closeMatch

#Define a function that fetches the list of genres for the given mood
def GetGenreFromMood(mood):
    mood = mood.lower()
    if mood in moodToGenre:
        return moodToGenre[mood]
    elif mood in synonymToBaseMood:
        baseMood = synonymToBaseMood[mood]
        return moodToGenre[baseMood]
    else:
        closeMatch = getCloseMoodMatches(mood)
        if len(closeMatch) != 0:
            print(f"Did you mean '{closeMatch[0].title()}?'")
            return GetGenreFromMood(closeMatch[0])
        else:
            return 0
