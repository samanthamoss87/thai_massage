# **Thai Siam Massage**
## Table of Contents
1. [User Experience](#user-experience)
    - [Goals](#goals)
    - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
2. [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Programs Used](#programs-used)
    - [Photo and Video](#photo-and-video)
    - [Icons](#icons)
3. [Features](#features)
    - [General Features](#general-features)
    - [All pages](#all-pages)
    - [Nav bar](#nav-bar)
    - [Footer](#footer)
    - [Banner](#home-page)
    - [Home Page](#home-page)
    - [Treatments](#treatments)
    - [Book Now](#book-now)
    - [Login](#login)
    - [Privacy Policy](#privacy-policy)
    - [Terms and Conditions](#terms-and-conditions)
4. [Future Implementations](#future-implementations)
5. [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Platforms](#platforms)
    - [Other Tools](#other-tools)
6. [Local Development & Deployment](#local-development--deployment)
    - [Local Development](#local-development)
        - [Local Preparation](#local-preparation)
        - [Local Instruction](#local-instruction)
    - [Github Deployment](#github-deployment)
        - [Github Preparation](#github-preparation)
        - [Github Instrucation](#github-instruction)
7. [Testing](#testing)
    - [Methods](#methods)
    - [Validation](#validation)
    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
8. [Bugs](#bugs)
    - [known bugs](#known-bugs)
    - [Fixed bugs](#fixed-bugs)
 
9. [Credits](#credits)
    - [Acknowledgement](#acknowledgement)
10. [Contact](#contact)


# Project 4 - Important Notes
For Project 4, I developed a Thai massage booking system using HTML, CSS, JavaScript, Django, and Bootstrap to create a seamless and interactive user experience. The website allows customers to book massage sessions, and cancel their appointments effortlessly. Django powers the backend, handling user data, appointments, and admin functionality. Bootstrap ensures the site is fully responsive and visually consistent across devices. Javascript handles sending emails, responsive navbar and time selections. This project not only demonstrates my ability to integrate multiple technologies but also provides a practical, real-world solution for managing bookings efficiently.


# Technologies used
## Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Page markup
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
    - Styling
- [Django](https://www.djangoproject.com/)
    - Project Backend
## Libraries 
- [Google Fonts](https://fonts.google.com/)
    - Font style
- [Bootstrap](https://getbootstrap.com/)
    - App Theme and Styling
## Platforms
- [Github](github.com)
    - Store the code remotely for deployment
- [Gitpod](gitpod.io)
    - Development environment for the project
- [Heroku](https://www.heroku.com/)
    - Deployment of the project


# Local Development & Deployment
## Local Development
### Local Preparation
**Requirements**
- IDE like [Visual Studio Code](https://code.visualstudio.com/download)
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

### Local Instruction
1. Clone the repository and go inside the folder
```
git clone https://github.com/samanthamoss87/thai_massage.git
```
2. Open your IDE and open the folder you just cloned
3. Change the database configuration of the app in thai_massage/settings.py
```
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / "db.sqlite3"
    }
}
```
4. Open the terminal and run these commands to create the database
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
5. Now run this command to run the website
```
python manage.py runserver
```
4. Enjoy the site

## Heroku Deployment
### Setting up your git repository
1. Create a new repository and clone it to your computer
2. Put all the files to the repository folder
3. Create a file called `.python-version` and add python version to it. eg. 3.12
4. Create a file called Procfile and add this to the file `web: gunicorn your-project-name.wsgi --log-file -`
5. Replace `your-project-name` to your project name eg. thai-massage
6. Now run these commands to upload the files to Github 
    - `git add .`
    - `git commit -m "your commit message"`
    - `git push`
7. Login to your [Heroku](https://www.heroku.com/) account
8. Create a new app and give it a name
9. Connect your github account from deployment method
10. Search and Select your repository
11. Click on Deploy
