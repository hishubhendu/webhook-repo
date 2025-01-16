# webhook-repo
This will contain the Flask application, which acts as the webhook receiver, processing incoming GitHub actions and storing them in MongoDB.


Overview

This project is built using a backend-focused tech stack, aiming to provide efficient and scalable solutions. As a backend developer, the focus has been entirely on server-side technologies without the use of frontend frameworks like JavaScript or HTML.

Tech Stack

Backend

Python: The core programming language used for developing the backend logic.

Flask: A lightweight WSGI web application framework in Python, chosen for its simplicity and flexibility.

MongoDB: A NoSQL database used to store and manage the application's data efficiently.

Not Included

JavaScript: No client-side scripting was implemented as the focus is on backend development.

HTML: No frontend templates or static HTML pages were created.

Features

API development using Flask for handling HTTP requests and responses.

Data management using MongoDB for a flexible and scalable database solution.

Getting Started

Prerequisites

Python 3.x

Flask

MongoDB

Installation

Clone the repository:

git clone <repository-url>

Navigate to the project directory:

cd <project-directory>

Install the required Python packages:

pip install -r requirements.txt

Start the Flask application:

flask run

Configuration

Ensure MongoDB is running on your local machine or update the database connection string in the configuration file.


License

This project is licensed under the MIT License. See the LICENSE file for details.