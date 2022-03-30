# Testing

## Responsiveness and Compatibility

1. Lambda Test was used to check the site on different browsers and operating systems:
    * Safari
    * Chrome
    * Firefox
    * Edge
    * Opera
    * The site is compatible and accessible across all browsers.
    * Please click here to view browser testing screenshots.
    
2. Devices and Screen Sizes

    * The site was tested using the Responsively App as well as the Google Chrome device tool bar. The site has been set up to render effectively across multiple screen sizes and devices. I have tested using the following device displays:
    
    * Responsively App:
        * 5K Display 5120 * 2880
        * 4K Display 3840 * 2160
        * MacBook Pro 16 inch 3072 * 1920
        * MacBook Pro 15 inch 2880 * 1800
        * MacBook Pro 13 inch 2560 * 1600
        * Laptop with HiDPi Screen 1440 * 900
        * Laptop 1400 * 1000
        * MacBook Air 1440 * 900
        * Laptop with MDPi Screen 1280 * 800
        * Generic Laptop 1280 * 950
        * iPad Pro 1024 * 1366
        * Kindle Fire HDX 800 * 1280
        * iPad 768 * 1024
        * Microsoft Lumia 550 640 * 360
        * Blackberry Playbook 600 * 1024
        * Nokia N9 480 * 854
        * iPhone 6/7/8 Plus 414 * 736
        * iPhone 6/7/8 375 * 667
        * Galaxy S 5 360 * 640
        * iPhone 4 320 * 480
        * JioPhone 2 240 * 320
        * Responsive Mode - change the screen width to test various sizes
        
    * Google Chrome device tool bar:
        * Galaxy Note 3
        * Galaxy Note II
        * Galaxy S III
        * KindleFire HDX
        * LG Optimus L70
        * Laptop with HiDPI screen
        * Laptop with MDPI screen
        * Laptop with touch
        * Microsoft Lumia 550
        * Microsoft Lumia 950
        * Moto G4
        * Galaxy S5
        * Pixel 2
        * Pixel 2 XL
        * iPhone 5/SE
        * iPhone 6/7/8
        * iPhone 6/7/8 Plus
        * iPhone X
        * iPad
        * iPad Pro
        * Surface Duo
        * Galaxy Fold
        * Responsive Mode
        
        
## Code Validation

1. W3C HTML Code Validator
    * The code for all html pages was entered into the validator and all pages passed excluding the django templates tags.
          
2. W3C CSS Jigsaw Validator
    * The code for the following style sheets were entered into the validator and passed excluding the google fonts import:
    * style.css
    * checkout.css
    * lessons.css
    * profile.css
    
    Please <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/tree/main/project-files/testing/css-validation" target="_blank">click here</a> to view the screenshots.
    
3. JScript Code Validator
    * The code for the following Javascript scripts pages was entered into the validator passed:
        * script.js
        * stripe_elements.js
        * stripe_subscriptions.js
        * submit_overlay.js
        * checkbox.js
        * countryfield.js
      
      Please <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/tree/main/project-files/testing/javascript-validation" target="_blank">click here</a> to view the screenshots.
        
4. All .py files passed through pep-8 online successfully:

   Please <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/tree/main/project-files/testing/pep-8%20validation" target="_blank">click here</a> to view the screenshots.
 
5. Flake8 ran within the console returned no errors:
   ![Flake 8 test result](https://github.com/claire-potter/belle-musique-studio/blob/main/project-files/testing/pep-8%20validation/flake8%20validation.jpg)

6. Pycodestyle ran within the console returned no serious errors:
   Please <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/tree/main/project-files/testing/pycodestyle-validation" target="_blank">click</a> here to view the screenshots.

## Testing Accessibility

The Wave Evaluation Tool was used to test the Accessibility of the site.

I had to make some changes to make sure I could pass the accessibility testing as best as possible. All pages note mentioned below, did not have any errors.

Please <a href="https://github.com/Claire-Potter/Belle-Musique-Studio/tree/main/project-files/testing/wave-accessibility" target="_blank">click here</a> to view the Wave screenshots.

**Home page:**

There was an incorrectly labeled role in the navigation menu which was changed.

Three contrast errors were received:
The footer content on the homepage was picked up as low contrast. I had purposely left out the footer background on the homepage as I liked the effect of the full background image. I added the footer colour back for the home page.

**About page:**

The links to the store contained no text. This was corrected.

**Lessons page:**

The seven errors received were all in relation to hidden form fields which are referenced in the Javascript and not visible to any users. They remain as is.

**Product Details page:**

Three errors were found relating to the quantity field. Aria-labels were added.

**Shopping Bag:**

Seven errors were corrected by adding aria-labels to the form elements that did not have labels and by adding content to an empty table header.

**Checkout:**

Nine errors were corrected by fixing the alt tag input for the  product image, and adding aria-labels to the form.

**Lesson Bag:**

Three empty table headers existed which were corrected.

**Profile:**

Nine errors were corrected by adding aria-labels to the form.


## Performance:

Google lighthouse utilised to test performance of site and mobile. Please see reports attached here.

I used the tool ImageOptimizer to resize all images to improve performance.


## Automated Tests

### Snyk Validation

* About:
 * Snyk Open Source
 * Automatically detect vulnerabilities and accelerate fixing throughout your   development process

* The following steps were followed to run the snyk integration
1. Set up a free Snyk Account
2. Set up integration with git hub
3. Select a project from the Snyk dashboard - choose which GitHub repository 
   to run Snyk validation for
4. Wait for the validation report to generate
5. A pull request will auto-generate to update requirements.txt with new        versions to solve vulnerabilities
6. Run the pull request
7. Check for any version issues - for example I could not upgrade from urllib3 1.25.7 as that specific version was required
8. Change the version back to the required version through pip

Please see Snyk screenshots here

## Django Extensions

### Validate-template

The validate-template test was created in home - tests.py and run for all templates.

Before:

After corrections:


## HTML-Validator 

The html-validator test was run for all templates.

It was installed as follows:

1. Install django-extensions
2. Add to apps list
3. Install html-validator
4. Set up html-validator middleware
5. Add the html-validator settings to settings.py
6. Enable and open each site page for validation file to be generated.
7. Only if a template contains an error will the txt file be created and displayed in the console, therefore there are no screenshots for templates once errors were corrected.

Please click here to view the results.

## Spell Checker

Code Spell Check was installed as an extension and used continuously
to check spelling when coding.
About:

Example:


## Bugs and Issues

### Payments vs. Subscriptions

My original idea was to set up a subscription section to offer lesson subscriptions, shorter courses as well as a workshop section to offer workshop bookings. I wanted it to work alongside the music store product payment functionality. A user would be able to use one shopping bag and add store products, short courses, workshop bookings and subscriptions to the same shopping bag and proceed with payment.

Due to time restraints I did not proceed with the workshop and short courses creation.

To create an integrated shopping bag and checkout process turned out to be extremely complicated to achieve due to the API with stripe, processing payments as well as having to create a customer and a subscription. I had already set up my store, shopping bag and checkout app according to the 'Boutique Ado' project.  I utilised a djstripe library and a tutorial to create subscriptions, this only processed one subscription at a time. I then went to try to include the subscription code alongside the store product code for shopping bag and checkout. I really wanted an aligned user experience.

The processes were too different and complicated to include in one view so I ended up building a completely separate music lesson shopping bag and checkout process. I tried to align it to the store product process as far as possible. It is set up to only process one subscription at a time, however I kept the music lesson bag as a future enhancement would be to include short courses as part of the lesson section, and add multiple short courses to the music lesson bag to be purchased together. The subscriptions would then not need to be added to the bag but from the lesson page a user would proceed directly to checkout and payment.

The double shopping bag and music lesson bag reflecting in the success message is a bit confusing and as a future enhancement I would look at how best to separate these two views. It is left as is for now, as it is important for a user to be able to perform both shopping processes at the same time, without them interfering with each other.

### Webhooks

I had an issue when setting up the webhooks. I could not get them to succeed no matter how often I tried. I then decided to deploy my site and see if it was because of the dev website address. This indeed was the reason and the webhooks were working successfully.

The djstripe webhook is setup and succeeding. I however struggled to send the confirmation and cancellation emails through the webhook. Due to time, I ended up sending the confirmation and cancellation emails from the views.py file instead.


## Feature and User Story Testing

### Feature: Navigation

* The site has a navigation menu, which displays on the desktop and resizes appropriately for smaller screens
    * Pass
* All menu options are readable and all links direct the user to the correct pages
    * Pass
* The Navigation menu is created within the header and is styled according to the site design
    * Pass

#### User Story
As **a User** I can **easily Navigate across all site pages** so that **I can view all content logically and without hassle**

#### Acceptance Criteria
* The Navigation menu is located in a visible page section
    * Pass
* The menu items are logical and all links open the correct pages
    * Pass
* The Navigation menu items will display according to the user's logged in status
    * Pass
* If the user is a staff member, they will also have access to the Admin site and additional pages
    * Pass
* The Navigation menu will re-size for smaller screens and will display as a the navigation 'hamburger'
    * Pass

#### Desktop Site 
![Navigation Menu Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/01.navigation-desktop.JPG)


#### Mobile Site
![Navigation Menu Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/01.navigation-mobile.JPG)

### Feature: Home Page

* The Home Page displays a beautiful and well rendered background image
    * Pass
* This cover is created as a bootstrap cover and covers the entire page
    * Pass
* The home page renders well across screen sizes
    * Pass
* The Home Page provides clear direction as to next action required by providing a menu with the main page links
    * Pass

#### Desktop Site

![Home Page Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/03.home-page-desktop.JPG)

#### Mobile Site
![Home Page Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/03.home-page-mobile.JPG)


### Feature: The Cover

* The Cover exists across all site pages. It contains the same background image.
    * Pass
* The page title and the sub-title are updated according to each page. Keywords have been included in these sections where relevant.
    * Pass
* A Cover model stores the title and sub-title per page and this is called in the various views.py files and the correct cover is returned.
    * Pass

* If tags are used to determine the different style classes depending on the cover page and the page updates accordingly.
    * Pass

### Desktop Site
![Cover Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/06.cover-desktop.JPG)
### Mobile Site
![Cover Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/06.cover-mobile.JPG)


### Feature: The Footer

* The Footer contains the creation date and designer details
    * Pass
* It has been styled in a darker blue colour to create contrast with the white font
    * Pass
* The Social Media link icons are displayed in the footer
    * Pass
* Each of these icons will open the respective social media site on a new blank page ensuring the user has easy access to the Belle Musique Studio social accounts
    * Pass
* The Facebook link opens the actual business page of Belle Musique Studio
    * Pass
* The Privacy Policy opens the privacy policy document for the site on a new blank page
    * Pass


#### Desktop Site
![Footer Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/24.footer-desktop.JPG)
#### Mobile Site
![Footer Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/24.footer-mobile.JPG)


### Feature:  The About Us page

* The Home Screen contains a link to the About page 
    * Pass
* The user should have an understanding of what to expect from the site after they have read through the page
    * Pass
* The about page can also be accessed from within the navigation menu
    * Pass
* A back to top arrow is included at the end of the screen, whcih allows the user to quickly navigate back to the top of the screen
    * Pass
* The About page contains the following sections:
    * Get to know Jo-Anna Hope
       * Pass
    * Music Lessons
        * Pass
    * Student Showcase
      * Pass
    * Music Store Link
       * Pass


#### User Story

As a **Site User** I can **understand the site purpose** so that **my expectations of the site are set**

#### Acceptance Criteria
  
* As soon as a user enters the site they should be presented with the site purpose
    * Pass
* This should be easily understood and provide the necessary directions required
    * Pass
* The user should have an understanding about what to expect
    * Pass
    
#### Desktop Site
![About Us Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/04.about-page-desktop.JPG)


#### Mobile Site
![About Us Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/04.about-page-mobile.JPG)


### Feature: Student Showcase

* Front end form provided for a staff member to capture a new student showcase record. It can be completed and saved successfully. It includes the necessary validations.
    * Pass
* The latest student showcase record is displayed on the about page
    * Pass
* The video and image resize according to screen size
    * Pass
* A marketing email is triggered and successfully delivers to all users who have opted in to receive marketing.
    * Pass
    

#### User Story
    
As the **Site Owner / Site Admin** I can **showcase a student on the about page** so that **I can show off their talents**
  

#### Acceptance Criteria
  
* A Site Owner / Admin can create posts that will be displayed on the About page.
    * Pass
* The post will include an image and a video if uploaded
    * Pass
* The customer and subscription are linked to the post
    * Pass
  

#### Student Showcase
##### Desktop Site
![Student Showcase Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-desktop.JPG)

##### Mobile Site
![Student Showcase Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-mobile.JPG)

#### Student Showcase Form

![Student Showcase Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-form.JPG)

#### Student Showcase Email

![Student Showcase Email](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/05.student-showcase-email.JPG)
    
### Feature: Lessons

* The Lessons page returns the details on all of the available lessons that the studio offers.
    * Pass
* A back to top arrow is included at the end of the screen, which allows the user to quickly navigate back to the top of the screen
    * Pass
* Each lesson displays a relevant image, the lesson name which includes the length of the lesson and a lesson description.
    * Pass
* The lessons are created in the DJStripe Products model.
    * Pass
* Included with each lesson are three subscription pricing plans, a weekly plan, a monthly plan and an annual plan.
    * Pass
* The plans are created in the DJStripe Plan and Pricing models which have a foreign key relationship with the Product model.
    * Pass
* A select button is available below each plan to allow the user to select the lesson and plan. The lesson is selected through the Javascript script attached to the page.
    * Pass
* Only one lesson and plan can be selected, once selected it will reflect in the Selected Lesson section at the end of the page.
    * Pass
* To change their selection, the user just needs to click select under another option.
    * Pass
* When they are ready they can click the Add to Bag button which will submit the form and add the lesson and plan to the shopping bag. The Add to Bag button will bee disabled until a selection has been made to prevent the user from submitting an empty form.
    * Pass
* An alternative return home button is available to allow the user to return to the home page.
    * Pass
* Once the lesson has been selected and reflects in the lesson bag, the select and add to bag buttons will be disabled to prevent the user from adding another lesson to the bag as the checkout process is only handled to equip one subscription activation and payment per process.
    * Pass

### User Stories

As a **Site User** I can **view available lessons offered** so that **I can subscribe**

#### Acceptance Criteria

Info on singing lessons displays
    * Pass
Info on piano lessons displays
    * Pass
*Info on songwriting lessons displays
    * Pass
The links are clickable and direct the user to order a subscription
    * Pass

As  a **Site User** I can **view singing lessons offered** so that **I can subscribe**
  
#### Acceptance Criteria
  
* View details on singing lessons
    * Pass
* View various options available
    * Pass

As  a **Site User** I can **view piano lessons offered** so that **I can subscribe**
  
#### Acceptance Criteria
  
* View details on piano lessons
    * Pass
* View various options available
    * Pass

As  a **Site User** I can **view songwriting lessons offered** so that **I can subscribe**
  
#### Acceptance Criteria
  
* View details on songwriting lessons
    * Pass
* View various options available
    * Pass
  

#### Desktop Site
![Lessons Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-desktop.JPG)

#### Mobile Site
![Lessons Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-mobile.JPG)

#### Edit a Lesson

* As a staff member I can select the edit button and the Edit a Lesson page will open.
    * Pass
* As a site user, the Edit button will not reflect on the page.
    * Pass
* An Alert message will display to let me know which lesson I am editing.
    * Pass
* The current lesson and plans details will pull through to the form.
    * Pass
* The form is set up to allow me to edit certain lesson details and plan details. Three plan sections are included (referred to as prices on the front end site) one for each linked plan.
    * Pass
* Fields which are not allowed to be edited, according to the DJStripe model set up have been grayed out.
    * Pass
* An update lessons button allows me to update and submits the form. The models will be updated within the database and integration through to stripe will ensure the applicable updates will take place on stripe.
    * Pass
* A success message is displayed when a lesson is successfully updated.
    * Pass
* A cancel button exits the page and returns to the lessons page.
    * Pass
    

#### Add a Lesson

* As a staff member I can select the Manage Lesson Products option under the My Account dropdown menu and the Add a Lesson page will open.
    * Pass
* As a site user, the option will not reflect on the menu.
    * Pass
* A new form will display, with placeholder text explaining the different fields.
    * Pass
* The form is set up to allow me to add lesson details and plan details. Three plan sections are included (referred to as prices on the front end site) one for each linked plan.
    * Pass
* Fields which should have standard values to align with other prodcuts have been pre-populated and are greyed out.
    * Pass
* The Active checkbox has been pre-selected.
    * Pass
* An add lesson button allows me to submit the form. Fields are validated and the form will not submit if missing relevant fields. The models will be updated with the new lesson within the database and integration through to stripe will ensure the lesson and plans will will be created on stripe.
    * Pass
* A success message is displayed when a lesson is successfully updated.
    * Pass
* A cancel button exits the page and returns to the lessons page.
    * Pass
* The new lesson reflects on the lessons page.
    * Pass
    

#### User Story

As the **Site Owner / Admin** I can **Update products and lessons** so that **I can maintain my offerings**
  
#### Acceptance Criteria
  
* A Site Owner has access from the front end to maintain all available lessons - Add or Update
    * Pass


#### Edit a Lesson Form

![Edit a Lesson Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-edit-form.JPG)

#### Add a Lesson Form

![Add a Lesson Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/07.lessons-add-form.JPG)

### Feature: The Music Lesson Bag


* When a lesson is selected and submitted, the success message will display a smaller version of the music lesson bag with a summary.
    * Pass
* The Music Lesson Bag logo in the header, will now reflect the total cost of the lesson.
    * Pass
* When a site user clicks on the music lesson bag icon, the Music Lesson Bag page will open.
    * Pass
* The following information will be displayed:
   * Image
       * Pass
   * Lesson information including plan
       * Pass
   * Quantity 
       * Pass
   * Price
       * Pass
* A Remove button is available which will remove the lesson from the bag for the user.
    * Pass
* The bag total will display and the user can select secure checkout to move on to the checkout page.
    * Pass
* Three adverts exist at the bottom of the screen each with a link to the advertised page.
    * Pass
* The display for the mobile view does not include a table, it displays the items one after the other with the bag total and checkout button displayed on top. The back to top arrow is included on smaller screens.
    * Pass

#### User Story

As  a **User** I can **add a lesson to the music lesson bag** so that **I can view the lesson and proceed to checkout**
  
#### Acceptance Criteria
  
* The correct details of the lesson reflect in the music lesson bag
   * Pass
* A miniature version of the music lesson bag reflects in the success message
   * Pass
* The user can select to remove the lesson from the bag
   * Pass
* The user can proceed to checkout from inside the bag
   * Pass

#### Desktop Site
![Lesson Bag Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/08.music-lesson-bag-desktop.JPG)

#### Mobile Site
![Lessons Bag Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/08.music-lesson-bag-mobile.JPG)

### Feature: Music Lesson Checkout

* Only users with an account can proceed to subscribe to lessons as recurring payments are required.
   * Pass
* Site browsers will be referred to the login page.
   * Pass
* The summarised lesson details reflect correctly on the checkout page with the subtotal and order total reflecting correctly.
   * Pass
* The site user can capture their credit card number in the payment element - which is generated through integration with stripe.
   * Pass
* The site user can select the change subscription button which will take them back to their lesson bag to remove the lesson.
   * Pass
* The site user can select subscribe to proceed with the subscription creation.
   * Pass
* The customer, subscription and payment will be created on stripe and returned. If a customer already exists, the subscription will be added against the same customer account on stripe.
   * Pass
* The site user will proceed to the successfully subscribed page.
   * Pass
* The site user can complete their personal details and additional details and select finalise to finalise their subscription.
   * Pass
* The site user can choose to cancel the subscription, which will cancel the subscription on Stripe and delete it from the database. The site user will be returned to their profile page.
   * Pass
* If the site user finalises their subscription, they will be directed to the lesson complete page.
   * Pass
* An email confirming their subscription details will be sent to their email address provided.
   * Pass
* A subscription summary will be provided on the subscription complete page.
   * Pass
* A success message containing the details will be displayed.
   * Pass
* A link to the latest invoice for the subscription will be available.
   * Pass
* If the user opens the link, it will open on a new page and the user has access to view or download the stripe invoice.
   * Pass
* The music lesson bag will now be empty.
   * Pass

#### User Story

As a **Site User** I can **proceed to checkout, pay for the subscription and add subscription details** so that **I can subscribe to a lesson**
  
#### Acceptance Criteria
  
* The correct pricing appears on the checkout page and I can capture my payment details
   * Pass
* I can add my details and student name to the subscription
   * Pass
* A subscription summary is generated and displayed
   * Pass
* I can access the Invoice on Stripe from the subscription summary
   * Pass


#### Desktop Site
![Music Lesson Checkout Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-payment-desktop.JPG)
![Music Lesson Subscribe Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-subscribe-desktop.JPG)
![Music Lesson Complete Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-complete-desktop.JPG)
![Stripe Invoice](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-stripe-invoice.JPG)

#### Mobile Site
![Music Lesson Checkout Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-payment-mobile.JPG)
![Music Lesson Subscribe Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-subscribe-mobile.JPG)
![Music Lesson Complete Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/09.lesson-checkout-complete-mobile.JPG)


### Feature: Music Store


* The music store provides the site user with three different store views to choose from. The products will display according to these categories:
    * All Products
        * Pass
    * Music Tools
        * Pass
    * Instruments and Equipment
        * Pass
* When the site user clicks on the shop now link under the category the relevant product view will open.
    * Pass
* A back to top arrow is included at the end of the screen, whcih allows the user to quickly navigate back to the top of the screen.
    * Pass
* A link to Yamaha to check out their products is included.
    * Pass
* Two adverts display at the end of the music store page, one for music lessons and the other for student showcase.
    * Pass
* The advert buttons will take the site user to the relevant page with further information.
    * Pass

   
#### User Story

As  a **Site User** I can **view the music store menu** so that **I can purchase individual products**
  
#### Acceptance Criteria
  
* Category menu for music store
    * Pass
* Each category has a shop now button
    * Pass
* The links are clickable and the view opened displays the relevant products for the category selected
    * Pass
  

#### Desktop Site
![Music Store Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/10.music-store-desktop.JPG)

#### Mobile Site
![Music Store Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/10.music-store-mobile.JPG)

### Feature: Products page


* The products page will render differently depending on which category is selected:
    * All Products - returns all store products
        * Pass
    * Music Tools - returns music support tools such as a metronome and music sheets
        * Pass
    * Instruments and Equipment - returns keyboards and sound equipment
        * Pass
* The product category and product count reflect at the top right of the page.
    * Pass
* A menu is available to select to sort the product items by various different views:
     * Price - low to high and high to low
         * Pass
     * Rating - low to high and high to low
         * Pass
     * Name - A to Z and Z to A
         * Pass
     * Category A to Z and Z to A
         * Pass
* Selecting each view will sort the products accordingly
    * Pass
* A product image, title, price, category and rating displays per product item.
    * Pass
* If a user is a staff member they will have the edit and delete buttons available to them.
    * Pass
* If a user is not staff, these buttons will not display.
    * Pass
* If a user clicks on the product image, the product detail page will open in a new tab.
    * Pass
* A back to top arrow is included at the end of the screen, which allows the user to quickly navigate back to the top of the screen.
    * Pass
* A return button will take the site user back to the music store page.
    * Pass

  
#### User Story

As  a **Site User** I can **sort the music store products** so that **I can easily find what product I am searching for**
  
#### Acceptance Criteria
  
* I can sort the music store products according to various options
    * Pass
* I can sort the music store products within a specific category
    * Pass
* I can sort the music store products across categories
    * Pass

#### Desktop Site
![Products Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-desktop.JPG)

#### Mobile Site
![Products Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-mobile.JPG)

#### Edit a Product

* As a staff member I can select the edit button and the Edit a  Product page will open.
    * Pass
* As a site user, the Edit button will not reflect on the page.
    * Pass
* An Alert message will display to let me know which  product I am editing.
    * Pass
* The current product details will pull through to the form.
    * Pass
* An update product button allows me to update and submits the form. The model will be updated within the database.
    * Pass
* A success message is displayed when a product is successfully updated.
    * Pass
* A cancel button exits on the page and returns to the products page.
    * Pass

#### Add a Product

* As a staff member I can select the Manage Shop Products option under the Admin dropdown menu and the Add a Product page will open.
    * Pass
* As a site user, the option will not reflect on the menu.
    * Pass
* A new form will display.
    * Pass
* The form is set up to allow me to add product details. 
    * Pass
* An add product button allows me to submit the form. Fields are validated and the form will not submit if missing relevant fields. The model will be updated with the new product.
    * Pass
* A success message is displayed when a product is successfully updated.
    * Pass
* A cancel button exits on the page and returns to the products page.
    * Pass
* The new product reflects on the lessons page.
    * Pass
  

#### Delete a Product

* As a staff member I can select the Delete button from the products page and the product will be deleted from the model.
* A success message will display confirming deletion.
* A site user will not be able to view the Delete button.
  

#### User Story


As the **Site Owner / Admin** I can **Update products and lessons** so that **I can maintain my offerings**
  
#### Acceptance Criteria
  
* A Site Owner/Admin has access from the front end to maintain all products in the music shop - Add, Update or Archive
* Pass

#### Add a  Product Page

![Add a  Product Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-add-form.JPG)

#### Edit Product Page
![Edit Product Form](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/11.products-edit-form.JPG)

### Feature: Product Detail Page

* The product detail page displays a product image, title, price, category, rating and description per product item.
    * Pass
* A quantity selection tool is available to the site user to increase or decrease the amount of items they would like to select.
    * Pass
* It validates to ensure the value is not less than 1 and not greater than 99
* By selecting add to bag, the selected quantity of the product is added to the shopping bag.
    * Pass
* A success message displays which includes a mini version of the shopping bag. 
    * Pass
* The total amount now reflects under the shopping bag icon.
* A keep shopping button is available which will return the user to the products page.
    * Pass
    

#### User Stories

As  a **Site User** I can **view an individual product** so that **I can decide whether to make a purchase or not**
  
#### Acceptance Criteria
  
* View details on the product
   * Pass
* View price, specifications and delivery options
   * Pass
* View details and images to make an informed decision
   * Pass
   
As a **Site User** I can **select the correct quantity** so that **I can buy the correct number of products I require**
  

#### Acceptance Criteria
  
* When adding a product to the shopping bag I can select the quantity.
    * Pass
* The correct quantity appears in the bag and the sub-total and totals update correctly.
    * Pass
   

#### Desktop Site
![Product Detail Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/12.product-detail-desktop.JPG)

#### Mobile Site
![Product Detail Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/12.product-detail-mobile.JPG)

### Feature: The Shopping Bag


* When a product is selected and submitted, the success message will display a smaller version of the shopping bag with a summary.
    * Pass
* The Shopping Bag logo in the header, will now reflect the total cost of the bag.
    * Pass
* When a site user clicks on the shopping bag icon, the Shopping Bag page will open.
* The following information will be displayed:
   * Image
       * Pass
   * Product Info
       * Pass
   * Price
       * Pass
   * Quantity
       * Pass
   * Sub-Total
       * Pass
* A Remove button is available which will remove the product from the bag for the user.
    * Pass
* The user is able to increase or decrease the quantity of a product through the quantity selector.
    * Pass
* When the user clicks the update button the new quantity will be updated and confirmed through a success message.
    * Pass
* The user will be told how much they still need to spend to receive free delivery in red text (if they are not over the threshold as yet).
    * Pass
* The bag total, delivery and grand total will display and the user can select secure checkout to move on to the checkout page.
* A keep shopping button will return the user to the products page.
    * Pass
* Multiple product items can be added to the bag at the same time.
* Three adverts exist at the bottom of the screen each with a link to the advertised page.
    * Pass
* The display for the mobile view does not include a table, it displays the items one after the other with the bag total and checkout button displayed on top. The back to top arrow is included on smaller screens.
    * Pass

#### User Stories

As a **Site User** I can **view all items added to my shopping bag** so that **I can see what I am purchasing and the total cost**
  
#### Acceptance Criteria
  
* View a summarised view of all products added to the shopping bag.
    * Pass
* View amount and sub-total per product.
    * Pass
* View total amount for all products.
    * Pass

As  a **Site User** I can **adjust the number of items in my shopping bag** so that **I purchase the correct amount**
  
#### Acceptance Criteria
  
* I can increase or decrease the quantity of a product I wish to purchase.
    * Pass
  

#### Desktop Site
![Shopping Bag Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/13.shopping-bag-desktop.JPG)

#### Mobile Site
![Shopping Bag Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/13.shopping-bag-mobile.JPG)


### Feature: Checkout


* All users, including those without an account can process to checkout and purchase products.
    * Pass
* The summarised product details reflect correctly on the checkout page with the subtotal, order total, delivery and grand total reflecting correctly.
    * Pass
* The site user can complete their personal details and delivery details.
    * Pass
* If the site user has an account they can select to save these details to their profile.
    * Pass
* If they do not, they will be told that they can login or create an account in order to save their details.
    * Pass
* The site user can capture their credit card number in the payment element - which is generated through integration with stripe.
    * Pass
* The site user can select the adjust bag button which will take them back to their shopping bag.
    * Pass
* The site user can select checkout to proceed with the payment.
    * Pass
* The payment will be processed on stripe.
    * Pass
* The site user will proceed to the checkout success page.
    * Pass
* An email confirming their order details will be sent to their email address provided.
    * Pass
* An order summary will be provided on the page.
    * Pass
* A success message containing the details will be displayed.
    * Pass
* The shopping bag will now be empty.
    * Pass

#### User Stories

As a **Site User** I can **easily checkout and capture my payment information** so that **I experience an efficient service**
  
#### Acceptance Criteria
  
* If I have an account, I can save my payment details to my account
    * Pass
* If I don't have an account I can choose to capture my payment details when checking out
    * Pass
* Checkout process runs smoothly and optimally
    * Pass

As a **Site User** I can **rest assured that all personal and payment information that I capture is secure** so that **I know my data and account is secure**
  
#### Acceptance Criteria
  
* Payment through Stripe.com is enabled.
    * Pass
* No sensitive personal or payment data is visible to anyone but the site user.
   * Pass
* Security measures are in place to ensure the safety of payments.
    * Pass
    
As a **Site User** I can **view an order confirmation once I have checked out** so that **I can confirm all the details and the purchase is correct**
  
#### Acceptance Criteria
  
* Once a product/subscription has been purchased, I can view all details after checkout.
    * Pass
* A copy of the order details is saved to my profile and I can view this.
    * Pass
* A copy of the order  receipt is emailed to me.
    * Pass
* If any details are incorrect I can contact the site admin to assist.
    * Pass
  
As a **Site User** I can **purchase and cancel subscriptions and purchase products** so that **I can utilise all services and purchase goods from the same site**
  
#### Acceptance Criteria
  
* The same user can purchase subscriptions and choose to set up whether to pay annually, monthly or weekly as well.
    * Pass
* Select multiple products to purchase, have the total reflect all products and pay for the items upfront
    * Pass
    

#### Desktop Site
![Checkout Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-desktop.JPG)
![Checkout Success Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-success-desktop.JPG)

#### Mobile Site
![Checkout Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-success-mobile.JPG)
![Checkout Success Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/14.music-store-checkout-success-mobile.JPG)


### Feature: Contact Us

* A Site User is able to capture a message via the contact us page and submit the request.
    * Pass
* A Site User can submit a request whether they have an account or not.
    * Pass
* If they have an account their full name and email address will be generated from their user record. Their username will reflect against their contact request.
    * Pass
* The contact request is saved and admin can access it from the Admin site.
    * Pass
* An email is sent to the admin email address containing the name, email address and contact message of the user.
    * Pass
   

#### User Story

As a **Site User** I can **create and submit a contact request** so that **I can receive support from the site admin or owner**
  
#### Acceptance Criteria
  
* A User is able to capture a message.
    * Pass
* The contact request is saved and admin can access it from the Admin site.
    * Pass
* An email is sent to the admin email address containing the name, email address and contact message of the user.
    * Pass

#### Desktop Site
![Contact Us Desktop](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/15.contact-us-desktop.JPG)

#### Mobile Site
![Contact Us Mobile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/15.contact-us-mobile.JPG)


### Feature: Marketing and Advertising


* Across the site various internal advertisements are placed to market lessons and products.
    * Pass
* All adverts contain links to the relevant pages where a user can view lessons and products.
    * Pass
* The language is enticing.
    * Pass
* The Student Showcase advert leads the user to view the student showcase section which demonstrates the results of lessons.
    * Pass
* When a new student showcase is added, an email is sent to those who have opted in for emails, this includes links to lessons and products.
    * Pass
* An advert banner at the top of the page provides details on lessons, the free music lesson if a user subscribes annually and the free delivery threshold.
    * Pass

   
#### User Story

As  a **Site User** I can **easily view any subscriptions special offers, and delivery deals** so that **I can take advantage of the offer**
  
#### Acceptance Criteria
  
* View any specials on subscriptions.
   * Pass
* View any delivery discounts.
    * Pass
* Receive all specials/deals via an email.
    * Pass

#### Desktop Site
![Adverts](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-desktop.JPG)
![Banner](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-desktop-banner.JPG)

#### Mobile Site
![Adverts](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-mobile.JPG)
![Banner](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/16.adverts-mobile-banner.JPG)

### User Story: Messages

As  a **Site User** I can **view success, info, error and alert messages** so that **I am alerted of the impact of my actions**
  
# Acceptance Criteria
  
* When a user adds items to the shopping bag, a success message displays and previews the items in the bag
    * Pass
* When a user logs in logs out success messages displays
    * Pass
* If any errors or alerts occur, success messages display
    * Pass

#### Desktop Site
 
![Messages](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/17.messages-desktop.JPG)


#### Mobile Site
![Messages](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/17.messages-mobile.JPG)


## Feature: Account Management


#### Register for an account

* A customised registration form has been created for new users to register for an account.
    * Pass
* The new site user will need to provide an email address, username, first name, last name and password.
    * Pass
* An optional checkbox for marketing opt in selection is provided for new users to opt in to receive emails. An option to opt out of emails from their user profile will be a future enhancement.
    * Pass
* Once the user has selected to sign up, a verification email will be sent to the provided email address.
    * Pass

##### User Story

As  a **Site User** I can **create/register for an account** so that **I can create a user profile and save my personal information**
  
##### Acceptance Criteria
  
* I can create a simple account.
    * Pass
* I can save my personal information.
    * Pass
* I can view sections that require me to be logged in.
    * Pass
* I can perform site actions that require me to be logged in.
    * Pass

##### Desktop Site
![Register](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/18.register-desktop.JPG)


##### Mobile Site
![Register](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/18.register-mobile.JPG)

#### Verification Email

* Once I have successfully registered an email confirmation is sent.
    * Pass
* The email confirmation is received in the email inbox I have registered with.
    * Pass
* A link in the confirmation email takes me to confirm my email and login to my account.
    * Pass
* I can successfully login to my account.
    * Pass

##### User Story

As a **Site User** I can **receive an email confirmation upon registration** so that **my registration is confirmed**
  
##### Acceptance Criteria
  
* Once I have successfully registered an email confirmation is sent.
    * Pass
* The email confirmation is received in the inbox I have registered with.
    * Pass
* A link in the confirmation email takes me to login to my account.
    * Pass

##### Desktop Site
![Verify](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.verify-desktop.JPG)
![Confirm](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.confirm-desktop.JPG)

##### Mobile Site
![Verify](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.verify-mobile.JPG)
![Confirm](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/19.confirm-mobile.JPG)

#### Login and Logout


* A non-logged-in will have the option to register or log in from their navigation.
    * Pass
* A site user can easily log in to their account by accessing the navigation menu and selecting login. 
    * Pass
* A site user will have the option to login with their Facebook or Google account.
    * Pass
* A site user can add their username and password and submit to login to their account.
    * Pass
* A success message will display when logged in.
    * Pass
* When logged in the user can update their personal user profile and view/action restricted pages/content for logged-in users only.
    * Pass
* Once logged in they will have the option to logout from their navigation.
    * Pass
* When a site user selects to logout the site will log them out and confirm with a success message.
    * Pass

##### User Story

As a **Site User** I can **easily login or logout of my account** so that **I can update my personal profile and access user sections**
  
##### Acceptance Criteria
  
* A non-logged-in will have the option to register or log in from their navigation.
    * Pass
* A user can easily log in to their account, once logged in they will have the option to logout from their navigation.
    * Pass
* When logged in the user can update their personal user profile and view/action restricted pages/content for logged-in users only.
    * Pass


##### Desktop Site
![Login](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.login-desktop.JPG)
![Logout](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.logout-desktop.JPG)

##### Mobile Site
![Login](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.login-mobile.JPG)
![Logout](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/20.logout-mobile.JPG)

#### Password Recovery


* From the login screen I can access the Forgot Password button.
    * Pass
* I can enter my email address on the password reset page and submit.
    * Pass
* A reset password email with a link will be sent to my email address.
    * Pass
* I can open the link and reset my password and proceed to login to my account.
    * Pass

###### User Story

As a **Site User** I can **recover my password** so that **I can continue to access my account**
  
###### Acceptance Criteria
  
* If I have forgotten my password I can request to reset it.
    * Pass
* A reset password email with a link will be sent.
    * Pass
* I can open the link and reset my password and proceed to login to my account.
    * Pass

##### Desktop Site
![Password Reset](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/21-password-reset-desktop.JPG)

##### Mobile Site
![Password Reset](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/21.password-reset-mobile.JPG)


### Feature: User Profile


* I can save my delivery details to my user profile when I place an order.
    * Pass
* The details will be returned to the order form when I create a future order.
    * Pass
* I can view past orders and open the order information details from my profile.
    * Pass
* I can view all active subscriptions and open the subscription information from my profile.
    * Pass
* I can select to cancel a subscription from my profile, it will cancel and I will be returned to my profile page.
    * Pass


#### User Stories

As a **Site User** I can **personalise my user profile** so that **I can save shipping information, and view my orders and subscriptions**
  
#### Acceptance Criteria
  
* I can save my shipping details to my account.
    * Pass
* I can view past orders and active subscriptions.
    * Pass
    
As a **Site User** I can **create multiple subscriptions and add student details** so that **I can manage all family subscriptions from one account**
  

#### Acceptance Criteria
  
* When a user sets up their subscriptions they can add student details
    * Pass
* I am able to see the student assigned to the subscription from my profile
    * Pass


#### Desktop Site
![User Profile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/22.user-profile-desktop.JPG)

#### Mobile Site
![User Profile](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/22.user-profile-mobile.JPG)

### Feature: Admin Access


* All staff roles can access the front end site pages.
    * Pass
* Site Owner has specific access assigned which restricts what they have access to view, edit, create and delete within the site admin section.
    * Pass
* Site Administrator has specific access assigned which restricts what they have access to view, edit, create and delete within the site admin section.
    * Pass
* Super User has full access apart from restrictions in code and only applicable djstripe models reflected in site admin.
    * Pass

#### User Story

As a **Site Owner / Site Admin / Super User** I can **access the Admin facility as well as maintain items on the front end** so that **I can actively support customers and manage my business**
  
# Acceptance Criteria
  
* Site Owner has specific access assigned.
    * Pass
* Site Admin has specific access assigned.
    * Pass
* Super User has full access apart from restrictions in code and only applicable djstripe models reflected in site admin.
    * Pass

#### Groups
![Super User](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/23.super-user-group.JPG)
![Store Owner](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/23.site-owner-group.JPG)
![Site Administrator](https://github.com/Claire-Potter/Belle-Musique-Studio/blob/main/project-files/features/23.site-admin-group.JPG)