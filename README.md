# SLAB API

This API allows you to organize projects and their tasks. You can create, delete, update, get projects, all of this operations can also performed over theirs tasks.

This API implements [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) (JSON WEB TOKEN) that's why you must be first registered and after logged in order to get a Token that allows you to do request to API.

## Installation

In order to start using this API you must install `Python 3.8.5` and `MySQL 5.7`. (These were the versions used in develop).

Now, follow this steps:

1. Choose a place in your computer and clone this repository. Type in your terminal:

```
$ git clone https://github.com/cristian-bedoya/API_SLAB_Assessment.git
```

2. Once the repository has been downloaded, enter to it and create a python virtual enviroment. (This step is not required but it is highly recomended).

```
$ cd API_SLAB_Assessment
$ python3 -m venv env

```

The above command will create a folder called `env`.

> Make suere to use the right Python version at time of creating the virtual enviroment. 3. Install the requirements needed to run the API in the enviroment.

```
$ . ./env/bin/activate
$ pip install -r requirements.txt
```

4. Configure the database.

This API uses a MySQL database, the reason why you must configure one. For this it's included in this repository a file called `setup_db.sql` which will help you to do it easily. So in your terminal type:

```
$ cat setup_db.sql | mysql -uroot -p
```

Once you run the above command you must enter the passoword and wether all of it was OK the database should be created.

> You can change database name, username and password, to do so, modify the `setup_db.sql` file before runnig the above command.

5. Configure enviroment variables. The following variables will be used to run the API

```
DB_NAME    ----> database name
DB_USER    ----> username who has permisions over the database
DB_PWD     ----> database password
DB_HOST    ----> IP where the database is hosted.
SECRET_KEY ----> You can configure.
```

6. Prepare migrations to thedatabse (at the same time set the new screct key)

```
DB_NAME=db_slab DB_USER=user_slab DB_PASSWORD=pswd_slab DB_HOST=localhost DB_PORT=3306 KEY_SECRET='key_api_slab' ./manage.py makemigrations
```

7. Migrate tables

```
DB_NAME=db_slab DB_USER=user_slab DB_PASSWORD=pswd_slab DB_HOST=localhost DB_PORT=3306 KEY_SECRET='key_api_slab' ./manage.py migrate

```

## Usage

After setup proccess above the API is ready to be executed. In order to do it you only to need to execute below command in your terminal:

```
DB_NAME=db_slab DB_USER=user_slab DB_PASSWORD=pswd_slab DB_HOST=localhost DB_PORT=3306 KEY_SECRET='key_api_slab' ./manage.py runserver
```

> Change the enviroment variables if you modified the `setup_db.sql` file.

Now, the API is running in the 8000 port ready to receive requests. For this is good a idea to use a client like `Postman`.

#### List of endpoints:

Projects:

```
* GET    api/projects           List projects
* POST   api/projects           Create a new project
* PUT    api/projects/{id}      Update a prject by ID
* DELETE api/projects/{id}      Delete a project by ID
* PATCH  api/projects/{id}      Update partially a project by ID
```

Tasks:

```
* GET    /api/tasks        List of all task from project by ID
* POST   /api/tasks        Append a new task to a project by ID
* DELETE /api/tasks/{id}   Delete a task by ID from a project by ID
* PUT    /api/tasks/{id}   Update the task by ID from project by ID
* PATCH  /api/tasks/{id}   Update partially task by ID from a project by ID
```

Users:

```
* POST user/signup   Register a new user
* POST user/login    Login a user already registered.
```

#### Look at this example:

[Youtube Video Example](https://www.youtube.com/watch?v=kNA0Z6884Jg)

## Support

If you have any problem executing this AP, please do not hesitate to contact me at [Twitter](https://twitter.com/crisbedbla)https://github.com/cristian-bedoya/API_SLAB_Assessment.git

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

#### Cristian Bedoya
