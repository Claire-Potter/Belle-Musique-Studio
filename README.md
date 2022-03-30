# Belle Musique Studio
## About this project:

![Belle Musique Studio Mockup](https://github.com/claire-potter/belle-musique-studio/blob/main/project-files/design/all-devices-white.png)


<a href="https://belle-musique-studio.herokuapp.com/" target="_blank">Click here</a> to access the live site.

Belle Musique Studio is the business of singing and piano teacher Jo-Anna Hope. Jo-Anna runs her own small business and requires her own website through which users can subscribe to singing lessons, piano lessons, songwriting lessons and make product purchases. 

This project is based on the project example idea one for Code Institute project five, however, it has been modified to align with the needs of the music studio.

User profiles contain information that map to singing/piano or songwriting lesson plans and music product orders.

Jo-Anna and admin staff are able to showcase students by adding content to the Showcase student section on the about page.

A subscription-based payment model as well as an individual item purchase capability is in place.

An authentication and authorisation mechanism for students, shoppers as well as site owner, site administrator and super user has been set up.

SEO, Social Media and Email strategies have been employed to market the studio.

This site has been completed as  a minimum viable
product and hopefully in time, the functionality can be extended.

The project is developed using Django, Python, JavaScript, HTML, CSS, and the Bootstrap framework.

This is currently a test project.

<!-- Start Document Outline -->

* [UX Design](#ux-design)
	* [User Stories](#user-stories)
	* [Strategy](#strategy)
		* [High-level Business Goals](#high-level-business-goals)
		* [Value](#value)
		* [Why is this site so special?](#why-is-this-site-so-special)
		* [Trade-offs](#trade-offs)
	* [Scope](#scope)
	* [Structure](#structure)
		* [Skeleton](#skeleton)
		* [Access](#access)
			* [Site visitors](#site-visitors)
			* [Registered users](#registered-users)
			* [Site Administrator, Site Owner and Superuser](#site-administrator-site-owner-and-superuser)
	* [Wireframes](#wireframes)
		* [Differences](#differences)
	* [Design](#design)
		* [Colours](#colours)
		* [Fonts](#fonts)
	* [Search Engine Optimisation](#search-engine-optimisation)
	* [Web Marketing](#web-marketing)
		* [Content Marketing](#content-marketing)
		* [Social Media Marketing](#social-media-marketing)
		* [Email Marketing](#email-marketing)
	* [GDPR](#gdpr)
	* [Business Model](#business-model)
		* [B2C – Business-to-consumer.](#b2c--business-to-consumer)
* [Database](#database)
* [Features](#features)
* [Technologies used](#technologies-used)
	* [Languages](#languages)
	* [Agile Planning](#agile-planning)
	* [Images](#images)
	* [Libraries and Frameworks](#libraries-and-frameworks)
	* [Development tools](#development-tools)
	* [Deployment/Hosting](#deploymenthosting)
	* [Payment](#payment)
	* [Static and media file storage](#static-and-media-file-storage)
	* [Email](#email)
* [Testing](#testing)
* [Deployment](#deployment)
	* [Required technology](#required-technology)
	* [Maintaining Code](#maintaining-code)
	* [Deployment to Heroku](#deployment-to-heroku)
	* [How to Fork the Repository](#how-to-fork-the-repository)
* [References](#references)
	* [Code](#code)
		* [General Queries](#general-queries)
		* [Code Adaptations](#code-adaptations)
	* [Content](#content)
	* [Acknowledgments](#acknowledgments)

<!-- End Document Outline -->

# UX Design

## User Stories

**Project Goals**

**Site Users**
1. Register to create  an account 
2. Subscribe to  singing/piano or songwriting lessons
3. Choose to pay weekly, monthly or annually
4. Make individual purchases within the online music store
5. Contact the site owner
6. Complete functionality / access all features as created within the User Stories for the role: Site User

**Site Owner and Site Administrator**

1. Front End Create Only:
   * Student Showcase record
   
2. Front End Create and Update:

    * Products:
   
        * Singing Lessons
        * Piano Lessons
        * Songwriting Lessons
    
    * Subscription Plans:
   
        * Weekly payment
        * Monthly payment
        * Annual payment

3. Front End Create Update and Delete:
    * Product Inventory
    
4. Site Admin access as stipulated under the authorisations section

5. Receive contact emails when a contact request is sent from the site

6. Complete functionality / access all features as created within the User Stories for the roles: Site Administrator/ Site Owner


**User Stories**

You can view an organised board with all user stories here:

<a href="https://github.com/Claire-Potter/Belle-Musique-Studio#workspaces/belle-musique-studio-development-61e5727e52eb070014ba3072/board" target="_blank">User Stories</a>

## Strategy

### High-level Business Goals

 - Create a well thought-out and user friendly website to run the music studio via
 - All content to be concise and easy to understand
 - All offerings to contain the necessary content required by a site user to subscribe or make a purchase
 - The purpose of the website is to attract new clients as music lesson students, sell products to both clients and the general public and to manage the accounts of existing clients
 - To be utilised by site owner and site administrator, students and shoppers 
 - Optimise the site SEO to ensure that it ranks high with Google search
 - Run a marketing strategy through site advertisement, and marketing emails to promote the business

### Value

The value lies in the promotion of lessons on the site. The main revenue is generated through ongoing subscriptions. If other users are visiting the site as shoppers the site owner can use the opportunity to promote individual music lesson subscriptions and entice users to subscribe.
The student showcase section allows the site owner to display the skills of her students. All current students will also have access to make any necessary purchases directly from the studio, thereby promoting the music shop and generating additional revenue.


### Why is this site so special?

What makes this site special:

 - Receive all the necessary details to be able to learn about the studio and the lessons available
 - Subscribe to singing, piano or songwriting lessons with ease
 - Set up secure recurring payments
 - Manage multiple subscriptions from one account
 - Be able to pay weekly monthly or annually
 - Access and download recent invoices
 - Cancel subscriptions from the user profile
 - Purchase any music products necessary for lessons
 - Easy, direct and secure payment for products
 - Remember address details for future purchases
 - Access all past order information
 - Learn about the studio and receive weekly student showcases
 - Contact the site owner / site admin with ease
 
### Trade-offs

| Opportunity                                                                                                                                   | Importance | Difficulty |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|------------|
| Navigation across the site                                                                                                                    | 5          | 1          |
| Home Page with core links                                                                                                                   | 4          | 1          |
| About page including student showcase and advertisements                                                                            | 5          | 2          |
| Linked video to student showcase                                                                                                                  | 3          | 2       
| Lessons page with information on all lessons available and the weekly, monthly and annual subscription options                                                    | 5          | 4      |
| Integration with stripe to create and pay for subscriptions                                                                                                                | 5          | 4          |
| Lesson bag to add lessons to and checkout or remove lessons from                                                                                                                 | 4         |4         |
|Success and warning  messages for all actions. Success message to include lesson bag summary                                                                                                                   | 4          | 4         |
|Email sent when a subscription is successfully taken out                                                                                                                  | 4          | 3          |
| Ability to cancel an active subscription                                                                                           | 4          | 3          |
| Music Store with various products available for purchase                                                                                 | 4          | 4          |
| Different product views                                                               | 3          | 2          |
| Ability to select a product, view detail, add to shopping bag                                                       | 4          | 3         |
| Ability to select the product quantity and size if applicable | 4          | 4          |
| Ability to remove the product from the shopping bag                                                                                               | 3          | 2       |
| Ability to checkout and pay for the product/s with ease. Able to add a shipping address which can also be saved through to the user profile                    | 4          | 4          |
| Email confirmation for successful purchases      | 2          | 3        |
|Success and warning  messages for all actions. Success message to include shopping bag summary                                                                                                                   | 4          | 4         |
| User profile with subscription and order summaries and saved address details                                                 | 4          | 4          |
| Access a past order's details to review                                               | 4         | 4          |
| Access a subscription's details to review                                               | 4         | 4          |
| Contact form for all site users and visitors to contact administration via, to be sent out via email and to be received within the admin page                                               | 4         | 3         |
| Internal lesson, student showcase and store adverts across client facing pages to really promote the site's offerings                                             | 4          | 2         |
| Front end access for site owners and administrators to add/edit or delete music store products, add or edit lessons and subscriptions and showcase students                                             | 4          | 3         |
| Necessary access for different roles to the site admin section                                             | 4          | 2         |
| Worship programmes scheduled monthly which users can book to attend                                            | 3          | 4          |
| Interactive student profiles for students to post content from and comment on                                           | 3          | 4          |



Using the trade-off process to rank the importance and feasibility of the opportunities I have decided:

1. To go ahead with 25/27 of the opportunities.
2. Given the time-frame and my current skill as a developer, I have to narrow down the scope of the deliverable and focus on the core functionality.
3. The worship programme and interactive student profiles will not be included.

## Scope

For this project, the main aim is to create a transactional platform to assist a user through the subscription purchase process and the product purchase process. Secondary to that is to provide the user with the necessary information required to be able to make their decision around what lessons to enroll in and what subscription type would be best for them. The Music Store will be set up to be able to provide all of the necessary tools to music students for their lessons as well as to increase overall revenue. Every opportunity for internal advertisement will be taken to promote lessons, student showcases and the store. The website will be designed to render successfully across all screen sizes and platforms. Accessibility requirements will be considered and addressed. Apart from the default Django Admin centre, which is best utilised from a laptop/computer, the design has been completed for mobile first.

In order to create a streamline navigation menu, a My Account section has been added as a dropdown sub-menu. This section will include the options to Register / Login or Logout and access to the User Profile. An Admin dropdown has been added for staff access to site admin, product and lesson maintenance and student showcase form.

To provide an overview of the business, including it's purpose and owner information, an About page has been included. A user can easily scroll down the page to read the various information sections, a useful return to top icon has been included to easily return to the top of the page.

Users who have registered for an account will have the additional option of accessing and updating their user profile. It is not necessary to register to purchase an item from the store, however, to take out a subscription, a user is required to register as it will involve setting up recurring payments. Users are able to view all past order details from their profiles as well as their active subscriptions. They can cancel a subscription, just after they have paid for it in case it was done in error or at any later date from their profile.

Site Administrator and the Store Owner will have access to the Admin section which allows them to view and monitor site content and assist where required. They will also have the necessary front end access to add, edit and delete music store products and to add and edit subscriptions. As subscriptions are recurring the ability to delete the options has not been provided, as there would be active subscriptions in place and this would need to be managed. They will have access from the front end to add student showcase records.

The Super User will have additional access to the Admin section. Certain models will be limited in terms of being able to create, delete or edit content.

## Structure

### Skeleton

Below is an image of the site structure.


<a href="https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/site-map.pdf">Site Map</a>


### Access

This website will allow users to access different parts of the site depending on whether they're logged in/have an account. 


#### Site visitors
 * View Only:
   * Home Page
   * About Page
   * Privacy Information
 * View and Select:
   * View all Lesson details
   * Lessons - add a lesson to lesson bag
   * Lesson bag - view lesson bag
   * View all Music Store product details
   * Products - add a product to shopping bag
   * Shopping bag - view shopping bag
 * Edit and Delete:
   * Lesson bag - remove lesson from bag
   * Shopping bag - update item quantity and size
   * Shopping bag - remove item from shopping bag
 * Add only:
   * Checkout - order form
   * Checkout - payment information
   * Contact Us - contact form
   * Newsletter Sign Up form
 * Emails:
   * Receive order via email
   * Submitting the contact form triggers an email to the site admin

#### Registered users
Registered users will have the same access as site visitors as well as the following additional access:
 * View only:
    * User profile - order history and detailed information
    * User profile - subscription order information
 * Add only:
   * Checkout - lesson payment information 
   * Checkout - subscription form
   * Checkout - Save details to profile
   * Contact Us - contact form
 * Add, edit and delete:
   * User profile - default information
 * View and cancel:
   * User profile subscriptions
 * Emails:
   * Receive subscription creation via email
   * Receive subscription cancellation via email
 * URLs:
   * Link to stripe to view and download latest invoice
 

#### Site Administrator, Site Owner and Superuser

Initial access groups have been set up for the first launch of the site. Training would need to be provided to ensure staff know what to do. Access to be evaluated on an ongoing basis to ensure that all staff are able to adequately run the business and support their clients.

Front end access in place as stipulated within the project goals section. Lessons and Subscriptions can only be created and edited from the front end as the necessary integration with stripe has been set up to ensure alignment across both sites. Site Admin access to all related models will be view only to ensure that the functionality remains robust.

1. Site Administrator Group
 * View Only:
   * checkout | subscribed customer
   * checkout | subscription line item
   * djstripe | customer
   * djstripe | payment method
   * djstripe | invoice
   * djstripe | invoice item
   * djstripe | payment intent
   * djstripe | payment method
   * djstripe | price
   * djstripe | product
   * djstripe | subscription
   * djstripe | subscription item
   * djstripe | subscription schedule
   * djstripe | upcoming invoice
   * home | user
   * home | user subscription
   * home | subscription line item
   * profiles | user profile
   * store | category
 * View, Edit and Delete:
   * checkout | order
   * checkout | order line item
   * home | contact
    
 * Add, View, Edit and Delete:
   * account | email address
   * account | email confirmation
   * home | cover
   * home | student showcase
   * home | marketing sign up
   * store | music product

2. Site Owner Group

 The site owner will have the same access as the site administrator along with the following additional access:
  * View and Edit:
   * profiles | user profile
  
  * Add, View, Edit and Delete:
   * store | category
   
3. SuperUser
 The Super User will have additional access to the Admin section. Certain models will be limited in terms of being able to create, delete or edit content in alignment with the management of subscriptions.


## Wireframes

The original wireframes created are saved as wireframes-desktop and wireframes-mobile.

Please <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/tree/main/project-files/wireframes">click here</a> to view all wireframes

### Differences
1. I ended up separating the original home page design into a homepage which showed the cover as a full screen over-layed by the simple menu and the about page with the necessary information added separately. I really wanted an impactful home page and this was the best way to achieve that.
2. I added songwriting lessons to the original singing and piano lessons. I followed a djstripe tutorial to complete the subscription set up. For the lessons page I ended up creating each lesson individually instead of having them together per lesson type. Each lesson then had the three different subscription options that a user could choose between. As the page was already long I did not include the store section at the end of the page.
3. Two separate shopping bag icons were added -one for the store and one for subscriptions as the two features had to be kept separate. Two separate checkout processes were created and followed instead of one integrated process. This includes two separate shopping cart sections in the success message. I had also wanted to confirm billing address details in the success messages but it was already so busy I left it out.
4. The workshop feature was removed from scope.
5. I wanted to add the ability to add a product to the shopping bag from the products page, and have the product detail as a pop up, however I stuck to the 'Boutique Ado' tutorial and added the product from the product detail page.
6. My original idea was to have a social media section which would be a student community in which students could post and interact. The original user profile would have been similar to a social media profile. When looking at the detail, it was definitely beyond my ability to create something so complex. A simplified user profile was included, which has all active descriptions displayed and includes the ability to cancel a subscription.
7. I had wanted to complete dropdowns for the lessons, workshops and music store section from within the navigation. However it made sense to include a link to the first page only in the process. Two dropdowns were included in the navigation - one for the My Account section and another for Admin.


## Design
### Colours

The colours for this site are based on the below image and colour palette selected to compliment the image:

![Inspiration Image](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/design/home-background.jpg)

![Palette Image](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/design/colour-scheme/color-palette.jpg)

I was looking for a palette that would inspire and motivate.
The classic black and white photo of a piano player brings sophistication and a sense of tradition to the site. Hopefully this will inspire aspiring musicians to create and celebrate their talent.

Different cover titles and quotes have been set up for the different section. These are inspirational or whimsical quotes which help to differentiate each site section, inspire and engage with the user.

Various sized adverts have been designed to display across the client facing pages to attract new subscribers and shoppers. The showcase advert is there to show off the talent of the students and inspire new students to enrole.



### Fonts
The logo font for the site is 'The Nautigal' with the default font set as sans-serif.

![Nautigal Image](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/design/fonts/the-nautigal.JPG)

The main font used across the body is 'Eb-Garamond' with the default font set as sans-serif.

![Eb-Garamond Image](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/design/fonts/eb-garamond.JPG)

These fonts were chose to provide some sophistication. They are classical and elegant.

## Search Engine Optimisation

A description which is relevant and informative has been included in the meta of base.html: 

"The music studio of Jo-Anna Hope offers online piano lessons, singing lessons and songwriting courses. Includes an online music store to purchase keyboards and other musical instruments and tools."

Utilising Google Search, short keywords and long keyword phases were identified to include across the site to optimise search engine results for the site. These keyword were then run through wordtracker.com to check volume for the search with Google in the UK region.

The list of keywords for the site were narrowed down to:

1. Online piano lessons
2. Online singing lessons
3. Online songwriting course
4. piano lessons
5. singing lessons
6. songwriting course
7. learn to play the piano
8. music shops
9. music store
10. private piano lessons
11. keyboard
12. music

Two site features were used to ensure keywords were included logically within the site pages - the Covers feature - which includes the heading and sub-heading for each page, as well as the adverts sections which are added as articles. I reviewed all html semantics to make sure keywords were placed inside them. Additionally, wherever possible across the pages the key words were included in context. All images and image alt text were re-written to optimise search engine hits. An external link to Yamaha UK was included from the music store, as a reliable external link likely to improve traffic. The Facebook link was left as included for search engine reference, as it opens the actual Facebook business page.

A sitemap.xml file has been included to assist google search to find all page links that do not require logging in. 

A robots.txt file has been included.

A DNS certificate is not included as the site is a student test site only.

All links have been provided with either one of the following relationships:

* “nofollow” for any paid links and distrusted content.
* “sponsored” for any sponsored or compensated links.
   * A sponsored relationship was added for the link to the Facebook Business Page as it is the associated page for Belle Musique Studio
   * All internal adverts for lessons, the store or promotion of students were provided with a sponsored relationship as they are advertising Belle Musique Studio products and services and promoting their students.

## Web Marketing

### Content Marketing

Relevant internal advert sections with links have been included across user-facing pages to promote the music lessons and store products available. The aim of the adverts is to direct the attention of the user to the relevant pages and convert them to customers.

### Social Media Marketing

A Facebook business page for the studio has been set up to ensure organic growth of the business. The site is linked to the business account through the facebook social media link. The Facebook page includes a link back to the site.

<a href="https://github.com/Claire-Potter/Belle-Musique-Studio/tree/main/project-files/facebook-business-page" target="_blank">Click here</a> to access images of the Facebook page.

### Email Marketing

The Student Showcase feature is used as an email marketing tool. It is a weekly update from the studio and includes a link to view the featured student of the week. It includes music lessons and music store advertisements, ensuring that users who have signed up for emails are directed to access our lessons and products. Users will opt-in to receive emails when they register for an account.

## GDPR

A privacy policy was generated through https://www.privacypolicygenerator.info/ and a link to the policy is available in the page footer.


## Business Model

### B2C – Business-to-consumer.

B2C businesses sell to their end-user. This is the business model selected and utilised for Belle Musique Studio. 

![e-commerce business model](https://github.com/claire-potter/belle-musique-studio/blob/main/project-files/design/e-commerce-model.jpg)

* Who is the customer? 
    * The customer is the consumer, the individual by whom the purchased good or service will be used.
* What will they buy?
    * Belle Musique studio supplies music lesson subscriptions and music products. A customer would purchase a recurring subscription for a weekly music lesson or make a once off purchase from the store.
* And how will they pay?
    * All payments will be processed online through stripe.com.
    * They will be secure.
    * Products would require a once off payment to be made.
    * Subscriptions would require a recurring payment set up. The customer will have the choice to set up a weekly, monthly or annual subscription and would be billed accordingly.
* What data would need to be collected and stored?
    * The required data to purchase a product would be:
        * Full Name
        * Email Address
        * Credit Card Details
        * Delivery Address Details
        * Phone Number
    * The required data to take out a recurring subscription:
        * Full Name
        * Email Address
        * Credit Card Details
        * Phone Number
* Would the customer need to be authenticated?
    * For a once off purchase from the store, the customer would not need an account. However, if they wish to store any of their information within the database they would need to register for an account with Belle Musique Studio.
    * To take out a subscription for a weekly music lesson, as recurring payments are required, the customer will need to register and create an account in order to manage the subscription going forward.
* Roles within the e-commerce process:
    * Customer:
        * Subscribes to a lesson or
        * Orders a product
    * Belle Musique Studio Site:
       * Creates the customer and subscription record on Stripe and the database
       * Processes payment with stripe and sets up recurring payments
       * Creates the order and processes the payment through Stripe
       * Collects address details for delivery
    * Site Owner / Administrator:
        * Schedules the weekly online lesson with the customer
        * Provides the service
        * Arranges delivery of the product to the customer

# Database

For development, I used the sqlite3 database that comes with Django. A PostgreSQL database through Heroku is in use 
for the deployed live site.


 <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/dj_stripe_models.png" target="_blank">Database diagram - djstripe models</a>

 <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/belle_musique_studio.png" target="_blank">Database diagram - belle musique studio models </a>

# Features
 
Please access the features file <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/features-read-me.md" target="_blank">here</a>

# Technologies used 

## Languages
* HTML5
* CSS3
* JavaScript
* Python
* Dockerfile - Readme

## Agile Planning

* GitHub and ZenHub were used to plan epics and user stories including acceptance criteria and tasks
* Create and plan Project Backlogs
* Create and plan Sprints and Releases
* Create relative estimates and priority ratings
* A roadmap and relative reports are available to review the development lifecycle and completion progress
* Two workspaces were set up one for the development stage and the other for the design stage, a workflow was set up to automate the movement of the epics and user stories
* An integrated project board was also maintained however this does not offer as much detail as the zenhub board

## Images
Cloudinary used to crop and style the images
ImageOptimizer used to minify image file sizes


## Libraries and Frameworks
* Django was used to create templates and manage the project
* Bootstrap 4 was used to format the site design with their built-in CSS, Popper and JS
* FontAwesome 5.15.3 is used for social links and the rating stars
* Google Fonts is used for fonts on the site
* jQuery used to easily manipulate the DOM and update Bootstrap tools that require initialization
* DJStripe was utilised for the stripe integration for the lesson products and subscriptions
* Stripe was used as the integrated secure payment platform

## Development tools
* Git is used to track changes made to the repository and for version control
* GitHub is used to store the project and to share the project

## Deployment/Hosting
* Heroku is used to deploy and host the live site content


## Payment

The project uses stripe to handle all subscriptions and payments. A free stripe account was created. Products, plans and prices were set up and through DJStripe the models were synced with the project database. Two webhooks were set up one for the product payments and the other for subscriptions. The following configuration was added to settings.py:

    FREE_DELIVERY_THRESHOLD = 40
    STANDARD_DELIVERY_PERCENTAGE = 10
    STRIPE_CURRENCY = 'gbp'
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    STRIPE_LIVE_MODE = False
    STRIPE_TEST_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_TEST_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    DJSTRIPE_WEBHOOK_SECRET = os.getenv('DJSTRIPE_WEBHOOK_SECRET', '')
    DJSTRIPE_FOREIGN_KEY_TO_FIELD = 'id'


## Static and media file storage
* Amazon web services is used for static and media storage
* Create a user, user group, and policy by IAN 
* Then create a new bucket by S3
* Save all media files to AWS bucket
* Add the following configuration to settings.py:
    

         AWS_S3_OBJECT_PARAMETERS = {
              'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
              'CacheControl': 'max-age=94608000', }
              
      AWS_STORAGE_BUCKET_NAME = 'belle-musique-studio'
      AWS_S3_REGION_NAME = 'eu-west-2'
      AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
      AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
      AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
      STATICFILES_STORAGE = 'custom_storages.StaticStorage'
      STATICFILES_LOCATION = 'static'
      DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
      MEDIAFILES_LOCATION = 'media'
      STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
      MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


## Email
* Django.core.mail is used to integrate,  and send emails via gmail.smtp
* Stripe webhooks is used to trigger event related mails

# Testing

Please access the testing pack <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/testing/testing-read-me.md" target="_blank">here</a>

# Deployment

## Required technology

This website was developed on Gitpod using the Code Institute  student template with changes frequently committed to git then pushed onto GitHub from the Gitpod terminal. The deployed site utilises the new version of the python template.

The deployed version of the website is the master.

* Django: to create multiple apps in the project and manage templates
* Python3: write the code and run the project through Django
* PIP: install packages
* Git: version control
* Postgres: as the database to create content, add new content, and manage data
* AWS to store all static files
* Django.core.mail to send emails
* Heroku: to deploy the project and manage the app

## Maintaining Code

To maintain the code the following actions are taken:

1. Log into GitHub
2. Go to the repositories tab at the top of the screen
3. Click on the repository named Belle-Musique-Studio
4. Once in the repository select the green icon GitPod to open the code on GitPod
5. Gitpod will load
6. The belle-musique-studio Main branch will open
7. The belle-musique-studio folders and files will be visible on the left hand side
8. The credentials file env.py has been added to gitignore as it contains sensitive information. This file will need to be created and saved again to the repository
9. You will need to run the following command to install requirements:
    * Pip3 install -r requirements.txt
10. In settings.py ensure Debug is saved as Debug=True, remember to change back to Debug=False before pushing your changes back to GitHub
11. Run the dev site as follows:
    * Python3 Manage.py runserver
12. Create , test and save the change required to the relevant file
13. To save the changes back to github the following process needs to be followed:

    * clear the terminal by typing in "clear" and pressing enter

    *  Add the code to gitpod by typing in  "git add ." in terminal and press enter
    
    * Commit the code to gitpod by typing in "git commit -m "Add a short message here" and press enter
    
    * Push the code back down to github by typing in "git push" select enter
    
    * From the github side, refresh the repository page and the commit will reflect
    
    * Open the item to view the commit changes


## Deployment to Heroku
The website was deployed from GitHub to Heroku using the following steps:

1. Create a new application in Heroku:

    * Navigate to Heroku.com and login.
    * Click on the new button.
    * Select Create New App.
    * Enter a unique app name.
    * Select your current region.
    
2. Set up connection to Github Repository

    * Click the deploy tab and select GitHub - Connect to GitHub.
    * A prompt to find a github repository to connect to will then be displayed.
    * Enter the repository name for the project and click search to find your repository.
    * Click the connect button.
    
3. Add PostgreSQL Database:

    * Click the Resources tab.
    * Under Add-ons seach for Heroku Postgres and then click on it when it appears.

4. Add Dynos:
    * From Git create a procfile with the content: web: gunicorn bellemusiquestudio.wsgi 
    * Save the changes and push through to GitHub
    * Each dyno in your app belongs to one of the declared process types, and it executes the startup command associated with that process type.
    * Click the Resources tab.
    * Select to create Dynos
    * Select to add free Dynos

5. Set environment variables:
    * Click on the Settings tab and then click reveal Config Vars.
    * Login to  AWS account,  .
Copy the access key id and its secret key and save into Heroku's config var as 'AWS_ACCESS_KEY_ID' and 'AWS_SECRET_ACCESS_KEY', and create a 'USE_AWS' variable and set it to 'True'
    * Variables added:


        DATABASE_URL

        SECRET_KEY
        
        USE_AWS = True

        AWS_ACCESS_KEY_ID
        
        AWS_SECRET_ACCESS_KEY
        
        EMAIL_HOST_PASS
        
        EMAIL_HOST_USER - gmail email address
        
        GOOGLE
        
        STRIPE_PUBLIC_KEY
        
        STRIPE_SECRET_KEY
        
        STRIPE_WH_SECRET
        
        DJSTRIPE_WEBHOOK_SECRET



6. Enable automatic deployment:

    * Click the Deploy tab
    * In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

## How to Fork the Repository

1. To be able to fork the repository, you will need your own github and gitpod accounts with linked permissions
2. From your github home page in the search bar search for Claire-Potter
3. Under Users select the user Claire-Potter
4. On the repository page choose to open the Belle-Musique-Studio repository
5. At the top of the page on the right-hand side select to Fork the repository
6. Your own version of the repository will create
7. Select the green GitPod icon to open the work space on GitPod
8. Follow the steps in the Maintaining Code section above to make and save changes to your own repository
9. Remember you will need to create your own version of the env.py file for the credentials
10. Payments will not work unless you set up your own account with Stripe and integrate.
11. An AWS account will be required for static and media files.

# References

## Code

### General Queries

The following were used for any general queries or guidance required:

1. Code Institute LMS
2. Stack Overflow - https://stackoverflow.com/
3. Django 3.2 Documentation - 
https://docs.djangoproject.com/en/3.2/releases/3.2/

### Code Adaptations

1. The base code for this project is from the Code Institute 'Boutique Ado' project

2. Contact form is based on the Contact Form from the Code Institute Resume Project

3. The Subscriptions through DJStripe  was built by following this tutorial 
https://ordinarycoders.com/blog/article/django-stripe-monthly-subscription
4. DJStripe webhook set up according to https://dj-stripe.dev/usage/webhooks/#using-webhooks-in-dj-stripe
5. The following article was used to assist with the setup of subscriptions billing:
https://stripe.com/docs/billing/subscriptions/multiple-products

6. The stripe api guide was referenced to set up the lessons (product) and subscriptions (plans) access for administators to edit and add lessons and subscriptions from the front end:
https://stripe.com/docs/api/products
https://stripe.com/docs/api/plans

6. The instruction to create the apps-models.png image were found here:
https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16

7. The following article was referenced to customise crispyforms:
https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#custom-fields-placement-with-crispy-forms

8. The following tutorial video was followed to embed the videos in Django
https://www.youtube.com/watch?v=dGF1x14QNGA

9. The following site was referenced to complete the html-validator testing - 
https://pypi.org/project/django-html-validator/

10. Dj-stripe documentation referenced for additional set up support: https://dj-stripe.readthedocs.io/_/downloads/en/stable-2.2/pdf/

11. Stripe documentation referenced to understand how products and prices work -https://stripe.com/docs/products-prices/how-products-and-prices-work

12. The Student Showcase Marketing email was set up as per:
https://stackoverflow.com/questions/7583801/send-mass-emails-with-emailmultialternatives

## Content
1. The fictional music studio and Jo-Anna Hope are based on my Aunt Jo Hoult and her music studio
2. The favicon was created on Free Favicon Maker
3. Images sourced through Unsplash and Shutterstock
4. The student showcase video is from the publically available you tube post:
https://www.youtube.com/watch?v=kIN3MX1sYBs
5. Definitions used in site comments are from https://www.fullstackpython.com unless otherwise stated in the code
6. The descriptions used for the models were sourced from the following site:
https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/

## Acknowledgments
A huge thank you to my mentor Brian Macharia. The guidance and advice that you have provided has been invaluable.

Thank you to Code Institute for providing such well-thought out and put together course material and for the constant guidance and advice provided through Slack.

Finally, to my wonderful husband and children, thank you for your understanding and support through this process.
