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
    - [Data Schema](#data-schema)
3. [Features](#features)
    - [General Features](#general-features)
    - [All pages](#all-pages)
    - [Nav bar](#nav-bar)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [Treatments](#treatments)
    - [Book Now](#book-now)
    - [Login](#login)
    - [Dashboard](#dashboard)
    - [Booking Success](#booking-success)
    - [Contact](#contact)
4. [Future Implementations](#future-implementations)
    - [Calendar View](#main-dashboard-calendar-view)
    - [New Appointment Window (Modal/Popup)](#new-appointment-window-modalpopup)
    - [Customer Wallet](#customer-wallet)
5. [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Platforms](#platforms)
    - [Other Tools](#other-tools)
6. [Local Development & Deployment](#local-development--deployment)
    - [Local Development](#local-development)
        - [Local Preparation](#local-preparation)
        - [Local Instruction](#local-instruction)
    - [Heroku Deployment](#heroku-deployment)
        - [Repository Setup](#setting-up-your-git-repository)
        - [Heroku Setup](#setting-up-the-heroku-app)
7. [Testing](#testing)
    - [Methods](#methods)
    - [Validation](#validation)
    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
8. [Bugs](#bugs)
    - [known bugs](#known-bugs)
 
9. [Credits](#credits)
    - [Acknowledgement](#acknowledgement)
10. [Contact](#contact)


# Project 4 - Important Notes
For Project 4, I developed a booking system for a Thai Massage business, using HTML, CSS, JavaScript, Django, and Bootstrap. The site/system was designed to create a seamless and interactive user experience. The website allows customers to book and cancel appointments effortlessly. Django was utilised to powers the backend, handling user data, appointments bookings, deal withand administration functionality. Bootstrap ensures the site is fully responsive and visually consistent across various device types. Javascript handles sending emails, responsive navbar and time selections. This project not only demonstrates my ability to integrate multiple technologies but also provides a practical, real-world solution for managing bookings efficiently for a real business who upon completion/grading for this project, will utilise this booking system and look to have me build on these functionalities in the future.

# User experience
## Goals
### Visitor Goals
- Visitors who want to have best quality Thai massage can easily understand the range of massage services available .
- Visitors who have an interest in massage can identify the service they require and make a appointment/booking. 
- Visitors can manage their bookings, cancel appointments if necessary or make new/additional bookings
- Visitors can create user accounts easily, login to make, cancel or check any bookings/appointments they may have.
- Visitors upon making a booking can view their bookings on the booking dashboard
- Visitors making a booking encounter a message advising their booking was successful with a link to view the bookings Dashboard.
- Visitors can user the contact form to leave a message for Thai Massage team



### User goals are
- View /navigate the site and obtain information easily.
- Get information on the different types of massages available
- Contact the business via a number of different methods, phone, contact us and make a booking
- Make a booking for a massage treatment
- Cancel future bookings



### Business Goals
- Display and highlight the massage services available
- Get an understanding about the cost and duration of various types of treatment
- Get people to contact us to get more information.
- Gain more customer bookings to grow the businesss.
- The Massage business would like to grow and expand its business by taking bookings online via my booking portal.
- The Massage business would like to increase sales when phone lines are busy and by allowing customers to make out of hours bookings.



### User Stories

<div align="center"> 
    <img src="readme-images/user-story.png" alt="index mock up">
</div> 

- As a potential customer, I would like to see what relevant experiences the massage business can offer in my area.
- I would like to see what types of therapy the massage business offers and specialises in.
- As a customer looking at optimising the business's profitability and Growth iI would like to see what type of massage therapies are offered throughout my business.
- While visiting a massage therapy website, I want to Navigate through their different types of  treatments seamlessly and have a direct link to contact them. 
- I want to be able to contact the therapist with direct open-ended questions via a Contact us form.
- I want to be able to review the site and get the detail I need easily without reading huge amount of text.
- As a user I want to be able to use the site wherever I am in on any type/form of device and encounter an easy  way to navigate, find the information easily and make bookings in a time efficient manor. 
- I would like book sessions from the website with different types of therapy, dates and times.
- I would like to cancel any future scheduled appointments.



# Design
## Colour Scheme
<div align="center"> 
    <img src="readme-images/color-palatte.png" alt="Colour Palatte">
</div> 

- #000000 was used in all the font text
- #198754 was used as the main colour such as Footer Background, Button Text, Border and background
- #ffc800 was used as the hover colour of the navbar links
- #FFFFFF was the main background on all ages


## Typography

<div align="center"> 
    <img src="readme-images/typography.png" alt="Font Style">
</div>

- My primary font is [Poppins](https://fonts.google.com/specimen/Poppins?query=poppins) which is on all pages of the website
- I used Poppins font as it is clear for everyone to read, whilst also having a great style look for a Massage business


## Imagery
<div align="center"> 
    <img src="readme-images/imagery.png" alt="Imagery">
</div> 

- These are the photos I used for my website that all are copyright free.
- I researched hundreds of photos to get the best image to represent the relevant area of my business.
- They matched in line with the Businesses and the sectors we are working within.



## Programs Used
These are the programs I used to resize and convert the image to increase the performance of the site for mobile and desktop usage.


- [Link to simple imager resizer](https://www.simpleimageresizer.com/)
- [Link to tiny png](https://tinypng.com/)
- [Link to free convert](https://www.freeconvert.com/)
- [Link to Data Diagram](https://www.quickdatabasediagrams.com/)

## Data Schema

<div align="center"> 
    <img src="readme-images/data_schema.png" alt="Data Schema">
</div>

In the application there are 4 major tables which is Treatment, Booking, UserProfile and Contact. 

Contact table is individual. But Treatment is related to the booking table and also there is relation between the booking table and the userprofile so that the user can track their own bookings.



# Features
## General features
### All pages
## Nav Bar
<div align="center"> 
    <img src="readme-images/nav-desktop.png" alt="Nav bar">
</div> 

- This Nav bar is on all pages with the minimal design. 
- This Nav bar is fixed in place, so when you scroll down you can still access all pages.
- If you click on the logo, it will take you back to the home page. 
- Project 4 - There is now 5 pages, as there is a dashboard page added for the user to get more booking table of the future bookings

<div align="center"> 
    <img src="readme-images/nav-mobile.png" alt="Nav bar in phone format">
</div> 

- This is the look of the nav bar in the format of a phone
- I wanted it to look sleeker and user friendly in the style.
- Anything below 768px will show this format by using media queries. 

<div align="center"> 
    <img src="readme-images/nav-mobile-expand.png" alt="Nav hamburger">
</div> 

- This is the look of the Hamburger Nav.
- When you click on the Menu Button it brings the Nav list up.
- If you click on the logo, it will take you back to the home page.

## Footer
<div align="center"> 
    <img src="readme-images/footer-desktop.png" alt="Footer">
</div> 

- This footer is also accessible on all pages.
- The footer also holds the Privacy Policy and Terms and Conditions but those are not working. You have to add you own terms and conditions and privacy policies.
- The is aligned into the middle of the screen and always white in colour.
-  Project 4 - Twitter, Facebook, and LinkedIn social links added but they are not functional.


<div align="center"> 
    <img src="readme-images/footer-mobile.png" alt="Footer in phone format">
</div> 

- This is what the phone looks like in the phone format.
- Anything below 768px will show this format using media queries.


## Home Page
<div align="center"> 
    <img src="readme-images/hero-banner.png" alt="Home page banner">
</div> 

- This is my main page Hero, I wanted to make it eye catching, stylish, easy to read, easy to navigate, while also been user friendly.
- With hours of research I thought this image was the best way to convey the type of my business.

<div align="center"> 
    <img src="readme-images/welcome-section.png" alt="Welcome Section">
</div> 

- I added this text to make the front page be attractive to the eye, whilst also been business specific.
- Knowing that there is no background image, I wanted to add text to it to draw people in.


<div align="center"> 
    <img src="readme-images/visit-us.png" alt="Our Information">
</div> 

- Project 4 - I created a section where people can find our place easily.
- It gives the end user another direct link into the Booking page.


## Treatments
<div align="center"> 
    <img src="readme-images/treatment-page.png" alt="treatment page">
</div> 

- All the treatments with title, description, price and duration are visible
- It gives the end user another direct link into the Booking page.


## Book now
<div align="center"> 
    <img src="readme-images/book-now.png" alt="Booking page">
</div> 

- Treatment booking form where user have to select treatment type, treatment duration, time and date to book a schedule
- User must have to be a registered user of Thai Siam Massage and have to login first to book a treatment.


## Login
<div align="center"> 
    <img src="readme-images/login.png" alt="Login page">
</div> 

- Customer login page where user has to provide email and password to login.
- User must have to be a registered user of Thai Siam Massage to login
- There is a direct link to the register page if user is not registered



## Dashboard
<div align="center"> 
    <img src="readme-images/dashboard.png" alt="Dashboard">
</div> 

- After login user will redirected to the dashboard page
- Future bookings of the user are displayed within a table
- User can cancel any booking anytime with the cancel button


## Booking Success
<div align="center"> 
    <img src="readme-images/booking-success.png" alt="Booking Success">
</div> 

- After booking a schedule user will redirect to the booking success page
- Direct link for user to navigate to the dashboard


## Contact
<div align="center"> 
    <img src="readme-images/contact-form.png" alt="Contact us">
</div> 

- User can send us messages through this form that will be saved to the database
- User's message will send to the owner's email



## Future Implementations
### Reset Password
- If user forgot Username or password, user can reset their passwords through links from email

### Main Dashboard (Calendar View)
- Time Slots: Start: 09:00 AM | End: 10:00 PM
- Supports appointments on Hour, 30 mins, 15 mins
- Drag and Drop for easy rescheduling
- Colour-coded Gant-chart dashboard with each therapist displayed in a different colour and or column, type of massage, or status
- Appointment Slots:
    - Click on a time slot to open the New Appointment Window
    - Neutral colour slots can be used as labels/comments


### New Appointment Window (Modal/Popup)

- Customer Details
    - Name (Text Field)
    - Phone Numbers (Multiple Supported)
    - Duration (Dropdown: 15/30/45/60 mins, etc.)
    - Therapist Requested? (Checkbox)

- Massage Details
    - Type of Massage (Dropdown)
    - Colour Selection (15 colours)
    - Repeat Appointment (Checkbox + Frequency Selector)



- Pricing & Payment
    - Automated Cost Calculation (Editable Field)
    - Payment Received? (Checkbox for money tracking)
    - Customer Wallet Payment Methods:
        - Viva | Cash | Revolut | Voucher

- Refund Button with Comments
- Reminders & Confirmation
- Send Confirmation? (Yes/No Toggle)
- Comments & Notes
- Visible Comments:
    - Massage Type, Therapist Requested, Phone Number


- Hidden Comments (Double Click to Access):
    - Credit Balance/Vouchers & Prepayments
    - Cancellation Debt (Red), Positive Balance (Green), Credit (Orange)


### Customer Wallet
- Balance Tracking
    - Displays remaining balance
    - Funds can be loaded via Viva, Cash, Revolut, Voucher
    - Refund option available


- Voucher Wallet
    - Unique Voucher Numbers
    - Payment via Viva, Cash, Revolut
    - Balance Auto-Deducted on use
    - Option to Transfer Voucher Balance to Customer Wallet


- Cash Payments
    - Separate tracking for two cash boxes



# Technologies used
## Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Page markup
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
    - Styling
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Fronted behaviour control
- [Python](https://www.python.org/)
    - Project Backend Language

## Libraries 
- [Google Fonts](https://fonts.google.com/)
    - Font style
- [Bootstrap](https://getbootstrap.com/)
    - App Theme and Styling
- [Email.js](https://www.emailjs.com/)
    - To send customer message to the admin's email
## Platforms
- [Github](github.com)
    - Store the code remotely for deployment
- [Gitpod](gitpod.io)
    - Development environment for the project
- [Heroku](https://www.heroku.com/)
    - Deployment
- [Bootstrap Themes](https://startbootstrap.com/)
    - Website Theme
- [AWS](https://aws.amazon.com/)
    - Project Database
- [Postgresql](https://www.postgresql.org/)
    - Database


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
3. Create a file called `.python-version` and add python version to it. e.g. 3.12
4. Create a file called Procfile and add this to the file `web: gunicorn your-project-name.wsgi --log-file -`
5. Replace `your-project-name` to your project name e.g. thai-massage
6. Now run these commands to upload the files to Github 
    - `git add .`
    - `git commit -m "your commit message"`
    - `git push`

### Setting up the heroku app
7. Login to your [Heroku](https://www.heroku.com/) account
8. Create a new app and give it a name
9. Connect your GitHub account from deployment method
10. Search and Select your repository
11. Click on Deploy


# Testing

## Methods
### Validation 
- HTML has been validated with https://validator.w3.org/#validate_by_input
- CSS has been validated with https://jigsaw.w3.org/ and auto-prefixed with https://autoprefixer.github.io/.
- Links checked with https://validator.w3.org/checklink.
- I also used https://pagespeed.web.dev/
- Javascript codes have been validated with https://jshint.com/

### General Testing

- To test the views models and forms do the followings
    - Go to the root of the  project
    - Run this command `python3 manage.py test`


- Each feature was testing when it implemented into the code on both safari and chrome.
- The site was sent to family and friends to review and get their feedback.
- Contact us form have validation and will not submit without all information filled in.
- The images were testing on all devices and browsers for performance/load speed. 

### Mobile Testing
 - I tested the site on IOS and Android device using my phone and family members phone, going through the entire process, checking button, functions, load speed, style etc.         
- Chrome and Microsoft edge was used to inspect the site in mobile format, looking at functions, responsiveness and style.

### Desktop Testing 
- The website was designed on Microsoft laptop, and it was previewed in Chrome and Microsoft edge. 
- The website was tested by family and friends and numerous different devices.


# Bugs
## Known bugs
- When admin and user login from the same browser, the username from userdashboard vanishes if the superuser doesn't have a name
- Custom 404 Page is not working properly
- User doesn't get any email after booking a schedule due to smtp server error
- Privacy Policy and Terms and conditions page is not working as awaiting content from the client
- Automated git deployment is not working


# Credits

## Acknowledgement
- My father in law owns Thai Siam Massage and I was assisted with information regarding the business by his son (my husband) Richard Lane who helped me make the blueprint of the app

# Contact
- Please feel free to contact me at samantha.moss87@aol.com