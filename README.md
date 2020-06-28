# Final Milestone Project - Full Stack Frameworks with Django

Link to live demo [Classic Sounds](https://classic-sounds.herokuapp.com/)

The purpose of the project is to showcase the skills learnt throughout this course and to test capabilities in creating a functioning e-commerce site.

![Login Page](/media/images/Auth.jpg)

---

## Table Of Contents

**1. [UX](#ux)**

- [User Stories](#user-stories)

  - [Site Look & Feel](#Site-Look-&-Feel)
  - [Account Function](#Account-functions)
  - [Product Function](#Product-functions)
  - [Cart Function](#Cart-functions)
  - [Checkout Function](#Checkout-functions)

- [Design](#design)
  - [Framework](#Framework-Technologies)
  - [Color Scheme](#color-scheme)
  - [Icons](#Icons)
  - [Typeography](#Typeography)
  - [Wireframes](#Wireframes)

**2. [Features](#Features)**

- [Home App](#Home-App)
- [Account App](#Accounts-App)
- [Products App](#Products-App)
- [Cart App](#Cart-App)
- [Checkout App](#Checkout-App)
- [Profile App](#Account/Profile=App)
- [Contacts App](#Contacts=App)
- [Search App](#Search-App)
- [Base Template](#Base-Template)

**3. [Testing](#Testing)**

- [Validation Services](#Validation-Services)
- [Travis](#Travis)
- [Manual Testing](#Manual-Testing)
- [Found issues](#Found-issues)
- [User & Stripe payment testing](#User-&-Stripe-payment-testing)
- [Responsiveness](#Responsiveness)

**4. [Planned Features](#Planned-Features)**

**5. [Deployment](#Deployment)**

- [Prerequisite before deploying](#Prerequisite-before-deploying)
- [Running Code Locally](#Running-Code-Locally)
- [Running Code on Heroku](#Running-Code-on-Heroku)

**6. [Credits](#Credits)**

---

## UX

The purpose of the project was to create a website using the Full Stack Framework.
I chose to create an online musical instrument shop where the store can display, showcase and sell their products.
The design of the site was intended to present the product offerings in a more creative setting that was more
in line with the store mission and move away from generic on-line store formats.

## User Stories

Users require, at a minimum, the following functionality

### Site Look & Feel

- The abililty to view the site from any device (mobile, tablet, desktop).
- To be able to browse the site and the products before committing to registration.
- The site should flow and be intuitive.
- The sections & pages should be clearly defined and contain all relevent information.
- A clearly defined contact section with capability to request information from shop and links to Social Media platforms.

### Account functions

- Easily create my account.
- View my profile once I have completed account creation.
- Clear login and logout functions & logout should be possible from all screens.
- See user credentials in profile/account pages.
- Simple method to change my password.

### Product functions

- A view of all products with filter to each category type.
- I want to be able search for a product.
- A link from a product to a detailed view of the product with all relevent information and images.
- I want to be able add products to my cart and remove samehttps://themes.getbootstrap.com/ if I change my mind.

### Cart functions

- I can view my order summary before checkout.
- I want to be able to amend or remove the order from within the cart before submission.

### Checkout functions

- The checkout page should contain a summary and total price of the products ready for purchase.
- The submission form should be clear and secure.
- There should be clear messaging when a purchase is successful or unsuccessful.
- Completed purchases should be viewable within the site with potential to re-purchase.

## Design

The site design looked to differentiate Classic Sounds from generic e-commerce sites and contain
a more artisan feel to it. I chose 'greyscale' as a theme so as to give subtle colouring to all displays
with the exception of the product images. This was done so that the user would be drawn to those sections of
the site. The greyscale theme was taken from the Bootstrap site and amended to suit the ideals of the site with
light-to-dark transitions on the pages without background images.

The hope of the final design was that users or those just browsing would find Classic-Sounds a little bit
separated from the norm.

### Framework Technologies

The principle technologies utilised for the development were;

- [Bootstrap 4.5](https://getbootstrap.com/)
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
- [Django 1.11](https://www.djangoproject.com/)
- [Python 3.6.7](https://www.python.org/)

Supporting technologies applied were;

- [Visual Studio Code](https://code.visualstudio.com/) - The IDE used for developing this project.
- [GitHub](https://github.com/) - Code repository.
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
- [Stripe](https://stripe.com/docs/api) - Used to make secure payments.
- [AWS S3 Bucket](https://aws.amazon.com/)
- [Travis](https://travis-ci.org/) - for continuous integration.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Font Awsome](https://www.bootstrapcdn.com/fontawesome/)

The site was deployed using;

- [Heroku](https://www.heroku.com/) - for deployment
- [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.

### Color Scheme

The greyscale theme employed was maintained throughout the site with backgrounds displays in black & white, teal for main buttons
and colour imaging being reserved for product sections and specific product images.

### Icons

- [Font Awsome 5.11.2](https://fontawesome.com/)

### Typography

The following fonts were used :

- Varela
- Nunito

Taken from google fonts

### Wireframes

Initial wireframing templates for this project can be viewed [here](https://github.com/Mofarrell1967/classic-sounds-music/blob/master/static/wireframes/testing%20results.pdf)

## Features

### Home App

The home app page is divided into 4 sections with soft scroll functionality applied to each section.

The Top or Home section - allows the user to Login or Register for the site and the buttons displayed on this page
will change to product links once a user is logged in.

The About section provides the user with information about Classic Sounds and the purpose of the site.

The Collection section provides links to either an all products view or filtered by type. It also summarises
what can be found in those sections.

The Contacts section displays the means of contacting Classic Sounds along with Soical Media buttons and also provides the user
with a email information request link.

![Home Page](/media/images/Classic-Sounds.jpg)

### Accounts App

The accounts app will allow users to register and create their own unique account.
This is built using Django's authentication and authorization to validate profile data.
Passwords are hashed for security purposes.

The users will register using the registration form. Registered users will be able to
login by using the login form with their username and password or with their email and password.

The users can also reset their password if they forgot the original password using the reset
password link on the login.html page.

![Login Page](/media/images/Login.jpg)

![Login Page](/media/images/Auth.jpg)

### Products App

Displays all Products available in the store that can be purchased by authenticated users.

![Login Page](/media/images/products.jpg)

**products.html**

Displays all the products available in the website collection.
Pagination to display only 6 products per page.
Buttons above the display to allow users choose to filter by Guitars, Keyboards or Percussion.
Users can see the product image, name, summary & price. There is also a 'read more' option to take the user to the detail page.
Users can add the product to the cart.

**guitars.html**

Displays all the guitars available in the website.
Pagination to display only 6 products per page.
Buttons above the display to allow users choose to filter by Collection, Keyboards or Percussion.
Users can see the product image, name, summary & price. There is also a 'read more' option to take the user to the detail page.
Users can add the product to the cart.

**percussion.html**

Displays all the percussion instruments available in the website.
Pagination to display only 6 products per page.
Buttons above the display to allow users choose to filter by Collection, Keyboards or Guitars.
Users can see the product image, name, summary & price. There is also a 'read more' option to take the user to the detail page.
Users can add the product to the cart.

**keyboards.html**

Displays all the keyboard instruments available in the website.
Pagination to display only 6 products per page.
Buttons above the display to allow users choose to filter by Collection, Keyboards or Percussion.
Users can see the product image, name, summary & price. There is also a 'read more' option to take the user to the detail page.
Users can add the product to the cart.

**product_detail.html**

On this page the user can see all the details about the product.

![Product Detail](/media/images/detail.jpg)

- Product name
- Images of product
- Summary Description
- Manufacturer
- Product Description

The Product Description provides detailed information pertaining to each instrument.

If the user want to add the product to the cart they can do from here as well.

### Cart App

**cart.html**

The shopping cart page displays the summary details of all the items added to the cart.

- Product name
- Quantity
- Unit Price
- Option to adjust quanity
- Total Cart amount
- Button links to Checkout or Shop

![Login Page](/media/images/cart.jpg)

### Checkout App

**checkout.html**

The shopping cart page displays the summary details of all the items along with the total added to the cart.

The user need to fill out the payment form in order to go for the payment.

Once the payment is successfull, a message will be displayed.

If there is an error with the payment, the user will be notified with an error message.

Open successful completion of a purchase the user will be rediected to the accounts page where details of purchases
will be displayed.

![Login Page](/media/images/checkout.jpg)

### Account/Profile App

This app displays the current login credentials in use on the site and an option to update the password.

The page also displays historical purchases or a message to say there are no orders should none have been made to date.

![Login Page](/media/images/account.jpg)

### Contacts App

This app is accessible from the Contacts section of the home page and takes the user to an email information request page. Once
the user submits the information request an success response will be displayed with an option to return to the shop.

### Search App

This will allow the user to search for a product based on the name.

The search icon is visible from all the pages. The user enters the required search item and hits the enter
key to progress the search.

### Base Template

Provides Navbar and Footer details across all pages.

Navbar shows;

- Site name (also acts as home button)
- Search bar
- About link
- Shop link
- Contact link
- Account link (shown as icon) and only when user is authorised
- Cart link (shown as icon) and only when user is authorised
- Logout (shown as icon) and only when user is authorised and logged in

Any page messages will also be displayed in the navbar.

**Footer**

The footer features on every page.

The footer only contains the copyright details - Social Media links are displayed in the Contacts section.

# Testing

### Validation Services

- **HTML**: [https://validator.w3.org/](https://validator.w3.org/) used to validate the HTML code.

- **CSS**: [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) used to validate the CSS code.

- **JavaScript**: [https://jshint.com/](https://jshint.com/) used to check the JavaScript code.

### Travis

Travis was used for continuous integration testing.

[![Build Status](https://travis-ci.org/Mofarrell1967/classic-sounds-music.svg?branch=master)](https://travis-ci.org/Mofarrell1967/classic-sounds-music)

## Manual Testing

Due to the nature of the site and the need to maintain the flow it was felt that manual testing would be preferential over automated testing as it
allows the testing team to evaluate the behaviour of the site rather than just the functionality.

A testing matrix was developed and issued to 4 individual test users and only when all tests passed was the testing procedure signed off as complete.

The testing checklist can be viewed [Here](https://github.com/Mofarrell1967/classic-sounds-music/blob/master/static/wireframes/testing%20results.pdf)

## Found issues

- Cart item display on small mobile devices is not quite lining up.
- Transition from small laptop to tablet shows product images out of container. This issue is only displayed when
  the user manually resizes the screen but is not apparent should the page load on any particular device size.

These bugs will be corrected as part of the next version updates - see 'Planned Features' section

## User & Stripe payment testing

The checkout app is using the stripe payment for the payment option. The checkout app works from the Stripe API.

Card number - 4242424242424242

CVC - Any 3 digit number.

Expiry date - Any date in the future.

Demonstrator user credentials have been created that can be used if required

Username : demo
Password : demo

## Responsiveness

Chrome DevTools and physical devices were used throughout development for a number of purposes, one of which was to test the responsiveness and rendering across a range of sizes and devices.

The site has been tested successfully on

Apple Macbook Air - Safari browser

Apple iPhone 6,7 &8S - Safari Browser

Samsung S10+ - Chrome & Sansung browsers

Desktop - Chrome v.74

Desktop - Firefox v.67

# Planned Features

Features planned for version 2 of site are;

1.  Correction of bugs identified in "Found Issues" section above.
2.  Replace current messaging with Toastr.
3.  Add Wishlist to product pages.
4.  Create Admin Panel for superusers to manage database from within the application itself.
5.  Add a 'Buy Again' option to the Order History section.

# Deployment

## Prerequisite before deploying

1.  An active account on Stripe and have a copy of your API keys
2.  An active Postgres database setup on Heroku and you have a copy of the API key
3.  An active account on AWS with buckets configure to store media and CSS files
4.  An email account

## Running Code Locally

1.  Open the link to the [Github Repository ](https://github.com/Mofarrell1967/classic-sounds-music " Github Repository")
2.  Click the Clone or Download and select the copy icon
3.  In your local IDE open Git Bash
4.  Change the current directory to where you want the cloned directory to be made
5.  Type `git clone` and then paste the URL
6.  Press enter and your local clone will be ready
7.  Create and start a new environment
8.  install the project dependencies
9.  Create a new file called `env.py`
10. Enter your environment variables

import os

os.environ.setdefault("STRIPE_PUBLISHABLE","<enter key here>")
os.environ.setdefault("STRIPE_SECRET","<enter key here>")
os.environ.setdefault("DATABASE_URL","<enter key here>")
os.environ.setdefault("SECRET_KEY", "<enter key here>")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "<enter key here>")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "<enter key here>")
os.environ.setdefault("EMAIL", "<enter key here>")
os.environ.setdefault("EMAIL_PW", "<enter key here>")
os.environ.setdefault("EMAILJS_USER", "<enter key here>")

11. Add `env.py` to `.gitignore` file
12. Go into the terminal and run the following
    `python3 manage.py makemigrations`
    `python3 manage.py migrate`
    `python3 manage.py collectstatic`
13. Create a superuser
14. Run the server
    `python manage.py runserver`
15. in terminal run the following
    `git add --all`
    `git commit -m "initial commit"`
    `git push`
16. Open `localhost:8000` on your browser

## Running Code on Heroku

1.  Create a new app in Heroku
2.  Go into add-ons and add Heroku Postgres
3.  Go into terminal on your IDE and enter the following

    `pip3 install dj-database-url`
    `pip3 install psycopg2`
    `pip3 freeze > requirements.txt`

4.  Go into the terminal and run the following

    `python3 manage.py makemigrations`
    `python3 manage.py migrate`
    `python3 manage.py collectstatic`

5)  In Heroku click on settings and then Reveal Config Vars and add the following from the env.py file.

| Key Name              | Value                        |
| --------------------- | ---------------------------- |
| STRIPE_PUBLISHABLE    | <your_stripe_publishable>    |
| STRIPE_SECRET         | <your_stripe_secret>         |
| DATABASE_URL          | <your_postgres_database url> |
| SECRET_KEY            | <your_secret_key>            |
| AWS_ACCESS_KEY_ID     | <your_secret_key>            |
| AWS_SECRET_ACCESS_KEY | <your_secret_key>            |
| EMAIL                 | <your_email_address>         |
| EMAIL_PW              | <your_password>              |

6.  Connect the Heroku app to the GitHub
7.  In Heroku select Deploy Branch

---

## Credits

**Content**

Content for the products are from https://www.gear4music.ie/ and were modified for use in the project.
Theme design was sourced and influenced by https://themes.getbootstrap.com/

**Acknowledgement**

The tutors, mentors and support staff at Code Institute.

Special thanks to;
Tutor Stephen Moody for his constant education and support.
Mentor Maranatha Ilesanmi for his guidance and advice throughout this learning experience.
Fellow student Paul Dardis for assistance on the Pagination code.

**Disclaimer**

The content of this website is for educational purposes only.
