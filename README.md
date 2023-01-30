# Project Overview
This project is a simple web application using Flask and Flask-SQLAlchemy. The web app posts data to a PostgreSQL database and retrieves data from the same database. The web app image is built using Github Actions and pushed to DockerHub. A second Github Actions job starts a PostgreSQL container, pulls the web app image from DockerHub, and links the two containers.

## Prerequisites
Before you begin, make sure you have the following software installed on your local machine:
- Docker
- Docker Compose

## Setting up the project
1. Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/<your-username>/<your-repo>.git
2. Change into the project directory:
bash
Copy code
cd <your-repo>
3. Start the containers:
Copy code
docker-compose up
Access the web app by visiting http://localhost:80 in your web browser.

