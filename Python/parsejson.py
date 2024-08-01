import json
#Load the JSON file
with open('json-eg22.json', 'r') as file:
    data = json.load(file)
for book in data['library']:
    title = book['title']
    author = book['author']
    published_year = book['publishedYear']
    genres = ", ".join(book['genres'])
    available = book['available']    
    #print book details
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Published Year: {published_year}")
    print(f"Genres: {genres}")
    print(f"Available: {'Yes' if available else 'No'}")
    # newline
    print()  