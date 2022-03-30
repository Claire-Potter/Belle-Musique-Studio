# Features

## Navigation

### Desktop site:
![Navigation Menu Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/01.navigation-desktop.JPG)


### Mobile Site
![Navigation Menu Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/01.navigation-mobile.JPG)

The Navigation Menu falls within the Header. This is created on the template nav.html, which is included in the base template for all site templates. It contains the site logo - Belle Musique, with a music note as a font awesome icon. The Navigation menu is compressed into the navigation hamburger icon. When it is clicked the menu will display at the top of the site. When a nav-item is hovered over, it will highlight yellow.


### Links:
* Home - the home page
* About - the about us page
* Lessons - the lessons page
* Music Store - the music store page
* Contact Us - contact form
* My Account -dropdown menu
    * My Profile - profile page
    * Register - if logged out
    * Login - if logged out
    * Logout - if logged in
* Admin -dropdown menu
     * Staff Only:
           
          *  Site Admin - Django Admin centre
          *  Manage Shop Products - Add a product
          *  Manage Lesson Products - Add a lesson
          *  Showcase a Student - add a student showcase record


### Dropdown Menus

The My Account section is a dropdown menu containing the Login/Register/Logout links and My Profile link. The Admin section is a dropdown menu containing the link to Site Admin and the front end product and lesson management pages and student showcase page. 
The dropdown action is completed through the JavaScript script.js

#### Dropdown Desktop:

![Dropdown Menu Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/02.dropdown-desktop.JPG)

#### Dropdown Mobile:

![Dropdown Menu Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/02.dropdown-mobile.JPG)

## The Home Page

### Desktop Site
![Home Page Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/03.home-page-desktop.JPG)

### Mobile Site
![Home Page Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/03.home-page-mobile.JPG)

* The Home Page displays the background cover image in full
* The cover has been added using the bootstrap cover categories
* It includes a summarized menu for users to easily access the main pages and provides clear direction as to next action
* It is welcoming and sets the tone for the site
* The home page renders well across screen sizes


## The Cover

### Desktop Site
![Cover Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/06.cover-desktop.JPG)
### Mobile Site
![Cover Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/06.cover-mobile.JPG)

* The Cover exists across all site pages. It contains the same background image.
* The page title and the sub-title are updated according to each page. Keywords have been included in these sections where relevant.
* A Cover model stores the title and sub-title per page and this is called in the various views.py files.
* If tags are used to determine the different style classes depending on the cover page.

## The Footer

### Desktop Site
![Footer Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/24.footer-desktop.JPG)
### Mobile Site
![Footer Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/24.footer-mobile.JPG)


* The Footer contains the creation date and designer details
* It has been styled in a darker blue colour to create contrast with the white font
* The Social Media link icons are displayed in the footer
* Each of these icons will open the respective social media site on a new blank page ensuring the user has easy access to the Xperience DezignWiz social accounts
* The Facebook link opens the actual business page of Belle Musique Studio
* The Privacy Info opens the privacy policy document for the site on a new blank page
* The Newsletter link opens the newsletter form for a user to sign up for the weekly student showcase newsletter.


## The About Us page

### Desktop Site
![About Us Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/04.about-page-desktop.JPG)


### Mobile Site
![About Us Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/04.about-page-mobile.JPG)


* The Home Screen contains a link to the About page 
* The user should have an understanding of what to expect from the site after they have read through the page
* The about page can also be accessed from within the navigation menu
* A back to top arrow is included at the end of the screen, whcih allows the user to quickly navigate back to the top of the screen
* The About page contains the following sections:
    * Get to know Jo-Anna Hope
      * An image of the music teacher and a summary of who she is, what she does and what the studio offers. It allows the user to get to know her as a person as well as what they can expect as a student
    * Music Lessons
        * A summary of lessons are provided, time frame, weekly and monthly cost and the annual subscription special. It gives the user a quick overview and a link to access the lessons page.
    * Student Showcase
      * The section in which the weekly student showcase is posted
    * Music Store Link
       * Separate options for the user to visit the music store and view all products, musical tools or instruments and equipment

## Student Showcase

The Student Showcase section is updated weekly by the site owner or site administrator via the front end add student showcase form. It includes an image, excerpt, body, and video. It is an important section within the site as it allows the owner to showcase the skills of her students, which also provides an excellent form of advertisement to site browsers as they can see first hand what the lessons deliver. It is also an important section for existing customers, as it allows them to show off their own talent and creates something to work towards - to be selected as the student of the week. When a new record is added, the latest record will pull through to the about page.

When a new student showcase record is captured, a marketing email will be sent out to all users who have signed up to receive marketing newsletters from the site. This will provide them with an overview of the showcased student as well as an opportunity to advertise the lessons and music store products.

No approval from the subscribed customer is currently required on the site for the site owner to post about them - this is a future enhancement to be completed and if it were a live site, approval would need to be asked for before posting about any individual.

### Student Showcase
#### Desktop Site
![Student Showcase Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-desktop.JPG)


#### Mobile Site
![Student Showcase Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-mobile.JPG)

### Add Student Showcase
![Student Showcase Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-form.JPG)

### Newsletter Sign Up
![Newsletter Sign Up](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.newsletter.JPG)

### Marketing Email
![Student Showcase Email](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-email.JPG)


## The Lessons Page

### Desktop Site
![Lessons Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-desktop.JPG)

### Mobile Site
![Lessons Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-mobile.JPG)

* The Lessons page returns the details on all of the available lessons that the studio offers.
* A back to top arrow is included at the end of the screen, whcih allows the user to quickly navigate back to the top of the screen.
* Each lesson displays a relevant image, the lesson name which includes the length of the lesson and a lesson description.
* The lessons are created in the DJStripe Products model.
* Included with each lesson are three subscription pricing plans, a weekly plan, a monthly plan and an annual plan.
* The plans are created in the DJStripe Plan and Pricing models which have a foreign key relationship with the Product model.
* A select button is available below each plan to allow the user to select the lesson and plan. The lesson is selected through the Javascript script attached to the page.
* Only one lesson and plan can be selected, once selected it will reflect in the Selected Lesson section at the end of the page.
* To change their selection, the user just needs to click select under another option.
* When they are ready they can click the Add to Bag button which will submit the form and add the lesson and plan to the shopping bag. The Add to Bag button will bee disabled until a selection has been made to prevent the user from submitting an empty form.
* An alternative return home button is available to allow the user to return to the home page.
* Once the lesson has been selected and reflects in the lesson bag, the select and add to bag buttons will be disabled to prevent the user from adding another lesson to the bag as the checkout process is only handled to equip one subscription activation and payment per process.

### Edit a Lesson

#### Edit Lesson Page
![Edit Lesson Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-edit-form.JPG)

* As a staff member I can select the edit button and the Edit a Lesson page will open.
* As a site user, the Edit button will not reflect on the page.
* An Alert message will display to let me know which lesson I am editing.
* The current lesson and plans details will pull through to the form.
* The form is set up to allow me to edit certain lesson details and plan details. Three plan sections are included (referred to as prices on the front end site) one for each linked plan.
* Fields which are not allowed to be edited, according to the DJStripe model set up have been grayed out.
* An update lessons button allows me to update and submits the form. The models will be updated within the database and integration through to stripe will ensure the applicable updates will take place on stripe.
* A success message is displayed when a lesson is successfully updated.
* A cancel button exits the page and returns to the lessons page.

### Add a Lesson

#### Add a Lesson Page

![Add a Lesson Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-add-form.JPG)

* As a staff member I can select the Manage Lesson Products option under the Admin dropdown menu and the Add a Lesson page will open.
* As a site user, the option will not reflect on the menu.
* A new form will display, with placeholder text explaining the different fields.
* The form is set up to allow me to add lesson details and plan details. Three plan sections are included (referred to as prices on the front end site) one for each linked plan.
* Fields which should have standard values to align with other products have been pre-populated and are grayed out.
* The Active checkbox has been pre-selected.
* An add lesson button allows me to submit the form. Fields are validated and the form will not submit if missing relevant fields. The models will be updated with the new lesson within the database and integration through to stripe will ensure the lesson and plans will will be created on stripe.
* A success message is displayed when a lesson is successfully updated.
* A cancel button exits the page and returns to the lessons page.
* The new lesson reflects on the lessons page.
    

## The Music Lesson Bag

### Desktop Site
![Lesson Bag Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/08.music-lesson-bag-desktop.JPG)

### Mobile Site
![Lessons Bag Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/08.music-lesson-bag-mobile.JPG)

* When a lesson is selected and submitted, the success message will display a smaller version of the music lesson bag with a summary.
* The Music Lesson Bag logo in the header, will now reflect the total cost of the lesson.
* When a site user clicks on the music lesson bag icon, the Music Lesson Bag page will open.
* The following information will be displayed:
   * Image
   * Lesson information including plan
   * Quantity 
   * Price
* A Remove button is available which will remove the lesson from the bag for the user.
* The bag total will display and the user can select secure checkout to move on to the checkout page.
* Three adverts exist at the bottom of the screen each with a link to the advertised page.
* The display for the mobile view does not include a table, it displays the items one after the other with the bag total and checkout button displayed on top. The back to top arrow is included on smaller screens.


## Music Lesson Checkout

#### Desktop Site
![Music Lesson Checkout Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-payment-desktop.JPG)

#### Mobile Site
![Music Lesson Checkout Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-payment-mobile.JPG)

* Only users with an account can proceed to subscribe to lessons as recurring payments are required.
* Site browsers will be referred to the login page.
* The summarised lesson details reflect correctly on the checkout page with the subtotal and order total reflecting correctly.
* The site user can capture their credit card number in the payment element - which is generated through integration with stripe.
* The site user can select the change subscription button which will take them back to their lesson bag to remove the lesson.
* The site user can select subscribe to proceed with the subscription creation
* The customer, subscription and payment will be created on stripe and returned. If a customer already exists, the subscription will be added against the same customer account on stripe.
* The site user will proceed to the successfully subscribed page.
* The site user can complete their personal details and additional details and select finalise to finalise their subscription.
* The site user can choose to cancel the subscription, which will cancel the subscription on Stripe and delete it from the database. The site user will be returned to their profile page.
* If the site user finalises their subscription, they will be directed to the lesson complete page.
* An email confirming their subscription details will be sent to their email address provided.
* A subscription summary will be provided on the subscription complete page.
* A success message containing the details will be displayed.
* A link to the latest invoice for the subscription will be available.
* If the user opens the link, it will open on a new page and the user has access to view or download the stripe invoice.
* The music lesson bag will now be empty.


#### Desktop Site

![Music Lesson Subscribe Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-subscribe-desktop.JPG)
![Music Lesson Complete Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-complete-desktop.JPG)
![Stripe Invoice](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-stripe-invoice.JPG)

#### Mobile Site

![Music Lesson Subscribe Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-subscribe-mobile.JPG)
![Music Lesson Complete Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-complete-mobile.JPG)


## Music Store

### Desktop Site
![Music Store Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/10.music-store-desktop.JPG)

### Mobile Site
![Music Store Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/10.music-store-mobile.JPG)

* The music store provides the site user with three different store views to choose from. The products will display according to these categories:
    * All Products
    * Music Tools
    * Instruments and Equipment
* When the site user clicks on the shop now link under the category the relevant product view will open.
* A back to top arrow is included at the end of the screen, which allows the user to quickly navigate back to the top of the screen
* A link to Yamaha to check out their products is included.
* Two adverts display at the end of the music store page, one for music lessons and the other for student showcase.
* The advert buttons will take the site user to the relevant page with further information.


## Products page

### Desktop Site
![Products Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-desktop.JPG)

### Mobile Site
![Products Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-mobile.JPG)

* The products page will render differently depending on which category is selected:
    * All Products - returns all store products
    * Music Tools - returns music support tools such as a metronome and music sheets
    * Instruments and Equipment - returns keyboards and sound equipment
* The product category and product count reflect at the top right of the page.
* A menu is available to select to sort the product items by various different views:
     * Price - low to high and high to low
     * Rating - low to high and high to low
     * Name - A to Z and Z to A
     * Category A to Z and Z to A
* Selecting each view will sort the products accordingly
* A product image, title, price, category and rating displays per product item.
* If a user is a staff member they will have the edit and delete buttons available to them.
* If a user is not staff, these buttons will not display
* If a user clicks on the product image, the product detail page will open in a new tab.
* A back to top arrow is included at the end of the screen, which allows the user to quickly navigate back to the top of the screen.
* A return button will take the site user back to the music store page.

### Edit a Product

#### Edit Product Page
![Edit Product Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-edit-form.JPG)

* As a staff member I can select the edit button and the Edit a  Product page will open.
* As a site user, the Edit button will not reflect on the page.
* An Alert message will display to let me know which  product I am editing.
* The current product details will pull through to the form.
* An update product button allows me to update and submits the form. The model will be updated within the database.
* A success message is displayed when a product is successfully updated.
* A cancel button exits on the page and returns to the products page.

### Add a Product

#### Add a  Product Page

![Add a  Product Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-add-form.JPG)

* As a staff member I can select the Manage Shop Products option under the Admin dropdown menu and the Add a Product page will open.
* As a site user, the option will not reflect on the menu.
* A new form will display.
* The form is set up to allow me to add product details. 
* An add product button allows me to submit the form. Fields are validated and the form will not submit if missing relevant fields. The model will be updated with the new product.
* A success message is displayed when a product is successfully updated.
* A cancel button exits on the page and returns to the products page.
* The new product reflects on the lessons page.

## Product Detail Page

### Desktop Site
![Product Detail Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/12.product-detail-desktop.JPG)

### Mobile Site
![Product Detail Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/12.product-detail-mobile.JPG)

* The product detail page displays a product image, title, price, category, rating and description per product item.
* A quantity selection tool is available to the site user to increase or decrease the amount of items they would like to select.
* It validates to ensure the value is not less than 1 and not greater than 99
* By selecting add to bag, the selected quantity of the product is added to the shopping bag.
* A success message displays which includes a mini version of the shopping bag. 
* The total amount now reflects under the shopping bag icon.
* A keep shopping button is available which will return the user to the products page.

## The Shopping Bag

### Desktop Site
![Shopping Bag Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/13.shopping-bag-desktop.JPG)

### Mobile Site
![Shopping Bag Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/13.shopping-bag-mobile.JPG)

* When a product is selected and submitted, the success message will display a smaller version of the shopping bag with a summary.
* The Shopping Bag logo in the header, will now reflect the total cost of the bag.
* When a site user clicks on the shopping bag icon, the Shopping Bag page will open.
* The following information will be displayed:
   * Image
   * Product Info
   * Price 
   * Quantity
   * Sub-Total
* A Remove button is available which will remove the product from the bag for the user.
* The user is able to increase or decrease the quantity of a product through the quantity selector.
* When the user clicks the update button the new quantity will be updated and confirmed through a success message.
* The user will be told how much they still need to spend to receive free delivery in red text (if they are not over the threshold as yet).
* The bag total, delivery and grand total will display and the user can select secure checkout to move on to the checkout page.
* A keep shopping button will return the user to the products page.
* Multiple product items can be added to the bag at the same time.
* Three adverts exist at the bottom of the screen each with a link to the advertised page.
* The display for the mobile view does not include a table, it displays the items one after the other with the bag total and checkout button displayed on top. The back to top arrow is included on smaller screens.


## Checkout

### Desktop Site
![Checkout Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-desktop.JPG)

### Mobile Site
![Checkout Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-success-mobile.JPG)

* All users, including those without an account can process to checkout and purchase products.
* The summarised product details reflect correctly on the checkout page with the subtotal, order total, delivery and grand total reflecting correctly.
* The site user can complete their personal details and delivery details.
* If the site user has an account they can select to save these details to their profile.
* If they do not, they will be told that they can login or create an account in order to save their details.
* The site user can capture their credit card number in the payment element - which is generated through integration with stripe.
* The site user can select the adjust bag button which will take them back to their shopping bag.
* The site user can select checkout to proceed with the payment.
* The payment will be processed on stripe.
* The site user will proceed to the checkout success page.
* An email confirming their order details will be sent to their email address provided.
* An order summary will be provided on the page.
* A success message containing the details will be displayed.
* The shopping bag will now be empty.


### Desktop Site
![Checkout Success Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-success-desktop.JPG)

### Mobile Site
![Checkout Success Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-success-mobile.JPG)



## Contact Us

### Desktop Site
![Contact Us Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/15.contact-us-desktop.JPG)

### Mobile Site
![Contact Us Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/15.contact-us-mobile.JPG)
  
* A Site User is able to capture a message via the contact us page and submit the request.
* A Site User can submit a request whether they have an account or not.
* If they have an account their full name and email address will be generated from their user record. Their username will reflect against their contact request.
* The contact request is saved and admin can access it from the Admin site. 
* An email is sent to the admin email address containing the name, email address and contact message of the user.

## Marketing and Advertising

### Desktop Site
![Adverts](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-desktop.JPG)
![Banner](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-desktop-banner.JPG)

### Mobile Site
![Adverts](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-mobile.JPG)
![Banner](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-mobile-banner.JPG)

* Across the site various internal advertisements are placed to market lessons and products.
* All adverts contain links to the relevant pages where a user can view lessons and products.
* The language is enticing.
* The Student Showcase advert leads the user to view the student showcase section which demonstrates the results of lessons.
* When a new student showcase is added, an email is sent to those who have opted in for emails, this includes links to lessons and products.
* An advert banner at the top of the page provides details on lessons, the free music lesson if a user subscribes annually and the free delivery threshold.

## Account Management


### Register for an account

#### Desktop Site
![Register](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/18.register-desktop.JPG)


#### Mobile Site
![Register](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/18.register-mobile.JPG)


* A customised registration form has been created for new users to register for an account.
* The new site user will need to provide an email address, username, first name, last name and password.
* An optional checkbox for marketing opt in selection is provided for new users to opt in to receive emails. An option to opt out of emails from their user profile will be a future enhancement.
* Once the user has selected to sign up, a verification email will be sent to the provided email address.


### Verification Email

#### Desktop Site
![Verify](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.verify-desktop.JPG)
![Confirm](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.confirm-desktop.JPG)

#### Mobile Site
![Verify](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.verify-mobile.JPG)
![Confirm](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.confirm-mobile.JPG)


* Once I have successfully registered an email confirmation is sent.
* The email confirmation is received in the email inbox I have registered with.
* A link in the confirmation email takes me to confirm my email and login to my account.
* I can successfully login to my account.


### Login and Logout

#### Desktop Site
![Login](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.login-desktop.JPG)
![Logout](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.logout-desktop.JPG)

#### Mobile Site
![Login](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.login-mobile.JPG)
![Logout](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.logout-mobile.JPG)

* A non-logged-in will have the option to register or log in from their navigation.
* A site user can easily log in to their account by accessing the navigation menu and selecting login. 
* A site user will have the option to login with their Facebook or Google account.
* A site user can add their username and password and submit to login to their account.
* A success message will display when logged in.
* When logged in the user can update their personal user profile and view/action restricted pages/content for logged-in users only.
* Once logged in they will have the option to logout from their navigation.
* When a site user selects to logout the site will log them out and confirm with a success message.


### Password Recovery

#### Desktop Site
![Password Reset](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/21-password-reset-desktop.JPG)

#### Mobile Site
![Password Reset](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/21.password-reset-mobile.JPG)

* From the login screen I can access the Forgot Password button.
* I can enter my email address on the password reset page and submit.
* A reset password email with a link will be sent to my email address.
* I can open the link and reset my password and proceed to login to my account.

## User Profile

### Desktop Site
![User Profile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/22.user-profile-desktop.JPG)

### Mobile Site
![User Profile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/22.user-profile-mobile.JPG)

* I can save my delivery details to my user profile when I place an order.
* The details will be returned to the order form when I create a future order.
* I can view past orders and open the order information details from my profile.
* I can view all active subscriptions and open the subscription information from my profile.
* I can select to cancel a subscription from my profile, it will cancel and I will be returned to my profile page.

## Admin Access

### Groups
![Super User](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/23.super-user-group.JPG)
![Store Owner](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/23.site-owner-group.JPG)
![Site Administrator](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/23.site-admin-group.JPG)


* All staff roles can access the front end site pages.
* Site Owner has specific access assigned which restricts what they have access to view, edit, create and delete within the site admin section.
* Site Administrator has specific access assigned which restricts what they have access to view, edit, create and delete within the site admin section.
* Super User has full access apart from restrictions in code and only applicable djstripe models reflected in site admin.
