# Rest Api of User and Their Activity Period
    This project helps the user to get the list of the users and their activites. 
    You can also populate and delete the dummy data of users and their activity.

## Steps to follow:
1. Navigate to ftl_hr directory.
2. Run python manage.py test
3. Run python manage.py runserver
4. Open your web browser or postman and enter http://127.0.0.1:8000/api/v1/useractivity/.
5. After sending the request you will recieve response.  

### Commands lists:
1. python manage.py test
    #### This command will run all the tests.
2. python manage.py populate_useractivity 
    #### This command will create 10 user and 5 activities for every user.
3. python manage.py populate_useractivity --user 15 --activity 2
    #### This command will create 15 user and 2 activities for every user
4. python manage.py delete_useractivity
    #### This command will delete all the data.
5. python manage.py runserver
    #### this command will start the server.
    
## Pythonanywhere link:
http://asahu.pythonanywhere.com/api/v1/useractivity/
