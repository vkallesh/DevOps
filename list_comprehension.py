#!/usr/bin/python -v

#list comprehension example with and without

movies = ['star wars', 'Gandhi', 'casablanca', 'Gone with the wind']

#Normal approach

#Movies startswith G
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)
