``The project represents the Flask REST API ``
    
The structure of the project --> 

DIRS:
- migrations --> ( i will need to use the alembic in order not to update db manually)
- mocking --> (script for filling the db with fake data)
- models --> (Sqlalchemy repr)
- rest --> ( Building the logic for CRUD)
- services --> ( The file which is used to query the db)
- static --> ( for swagger)
- tests

Files:
- travis.yaml
- app.py --> the initial app which is configured 
- database --> configuration

+ ReadMe, reqs.txt, docker, db

also i need to created the dashboard for tasks in trello/notion/jira


    Essential links:
    1) http://127.0.0.1:5000/swagger/
    2) http://127.0.0.1:5000/events/
    3) http://127.0.0.1:5000/tickets/
    4) http://127.0.0.1:5000/tickets/<id>

    ----------------------------------------------------------------------------------------------
    **You can easily run the app from docker using these commands**:
  
    git clone: ...
    sudo docker build . -t tech_task_2_UK -f ./Dockerfile
    sudo docker run -p 8000:8000 tech_task
    sudo docker image ls
    sudo docker ps
    
    For the preliminaril usage of the project open a new terminal session and use these commands:
    sudo netstat -ltnp
    curl -X GET "http://127.0.0.1:5000/events/" -H  "accept: */*"

    ----------------------------------------------------------------------------------------------
    Used stack:
    1) Flask
    2) SQLAlchemy
    3) Flask-SQLAlchemy
    4) Flask-RESTful
    5) Flask-RESTful-swagger
    6) Flask-RESTful-swagger-ui
    7) SQLite3 
    8) Alembic
    9) Docker
    10) Pytest / pytest-cov
    11) Travis CI
    12) Gunicorn
    13) Logging
    14) GIT
    ----------------------------------------------------------------------------------------------
    Note:

    1) I spent almost 2.5 hours solving the problem with the import files from .rest directory.
    so that i decided to write the api classes in the main app, if I had more time, would correct it.
    2) The http://127.0.0.1:5000/tickets/<id> endpoint is not working in swagger UI, but you can use it in the browser.


