# API-v1.2

An API created using Python, Django REST Framework and PostgreSQL to serve the frontend for the project AniLite (https://anilite.netlify.app/#/). 
Uses the public API provided by Kitsu for fetching data related to anime, characters and genres via a script that gets data based on the ID
numbers provided and saves it to a Postgres instance hosted on supabase. Equipped with full CRUD functionality for all the models, pagination
and file based caching, the API currently has 62 genres, 50 anime and 1438 characters. API deployed on Heroku and database deployed on supabase.

The docs (auto generated using Swagger) can be found at: https://anilite-api-v1.herokuapp.com/docs/

## Endpoints

The API includes the following endpoints (x can be anime, character or genre):

1. `{x}/` : For providing a list of requested data in paginated format
2. `{x}/create` : For sending POST requests to create new data
3. `{x}/{slug}` : For accessing the details of a particular resource
4. `{x}/{slug}/update` : For updating a particular resource
5. `{x}/{slug}/delete` : For deleting a particular resource
  
## Query Parameters
  
- The `anime/` endpoint has the following query parameters:
  1. `?startswith={value}`: Used to show the anime whose names start with the provided value
  2. `?includes={value}`: Used to search for available anime names including the provided value
  3. `?sort={value}`: Used to sort available anime based on any of the available fields (like the airing date, number of episodes, ranking etc.)
  4. `?genre={value}`: Used to filter available anime based on the genre provided
  5. `?type={value}`: Used to filter anime based on whether it's a series, movie or OVA/ONA

- The `character/` endpoint has the following query parameters:
  1. `?startswith={value}`: Used to show characters whose names start with the value provided
  2. `?includes={value}`: Used to search for available characters whose names include the provided value
  3. `?sort={value}`: Used to sort the available characters on the bases of any of the available fields

## Future prospects

Currently working on implementing an authentication system using JWT web tokens and Google OAuth, will be followed by the addition of anime streaming
links and much more.
  
