

[![Build Status](https://travis-ci.org/richdevelopments/guitar-shed.svg?branch=master)](https://travis-ci.org/richdevelopments/guitar-shed)

# Guitar Shed

## Introduction
----
<div align="center">
    <img src="https://i.ibb.co/C09Kdf2/Guitar-Shed-Home.png" href="https://guitar-shed.herokuapp.com/" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>
<br>

[Guitar Shed](https://guitar-shed.herokuapp.com/) is an **E-Commerce** website offering customers guitar lesson tutorial videos to vote for and purchase. The website name "Guitar Shed" comes from the word "Woodshed" or "Woodshedding". This is a term that’s used a lot among professional musicians around the world. The meaning is to practice or hone skills, particularly musical skills. The origin is from the fact that for purposes of privacy people would go to their woodshed to practice without being overheard.

The subjects taught in the tutorials are voted for by the customers using a **voting poll** application. Each poll has two options that are guitar technique subjects. The winning subject is the one with the most votes when the Poll expires. Which ever subject wins, I will then make a guitar tutorial based on that winning subject that will then be available to purchase in the Store.
The aim of the website is to provide guitar tutorials that the customer really wants and not just another random online guitar lesson video.

The project utilises multiple apps that use different online services, that come together to form a finished product. These are outlined in the UX Design below.

The app makes use of Whitenoise to host my static files, as well as integrates with Stripe for managing the apps checkout features.


## Table of Contents
----
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
        - [Guitar Shed Goals](#family-hub-goals)
    - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
        - [Business Stories](#business-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Registration Page](#registration-page)
        - [Log In Page](#log-in-page)
        - [Polls Page](#polls-page)
        - [Store Page](#store-page)
        - [Cart Page](#cart-page)
        - [Checkout Page](#checkout-page)
    - [Features Left to Implement](#features-left-to-implement)

3. [Database](#database)
    - [Database choice](#database-choice)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Contact](#contact)

9. [Disclaimer](#disclaimer)

----

# UX

## Goals

### Visitor Goals

The central target audience for Guitar Shed are:
- Hobbyists who want to learn new guitar techniques.
- Beginner guitar players.
- Advanced guitar players.
- Professional guitarists.

User goals are:

- Have somewhere to search for guitar tutorials to help better specific guitar techniques.
- Have somewhere to vote and ask for tutorials that the user really wants.
- Have a place to learn songs and new styles of music.
- Inspire users to progress and be creative.

### Business Goals

The target businesses to use Guitar Shed to advertise:
- Promote music events, concerts, local gigs.
- Guitar and Music magazines.
- Music platforms such as Apple Music and Spotify.
- Promoting latest Artist releases.

### Guitar Shed Goals

- Provide an effective, easy to use site for guitar players to search and vote for guitar tutorial videos that suit their needs.

- So that I can learn and practice frontend and backend programming together. To combine the use of HTML, CSS, Bootstrap and JavaScript with Python, Django and PostgreSQL.

- While this is currently a student project, the future goal of Guitar Shed is to monetise the website so that he users can actually buy and download the video tutorials, and also to charge businesses for advertising their events and activities on it. This will come later once the site has a few more features to offer those who use it (see [Features Left to Implement](#features-left-to-implement)).

## User Stories

### Visitor Stories

As a visitor to Guitar Shed I expect/want/need:

1. To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.

2. The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.

3. To search the videos to find the ones that will improve the techniques I want to work on.

4. To easily vote for the tutorial videos that I want to buy to improve my specific guitar techniques.

5. The site to provide easy access to the contact information,  email, website, social media links.

6. As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices.

7. As a regular user of the Guitar Shed website, I expect to be able to connect to their social media channels, to keep up to date with new entries on the site.

## Design Choices

I wanted the Guitar Shed website to have a smart modern feel, keeping things simple to emphasis the products and functioning. The following design choices were made with this in mind:

### Fonts

- The primary font `PT Sans` was chosen for the main text of the site because it is easy to read and complements the fonts chosen for titles very well. A extra reason for picking this font is that it is still easy to read when printed small.

- I used the `Helvetica` font for the main headings because it is simple and clear. The font stands out very well.

### Icons
For the icons I used fontawesome.

- Icons are mostly used on the navigation bar.

- Social media icons for facebook, twitter and youtube are used in the footer on every page of the site

### Colours

- The colours for this project were chosen because I wanted to the site to look smart and modern and I feel I have achieved this with the dark green/blue gradient background effect.

- A mainly white colour was chosen for the main text and headers as it made the text stand out on the darker background.

- The navbar background colour is a bold blue, which again stands out over the gradient background.

- The social media icons have a white border around them to help them stand out.

### Styling

- All **buttons** on the site fit the same bootstrap button styling in size and shape, but I added my own gradient green colours to them so they standout.

- Bootstrap **panels** were utilised on Guitar Shed to display the video product available to purchase. The panels were styled with **curved corners**, a theme repeated around the entire website in images, input boxes and buttons etc.

- Hover Effects
    - The **dropdown menu** (visible when logged in) has a hover effect that when hovering the dropdown menu opens with a "fade in" type movement and "fade out" when closing. This makes for a pleasingly smooth transition all achieved using jQuery.

    - Css effects on social media icons cause them to animate to red when hovered over.

- Some subtle **shadows** have been added to panels and nav bars, to give them depth on the page.


## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project. The design did change some what in development process.

- [Home](https://ibb.co/CsjNWtj)
- [Store](https://ibb.co/XDdrpx6)
- [Polls](https://ibb.co/PMb9jCm)
- [Register](https://ibb.co/FzxFTJW)
- [Cart](https://ibb.co/hghYt20)
- [Log in](https://ibb.co/ZmWCbdd)

# Features

## Existing Features

### Elements on every page
- Navbar
    - The navigation bar features the Guitar Shed in the top left corner.

    - For visitors to the site who are not logged in, list items links are available for them to use.
        1. Home
        2. Store
        3. Register
        4. Log in

    - For users who are logged in, the list items are as follows:
        1. Home
        2. Store
        3. Polls
        4. Cart
        4. Menu (this option is a dropdown menu)
            - Profile
            - Log out

    - The navbar is collapsed into a burger icon on small screens.

    - The stylish design choice was made to drop the navbar down from to the top of the page and to not have it spanning the full width of the page. This keeps it a bit smaller and looks smart which is what I was aiming for with the design.

- The Search bar is an animated search bar that grows when focus. At first I was sure where to put a normal search bar as it was getting in the way so I experimented with css and came up with the growing search bar so it would sit nicely in the corner.
The search bar is available to use on most of the pages, for the user to search the library of products.

- Admin side of the site features see

- Footer
    - The footer features:
        - Contact information for Guitar Shed.
        - Copyright information.
        - Links to social media locations.


### Home Page

<div align="center">
<img src="https://i.ibb.co/C09Kdf2/Guitar-Shed-Home.png" alt="Guitar Shed home page on all major screen sizes" >
</div>

**Headings**

- The Home page has a big heading telling the user what is on offer, with a description underneath explaining to the user how to use the website.

**Video**

- The home page features a **promotional video**. The video encourages the user to sign up to the website and explains how to use the website. It also shows sample clips of what to expect in the tutorial videos and what the customer can expect to work on.

### Registration Page

<div align="center">
<img src="https://i.ibb.co/WBQKqZN/Guitar-Shed-Register.png" alt="Guitar Shed register page on all major screen sizes" >
</div>

- The registration page features a simple form, where the user can input a username, email address and password. The form was kept deliberately simple so that signup has minimum barriers.

- Once the form is complete the data is sent to the backend where the user details are stored. (See database information below for details).

### log In Page

<div align="center">
<img src="https://i.ibb.co/m8kM0mX/Guitar-Shed-Login.png" alt="Guitar Shed login page on all major screen sizes" >
</div>

- The log in page also features a simple **form** where the user can enter either their username or their email address, and their password.

- If the user inputs incorrect data an error message tells them to input the correct credentials.

- When the user logs in with a correct email and password a success message tells them they have logged in successfully.

### Polls Page

<div align="center">
<img src="https://i.ibb.co/rmhbYRS/Guitar-Shed-Polls.png" alt="Guitar Shed Poll page on all major screen sizes" >
</div>

- The Polls Page features the voting polls for the users to vote for the subjects they want a video tutorial to be cased on. The user votes by clicking on the radio button underneath the subject/option they want and then clicking the vote button. When the user clicks on the **Vote button** the amount for that subject/option increases and this gets registered on the results on the frontend and also to the backend. Each voting poll has an expiry date. The subject/option with the most votes when the voting poll expires, wins the poll. I will then make a video tutorial based on the winning subject, which will then be available to purchase in the Store.
When a voting poll has expired, it displays "Poll expired. Purchase winner!" with a **Buy button** next to it which will redirected the user to the Store to purchase the winner.

### Store Page

<div align="center">
<img src="https://i.ibb.co/Fzx5YnT/Guitar-Shed-Store.png" alt="Guitar Shed Store page on all major screen sizes" >
</div>

**Product Panels**
- Each **product panel** in the Store gives the user some brief and useful information about each of the video products displayed. The product image, title and description introduces the product to the user. The user can choose however many of each item they wish to add to the cart. The products get added to the cart after selecting the amount and then clicking the add button, or will add 1 quantity of the product if an amount is not selected but the user clicks the add button.


### Cart Page

<div align="center">
<img src="https://i.ibb.co/5BzsGgC/Guitar-Shed-Cart.png" alt="Guitar Shed Cart page on all major screen sizes" >
</div>

- The Cart Page is where the user can amend the amount of products they would like to purchase. They then click the **Checkout button** which takes the user to the Checkout Page.

### Checkout Page

<div align="center">
<img src="https://i.ibb.co/5RbzcTd/Guitar-Shed-Checkout.png" alt="Guitar Shed Checkout page on all major screen sizes" >
</div>

- On the Checkout Page, users can see the products that they are about to purchase with the Total amount to pay. The user then fills out their shipping and payment details in a **form** then clicking the **Submit button** which the application then sending the details through **Stripe**. If there are any name and address details that are incorrect an error message prompts the user to enter the correct details. If the user enters incorrect payment card details, an error message will tell the user that the card details are incorrect or invalid.
If the user enters all correct details, the user will get a message saying "You have successfully paid".


## Features Left to Implement

1. The user Profile page needs more options such as the option to add more personal details and even a profile picture.

2. A part of the site where businesses can create an account and advertise their company, products and events.


# Database

### Database Choice
When this project was deployed to Heroku, Heroku uses ProstgreSQL for the database.
For this project I used the built-in Django administration site for the backend.
After logging in to the Admin site I created the following options to manage the backend of the website -

<div align="center">
<img src="https://i.ibb.co/dkN2ZyH/Guitar-Shed-Admin.png" alt="Guitar Shed Admin page on all major screen sizes" >
</div>

In the Users section, this is where all of the registered user information is stored and managed -
<img src="https://i.ibb.co/vcyGWP6/Guitar-Shed-Admin-Users.png" alt="Guitar Shed Admin User page on all major screen sizes" >

In the Order section, this is where all of the users order information is store which includes the users shipping details, products and product quantity.
<img src="https://i.ibb.co/bRdjP2y/Guitar-Shed-Admin-Orders.png" alt="Guitar Shed Admin User Order page on all major screen sizes" >

In the Polls section there is the Options page where I manage and create the subjects for the users to vote for.
<img src="https://i.ibb.co/h90j543/Guitar-Shed-Admin-Options.png" alt="Guitar Shed Admin Options page on all major screen sizes" >

In the Voting Polls section, this is where the Voting Polls are added or deleted.
<img src="https://i.ibb.co/f4XkzPg/Guitar-Shed-Admin-Voting-Polls.png" alt="Guitar Shed Admin Voting Poll page on all major screen sizes" >

When clicking on a Voting Poll, this then goes to the Change Voting Poll where each voting option can be changed as well as the expiry date and time for that Voting Poll.
<img src="https://i.ibb.co/THdfzx0/Guitar-Shed-Change-Voting-Poll.png" alt="Guitar Shed Admin Change Voting Poll page on all major screen sizes" >

In the Store section under Products, is where all of the products in the Store are managed. From adding new products, adding a Title, a Description, a Price and an Image. Editing and deleting the products are also done here.
<img src="https://i.ibb.co/5G3Z629/Guitar-Shed-Products.png" alt="Guitar Shed Admin Product page on all major screen sizes" >
<img src="https://i.ibb.co/3MdX0mD/Guitar-Shed-Change-Product.png" alt="Guitar Shed Admin Change Product page on all major screen sizes" >


# Technologies Used

### Tools
- [Whitenoise](http://whitenoise.evans.io/en/stable/) to store all static files for this project.
- [Imgbb](https://imgbb.com) to store all external images for this project.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [GitPod](https://www.gitpod.io/) for developing and to handle version control.
- [GitHub](https://github.com/) to store and share all project code.
- [Am I Responsive](http://ami.responsivedesign.is/) to create the images in this readme file of each page displayed on different screen sizes.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for Family Hub.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing
## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected.

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

#### Elements on every page

1. Navbar
    - Hover over each link, confirm the hover effect works as expected. __Pass__
    - Click the **Guitar Shed logo**, confirm it takes the user to the home page. __Pass__
    - Click the **Home** link, confirm it takes the user to the home page. __Pass__
    - Click the **Store** link, confirm it takes the user to the store page. __Pass__
    - Click the **Register** link, confirm it takes the user to the register page. __Pass__
    - Click the **Log In** link, confirm it takes the user to the log in page. __Pass__
    - Log into Guitar Shed, confirm that the navbar no longer displays the **Register** or **Log In** links but does now display the **Polls** **Cart** and dropdown menu. __Pass__
    - Hover over the dropdown menu, confirm it opens smoothly with javascript. __Pass__
    - Click the **Polls** link, confirm it takes the user to their polls page. __Pass__
    - Click the **Cart** link, confirm it takes the user to the cart page. __Pass__
    - Click the **Profile** link, confirm it takes the user to their profile page.__Pass__
    - Click the **Log out** link, confirm the user is logged out and the navbar returns to the logged out configuration. __Pass__

2. Footer
    - Hover over each social media icon, confirm the hover effect works as expected.
    - Click the **Facebook**, **Youtube** and **Twitter icons** and confirm they open the relevant social media pages in separate browser tabs. __Pass__

#### Home Page

- Video
    - Confirm that the video loads at a reasonable speed, and that the image is sharp and clear and plays well. __Pass__

- Headings
     - Confirm the heading for the page is easy to read. __Pass__

- Page text
    - Confirm the text for the page is easy to read. __Pass__


#### Register Page

- Go to Register page, confirm the form is displayed correctly. __Pass__

- Try to create a new account that already exists (same email and username), confirm that the *error alert* is informing the user that this **A user with that username already exists.**. __Pass__

- Try to create a new account with a new email address but a username that already exists in the database, confirm that the alert informing the user that this **username is already in use**. __Pass__

- Try to create a new account with a new username but a email address that already exists in the database, confirm that the alert informing the user that this **email is already registered**. __Pass__

- Create a new account with new username and email address, confirm that the **account conformation ** is launched with a log in button provided. __Pass__

- Click the log in button, confirm that it takes the user to the log in page. __Pass__

#### Log In Page

- Go to the log in page, confirm that the log in form is displayed correctly. __Pass__

- Try to log in with a username that do not exist in the database, confirm that the error alert is displayed to inform the user that **Your username or password is incorrect**. __Pass__

- Repeat above with incorrect email address, confirm same reaction. __Pass__

- Try to log in with an existing username but incorrect password, confirm that the error alert is displayed with a message informing the user of **Your username or password is incorrect**. __Pass__

- Try to **log in** using correct **username and password**, confirm that this is successful. __Pass__

- Log out, then try to log in using correct **email and password**, confirm that this is successful. __Pass__

#### Log Out Feature

- When logged in, click the log out link, confirm to the user **You have successfully been logged out**. __Pass__

#### Profile Page

- Go to the settings page for the account I am logged in as, confirm that the page is displaying correctly. __Pass__

#### Polls Page

- Go to Poll page, confirm the form is displayed correctly. __Pass__

- Clicking on a radio button under a subject/option then clicking vote button, increases the number of votes for that subject/option. __Pass__

- After voting on a poll, the user can no logger vote on that poll and the radio buttons and vote buttons are no longer displayed. __Pass__
- When a poll has expired a message "Poll Expired. Purchase winner!" with a Buy button is displayed. __Pass__
- The Buy button takes redirects to the Store. __Pass__

#### Cart Page

- Go to Cart page, confirm the form is displayed correctly. __Pass__
- If I access the the shopping cart at a user or as admin or staff member, the pages is the same. I have an amend button and checkout button. __Pass__
- Changing the quantity to 0 removes the item from the cart and brings me to an empty cart screen. __Pass__


#### Checkout Page
- Go to Checkout page, confirm the form is displayed correctly. __Pass__
 - The checkout page shows the items selected from the shopping cart.  The total for all items chosen is shown  above _Payment Details_ form. __Pass__
 - If I leave out the details on the payment details form and click _submit payment_, an alert appears on the form field to show the items that need to be filled in. __Pass__
 - If I fill out the form and provide the stripe developer credit card details, and click Submit Payment, I get a message saying my payment was successful. __Pass__


### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile and tablet specific elements on my iPhoneX and tablet, in both the Safari browser and Chrome internet browser.

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar
- Open the website on mobile, confirm that the navbar is collapsed into a burger icon. __Pass__
- click the burger icon, confirm that the navbar list appears are expected. __Pass__
- When logged in, confirm that the navbar list appears as expected for someone logged in. __Pass__
- When on tablet, confirm that the navbar is not collapsed on my larger tablet screen, but is on the smaller tablet. __Pass__

2. Footer
- On mobile, confirm that the footer sections stack on top of each other as expected. __Pass__
- On tablet, confirm that the footer sections appear as expected. __Pass__


Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

### Bugs discovered:
#### Solved bugs

1. Clicking the Add to cart button on a Product without adding a quantity displayed a page error. This was resolved by adding ```value="1" name="quantity" and type="number"``` to the Add to cart button. Now it will add a single product.

#### Unsolved bugs

1. The only annoying issue still to fix is the overlapping background on mobile when viewing the Polls page.


# Deployment

## Heroku Deployment

To deploy Guitar Shed to Heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DATABASE_URL | postgres://
SECRET_KEY | `<your_secret_key>`
STRIPE_PUBLISHABLE | `<your_stripe_publishable>`
STRIPE_SECRET| `<your_stripe_secret>`

8. In the Heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

# Credits

## Content

- All text and business model was written by me and had influence by [JamTrackCentral](https://www.jtcguitar.com).

## Media

### Images
- All images in the project were snapshots taken from my promotional video on the Home page.

### Video
- The promotional video on the Home page was recorded and edited by me and is me playing guitar in the video.

## Code

- I used a small part of an app that used to be in the course called We_are_Social, suggested to me by my tutor Aaron Sinnott. This was a forum app which had a Poll app in it that could be added to a forum post. I used the Poll part as an idea for my Poll page, and heavily changed it to suit my website.

## Acknowledgements

Special thanks to my mentor Aaron Sinnott for his patience and willingness to teach me his coding expertise and giving me valuable industry advice.

## Disclaimer
The content of this website is educational purposes only.

