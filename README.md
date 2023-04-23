# Photo Gallery RESTful API
This is a Python project built using the Flask web framework. The goal of this project is to create a photo gallery API that can perform CRUD (Create, Read, Update, Delete) operations on a collection of photos. This is a clone clone of my API created with Node.js and Express

# Getting Started
## Prerequisites
Python 3
Flask
Flask-CORS

## Installing
Clone this repository to your local machine.
Install the required packages by running the following command:
### `pip install Flask Flask-CORS`

## Running the Application
1. Navigate to the root directory of the application.
2. Start the Flask development server by running the following command:
### `python app.py`
The server should now be running on http://localhost:3002.

## API Endpoints
The following API endpoints are available:

GET	/	Returns a welcome message.
GET	/photos	Returns all photos.
GET	/photos/{id}	Returns a specific photo by ID.
POST	/photos	Adds a new photo to the collection.
PUT	/photos/{id}	Updates a specific photo by ID.
DELETE	/photos/{id}	Deletes a specific photo by ID.

## Built With
Flask - A micro web framework written in Python.
Flask-CORS - A Flask extension for handling Cross-Origin Resource Sharing (CORS).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
