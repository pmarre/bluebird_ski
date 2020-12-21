# Bluebird Ski Shop

Bluebird Ski Shop can be accessed here: [Live Site](https://bluebird-ski-shop.herokuapp.com/)
Stripe payment requires a test credit card number to check out, please use: 4242 4242 4242 4242 Exp: 04/24 Zip: 42424

## Table of Contents 
1. [UX](https://github.com/pmarre/bluebird_ski/blob/main/README.md#user-experience)
  - [User Stories](https://github.com/pmarre/bluebird_ski/blob/main/README.md#user-stories)
  - [Strategy](https://github.com/pmarre/bluebird_ski/blob/main/README.md#strategy)
  - [Scope](https://github.com/pmarre/bluebird_ski/blob/main/README.md#scope)
  - [Structure](https://github.com/pmarre/bluebird_ski/blob/main/README.md#structure)
  - [Wireframes](https://github.com/pmarre/bluebird_ski/blob/main/README.md#wireframes)
2. [Features](https://github.com/pmarre/bluebird_ski/blob/main/README.md#features)
  - [Future Features](https://github.com/pmarre/bluebird_ski/blob/main/README.md#future-features)
3. [Technology Used](https://github.com/pmarre/bluebird_ski/blob/main/README.md#technology-used)
4. [Testing](https://github.com/pmarre/bluebird_ski/blob/main/README.md#testing)
6. [Deployment](https://github.com/pmarre/bluebird_ski/blob/main/README.md#deployment)

## User Experience 

- The goal of Bluebird Ski Shop is to create an easy to use, responsive site for users to reserve services from a ski shop
- The site is responsive and works on all browsers
- Clickable items have hover effects to alert the user that they can be clicked
- Inputs use placeholders to clearly describe what needs to be entered by user
- The flow of the website is clear, so users can easy maneuver from landing page to checkout 

### User Stories

-_"I am learning to ski a place to easily reserve skis online in advance"_, Completed by allowing users to easily search the site for the service they are looking for and checkout. 
-_"I am always looking to save money by subscribing to a website"_, Completed by allowing users to sign-up and save 10% on all purchases. 
-_""_

### Strategy

My first step in the design process was to decide on a target audience so I could create a website that would work well for that audience. The target audience for a ski rental / service shop can be quite broad with absolute beginners looking to make a reservation, to seasoned skiers looking for ski repair services. In an effort to appeal to all, I created a site that is simple to use whether you were an absolute beginner or a professional. 

### Scope 

Next, I worked out what this broad audience needed. Many people travel from out town to go skiing and snowboarding, but don't always want to lug around their own equipment through airports or don't have the space in their car. So, I came up with a simple solution that any local ski shop could use, an online rental shop. 

After I came up with the solution, I decided to present it in a clear and simple design and focus on the services to be offered. Users can sign-up on the site to create and easier checkout process in the future and save 10%. 

### Structure

Responsiveness and clarity were key focuses of this site. With a broad target audience, I wanted every user to be able to quickly find what they needed and make a purchase. Since many users are likely traveling, responsiveness is important for users to be able to easily us the site on their phones while traveling. 

#### Wireframes 

<details>
  <summary>Homepage Wireframe</summary>
  <br />
  <img alt="Desktop homepage wireframe" src="https://github.com/pmarre/bluebird_ski/blob/main/media/readme_images/bbss_homepage.png">
</details>

<details>
  <summary>Services Wireframe</summary>
  <br />
  <img alt="Services wireframe" src="https://github.com/pmarre/bluebird_ski/blob/main/media/readme_images/bbss_services.png">
</details>

<details>
  <summary>Service Detail Wireframe</summary>
  <br />
  <img alt="Desktop service detail" src="https://github.com/pmarre/bluebird_ski/blob/main/media/readme_images/bbss_service_detail.png">
</details>

### Features 

This project is built with Django, Python, JQuery, CSS, HTML, and a uses a Postgres database for storage. This site also utilizes Stripe for checking out and All-Auth for login/out functionality.

#### More Key Features:

1. CRUD functionality
   - Superusers (admins) can quickly add, remove, delete services 
   - Users can easily save and edit their profile information
2. Stripe
   - Stripe is used to capture all payments 
3. Email
   - All users recieve verification emails upon signup and confirmation emails after purchase
4. Discount 
   - All registered users recieve 10% discount on purchases 
   
#### Future Features:

1. Sell products beyond just rentals and services
   - Expand site out to include ski related products for users to purchase 
2. Blog 
   - Include a ski related blog/newsletter that gets emailed out the subscribers 
3. Date functionality
   - For more accurate reservations, I would like to use a date range picker to reserve equipment on a specific day 

## Technologies Used

- Python - used as the backend language to connect what the user sees and the data they have input
- Django - framework used to simplify python for faster builds
- Postgres - database for storing all user input
- HTML5 - used to semantically structure website
- CSS3 - used for styling of HTML
- Javascript - used in conjunction with jQuery to create an interactive user experience
- jQuery - used in conjunction with Javascript to create an interactive user experience
- Stripe - used to recieve payments
- AWS S3 - used for file storage 
- Heroku - used for site deployment
- Bootstrap - used for quick, responsive styling 
- Font Awesome - Used for icons
- Google Fonts - Used for website typography
- Unsplash - used for free stock photos

#### Manual Testing:

##### Found Bugs/Errors:

1. Stripe webhooks 
   - I struggled to get the webhooks working on the live site, I continually reviewed the course, StackOverflow, and any other resources I could find and eventually resolved the issue
2. Database migration
   - After deploying my site and migrating everything over to S3, I went back and made some changes to my code that I then only migrated locally. I spent hours trying to figure out why my live site wasn't working only to realize I never migrated the updates over to S3. 
3. Settings / Django in general 
   - In general, I spent a lot of time playing with settings and debugging Django. Being new to this framework, it took me a few tries to really start to understand the complexities of Django.
3. Peer review in Code Institute Slack Channel
   - Used the peer review Slack channel to have student/alumni/mentors review the site and give feedback and look for bugs
   - There was one major issue caught:
   
#### Device/Browser Testing

1. Used Chrome Dev tools to test the responsiveness of this project on multiple devices
2. Check browser compatibility in Firefox, Chrome, and Safari

## Deployment

#### Local Deployment

To create a local copy of this repository, follow these steps:

1. Go to my [repo](https://github.com/pmarre/scratch/)
2. Click the "Clone or Download" button on the top-right of the page
3. Click the copy icon to copy the HTTPS link
4. Open terminal
5. Change the current directory to the location where the cloned directory will be made
6. Type `git clone <cloned URL>` with the cloned URL being the URL you copied in step 3 and run the command

For more information check out GitHub's guide to cloning a repo [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

#### Deploy to Heroku

Detailed instructions for deploying to Heroku can be found [here](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)
