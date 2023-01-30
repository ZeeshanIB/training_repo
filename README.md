# Project Overview
This project is a simple web application using Flask and Flask-SQLAlchemy. The web app posts data to a PostgreSQL database and retrieves data from the same database. The web app image is built using Github Actions and pushed to DockerHub. A second Github Actions job starts a PostgreSQL container, pulls the web app image from DockerHub, and links the two containers.

## Prerequisites
Before you begin, make sure you have the following software installed on your local machine:
- Docker
- Docker Compose


## Clone the repository to your local machine:
```bash
git clone https://github.com/ZeeshanIB/training_repo.git
# Change into the project directory:
cd web-app
#Start the containers:
docker-compose up
```

Access the web app by visiting http://localhost:80/items/<id> in your web browser.
you can access or test the webapp using

- sending get request
    - curl http://localhost:80/items/<id> 
- sending post request

    - curl -X POST http://localhost:80/items -H "Content-Type: application/json" -d '{"title": <value>, "content": <value>}'
