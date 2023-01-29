# Project Overview
This project is a simple web application using Flask and Flask-SQLAlchemy. The web app posts data to a PostgreSQL database and retrieves data from the same database. The web app image is built using Github Actions and pushed to DockerHub. A second Github Actions job starts a PostgreSQL container, pulls the web app image from DockerHub, and links the two containers.

