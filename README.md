# StoryGlowBack-end

## Indices 📑
- Project Description
- Feature
- Technologies and Libraries Used
- Installation
- Developer
## Project Description 📖

The backend of the web application will be built using Django and Django REST Framework  to provide a RESTful API for managing digital books and chapters.

## Feature 📋

1. **CRUD for Users:**

Create: Register new users.
Read: Retrieve user profile and list users.
Update: Modify personal user information.
Delete: Delete a user account 

2**CRUD for Books:**

Create: Allow users to create new books.
Read: Retrieve book details and associated chapters.
Update: Modify the details of an existing book.
Delete: Delete a book, with cascading deletion of associated chapters.

3**CRUD for Chapters:**

Create: Add chapters to a specific book.
Read: Read chapter.
Update: Edit the content of an existing chapter.
Delete: Remove a chapter from a book.

4**CRUD Genres:**

Browse by Genres: Get books filtered by specific genre.
Search: Search books by title.



## Technologies and Libraries Used 🛠️

* Python 3.8 +
* Psycopg2 2.9.9
* pillow 10.4.0
* Django 5.1
* djangorestframework 3.15.2
* djangorestframework-simplejwt 5.3.1
* Python dotenv 1.0.1
* Postgres 

## Installation ⚙️

Follow these steps to set up the project in your local environment and get started.

### Instructions

1. **Create a fork of the repository**

   Open the [StoryGlowBack-end](https://github.com/Angelinabassano/StoryGlowBack-end) repository on GitHub and click the "Fork" button in the top right corner of the page. This will create a copy of the repository in your own GitHub account.


2. **Clone your forked repository**

   Open a Git Bash terminal and run the command with the link to your new repository:

```bash
# Clone
git clone Your URL
```

3. **Open PyCharm and open the file you just cloned**


4. **To start, create a virtual environment via the terminal and then activate it**

```bash
# Create the virtual environment
python -m venv .venv
# Activate the virtual environment
.venv\Scripts\activate
#And if needed, deactivate the virtual environment
.venv\Scripts\deactivate
```


5. **Install the dependencies**
```bash
# If you have the requirements file, install the dependencies
pip install -r requirements.txt
# If you don't have it, do this to generate a requirements.txt file at the root of the project
pip freeze > requirements.txt
```


6. **Create your .env file**

You should create this at the same level as your requirements and it will be used to connect to the database you can create locally. 
(There is a sample file where you can view the data you need to include)


7. **Create your branch and start working!**

```bash
# Create the branch
git checkout -b feature/nombreDeTuRama
```

## Developer 🖥️
[**Angelina Bassano**](https://github.com/Angelinabassano)

