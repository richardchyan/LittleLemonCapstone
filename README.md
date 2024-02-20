Endpoints for homepage, menu, single menu items, bookings and table information, user registrations: 

/restaurant

/restaurant/menu 

/restaurant/menu/<int:pk>

/restaurant/booking/tables (requires authentication)

/auth/users (requires authentication)

/auth/token/login (Request a token)

Create an SQL database and change the name in the settings.py file to whatever you name the database. Default database name I've set is 
"littlelemon2". 

To authenticate to see booked tables and list of registered users, create a superuser and create a token in the admin panel, or request a token
using Djoser's /auth/token/login endpoint, along with your username and password, which will return a token for authentication

