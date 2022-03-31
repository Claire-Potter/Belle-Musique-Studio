# Django Apps and Models

All Apps and Models for Belle Musique Studio project.

The XperienceDezignWiz project is created utilising six separate Apps.

<!-- Start Document Outline -->

* [Home App](#home-app)
	* [1. The User Model](#1-the-user-model)
	* [2. The Contact Model](#2-the-contact-model)
	* [3. The Cover Model](#3-the-cover-model)
	* [4. The Student Showcase Model](#4-the-student-showcase-model)
	* [5. The User Subscription Model](#5-the-user-subscription-model)
	* [6. The Marketing Sign Up Model](#6-the-marketing-sign-up-model)
* [The Checkout App](#the-checkout-app)
	* [1. The Order Model](#1-the-order-model)
	* [2. The OrderLineItem Model](#2-the-orderlineitem-model)
	* [3. The Subscribed Customer Model](#3-the-subscribed-customer-model)
	* [4. The SubscriptionLineItem Model](#4-the-subscriptionlineitem-model)
* [Lessons App](#lessons-app)
* [Profiles App](#profiles-app)
	* [1. The UserProfile Model](#1-the-userprofile-model)
* [Shopping Bag App](#shopping-bag-app)
* [Store App](#store-app)
	* [1. The Category Model](#1-the-category-model)
	* [2. The Music Product Model](#2-the-music-product-model)
* [DJStripe Models](#djstripe-models)

<!-- End Document Outline -->

## Home App
The Home App is utilised to house:

### 1. The User Model
The User model replaces the allauth default User. It is
used to create User accounts to authenticate and access the site.
The customer field is used to store the associated Stripe customer once
they have been created and returned from Stripe.com.

| Key | Name       | Type                    | Explanation                                                                                                               |
|-----|------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.         
|  OnetoOne          | customer<br>     | OneToOneField(Customer, djstripe_id)                                                      | Conceptually, this is similar to a ForeignKey with unique=True, but the "reverse" side of the relation will directly return a single object.         |
|     | date_joined<br>     |DateTimeField               | A date, represented in Python by a datetime.date instance |
|     | email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                                 |
|     |  first_name       | CharField                                             | A field to store text based values.     
|            | is_active | BooleanField                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |
 |       | is_staff | BooleanField                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |
  |       | is_superuser | BooleanField                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |
  |     | last_login<br>     |DateTimeField               | A date, represented in Python by a datetime.date instance |
  |     |  last_name       | CharField                                             | A field to store text based values.   
    |     | password       | CharField                                             | A field to store text based values.  
        |     | username       | CharField                                             | A field to store text based values.  

### 2. The Contact Model
Utilised to store the contact request data and create the Contact us page view using the template contact.html. A foreignKey field is linked to store the username as the related_name 'contact'.

| Key        | Name       | Type                                                                | Explanation                                                                                                                       |
|------------|------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.         |
| ForeignKey | username   | ForeignKey(User, id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | body       | TextField                                                           | 	A large text field. The default form widget for this field is a Textarea.                                                        |
|            | created_on | DateTimeField                                                       | A date, represented in Python by a datetime.date instance                                                                         |
|            | email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                            |
|            | name       | CharField                                             | A field to store text based values.                                                                                               |


### 3. The Cover Model
Model created to render the cover input and save the cover name and quote to reflect.

| Key | Name         | Type                     | Explanation                                                                                                               |
|-----|--------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField             | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|     | name       | CharField                                             | A field to store text based values.                                                                         |
|     | page | CharField | A field to store text based values.                                                                                       |
|            | quote | CharField | A field to store text based values.      

### 4. The Student Showcase Model
Utilised to store the data added to create a student
showcase record.
Data is captured via the Add Student Showcase
front end page or in Site Admin.
Each record added should be linked back to the
associated Stripe customer and
subscription for record keeping purposes.

| Key        | Name       | Type                                                                | Explanation                                                                                                                       |
|------------|------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.         |
| ForeignKey | customer  | ForeignKey(Customer, djstripe_id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
| ForeignKey | subscription | ForeignKey(Subscription, djstripe_id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option. |
|            | body       | TextField                                                           | 	A large text field. The default form widget for this field is a Textarea.                                                        |
|            | date | DateTimeField                                                       | A date, represented in Python by a datetime.date instance                                                                         |
|            |excerpt     | TextField                                                           | 	A large text field. The default form widget for this field is a Textarea.                                                           |
|            |image_url     | URLField                                                          | 	A field to store the image url                         |
|            | name       | CharField                                            | A field to store text based values.                                                                                               |
|            | video_name | CharField                                             | A field to store text based values.                                                                                               |
|     | video_url    | EmbedVideoField          | A field to store the video url utilising the django library django-embed-video                                            |
### 5. The User Subscription Model
 The User Subscription model is utilised to link djstripe Subscriptions to a
 User record when the record is created in Stripe. A Foreign key field is
 used to link the model to the parent User model.

| Key        | Name       | Type                                                                | Explanation                                                                                                                       |
|------------|------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.         |
| ForeignKey | username   | ForeignKey(User, id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                               |
| ForeignKey | subscription   | ForeignKey(Subscription, djstripe_id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.
| |date         | DateTimeField                                                               | A date, represented in Python by a datetime.date instance                                                                                  |
|            |  subscription_name       | CharField                                            | A field to store text based values.                                                                                           |
|           |  subscription_user_id       | CharField                                            | A field to store text based values.                                                                                                                   |

### 6. The Marketing Sign Up Model
Utilised to store the data of users who have
signed up to receive a marketing letter from 
Belle Musique Studio.


| Key        | Name       | Type                                                                | Explanation                                                                                                                       |
|------------|------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>     | BigAutoField                                                        | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.         |
|            |  first_name       | CharField                                             | A field to store text based values.                                                          |
|    |  last_name       | CharField                                             | A field to store text based values.     
| |email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                                       |
|            | marketing_opt_in      | BooleanField                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                                                                             |
|            |  date         | DateTimeField                                                               | A date, represented in Python by a datetime.date instance                                                                                                                   |

## The Checkout App
The Checkout App is utilised to house the data for the Checkout processes and views for the relevant templates:

### 1. The Order Model
The Order model is where a user's order details are created and stored.
This includes the order_number, user details, shipping address
and order details.
It was created according to the Code Institute 'Boutique Ado' project.

| Key             | Name          | Type                                                                        | Explanation                                                                                                                                                                                               |
|-----------------|---------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 | id<br>        | BigAutoField                                                                | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                                                                 |
| ForeignKey      | user_profile | ForeignKey(UserProfile, id) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                          |
|      | country   | CountryField | A country field for Django models that provides all ISO 3166-1 countries as choices. CountryField is based on Django's CharField, providing choices corresponding to the official ISO 3166-1 list of countries .                                                                          |
|  | county   | CharField                                             | A field to store text based values.  |
| | date         | DateTimeField                                                               | A date, represented in Python by a datetime.date instance  |
|                 | delivery_cost        | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.                                                                                                                           |
|                 | email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                                                                                                         |
|                 | full_name  | CharField                                             | A field to store text based values.                                                                                                                                  |
|                 | grand_total      | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.                                                                                                 |
|                 | order_number  | CharField                                             | A field to store text based values.                                                                                                      |
|                 | order_total      | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.                                               |
|                 |original_bag     | TextField                                                           | 	A large text field. The default form widget for this field is a Textarea.                                                                                                                    
|            |  phone_number  | CharField                                             | A field to store text based values.                                             
||  postcode  | CharField                                             | A field to store text based values.                                             |
| |street_address1 | CharField                                             | A field to store text based values.                                             |
| |street_address2 | CharField                                             | A field to store text based values.                                             |
| |stripe_pid | CharField                                             | A field to store text based values.                                             |
| |town_or_city| CharField                                             | A field to store text based values.                                             |



### 2. The OrderLineItem Model
The OrderLineItem model includes the product item details of
 all products included in the order.
 It was created according to the Code Institute 'Boutique Ado' project.

| Key | Name         | Type                                                    | Explanation                                                                                                                      |
|-----|--------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField                                            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.        |
|ForeignKey | order        | ForeignKey(Order, id) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                    |
| ForeignKey | product       | ForeignKey(MusicProduct, id) | A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.      |
|     | line_item_total      | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.                                                            |
|     | product_size         | CharField                               | A field to store text based values.                                                                                              |
|     | quantity| IntegerField                                            | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.                     |

### 3. The Subscribed Customer Model

The SubscribedCustomer model is where a user's details
are saved as a customer record. This includes the customer details,
user details and contact details.
The djstripe customer id from the Customer model is copied and
saved as the subscribed_customer_id and the customer field
has a one to one relationship with the djstripe Customer model.

| Key | Name         | Type                     | Explanation                                                                                                               |
|-----|--------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     | id<br>       | BigAutoField             | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807. |
|  OnetoOne          | customer<br>     | OneToOneField(Customer, djstripe_id)                                                      | Conceptually, this is similar to a ForeignKey with unique=True, but the "reverse" side of the relation will directly return a single object.                                                                  |
|  OnetoOne          | user_profile<br>     | OneToOneField(UserProfile, id)                                                      | Conceptually, this is similar to a ForeignKey with unique=True, but the "reverse" side of the relation will directly return a single object.                 |
|     |  country   | CountryField | A country field for Django models that provides all ISO 3166-1 countries as choices. CountryField is based on Django's CharField, providing choices corresponding to the official ISO 3166-1 list of countries .                                                                                       |
|     |date         | DateTimeField                                                               | A date, represented in Python by a datetime.date instance  |
|                 | email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                                                                                                         |
|                 | full_name  | CharField                                             | A field to store text based values.                                                                                                                                  |
|                 | phone_number  | CharField                                             | A field to store text based values.                                                                                                   |
|                 | subscribed_customer_id | CharField                                             | A field to store text based values.                                                                                                      |

### 4. The SubscriptionLineItem Model
The SubscribedLineItem model is where a subscribed customer's
subscription details are saved as a subscription record. This
includes the subscription details and billing details.
The djstripe subscription id from the Subscription model is copied and
saved as the subscribed_id and the subscription field has a
Foreign Key relationship with the djstripe Subscription model.
The customer field has a Foreign Key relationship with the
SubscribedCustomer model, linking all subscriptions back to the customer.

| Key        | Name         | Type                                                                    | Explanation                                                                                                                                                |
|------------|--------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>       | BigAutoField                                                            | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                  |
| ForeignKey | customer   | ForeignKey(SubscribedCustomer, id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                          |
| ForeignKey | latest_invoice  | ForeignKey(Invoice, djstripe_id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                                        |
|ForeignKey | subscription   | ForeignKey(Subscription, djstripe_id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                                      |
|            | end_date       | CharField                                                | A field to store text based values.                                               |
|            | line_item_total      | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.  |
|             |original_lesson_bag     | TextField                                                           | 	A large text field. The default form widget for this field is a Textarea.                                                                                                                         |
|            |  price       | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.                                                                                               |
|     | quantity| IntegerField                                            | It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.                     |
|            | start_date       | CharField                                                | A field to store text based values.                                               |
|            | status       | CharField                                                | A field to store text based values.                                               |
|            | subscribed_id      | CharField                                                | A field to store text based values.                                               |
|            | subscription_name      | CharField                                                | A field to store text based values.                                               |


## Lessons App
The Lessons App is utilised to house the views for the lessons templates. It does not contain any models as the Product. Plan and Price models from DJStripe are utilised to store the data.

## Profiles App
The Profiles App is utilised to store the data for the User Profile and house the views for the profile templates. 

### 1. The UserProfile Model
The UserProfile  model allows the user to read,
edit and delete the various userprofile fields.
The model can be updated when an order is placed with
order address details
added by the user.

| Key        | Name         | Type                                                               | Explanation                                                                                                                                                |
|------------|--------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>       | BigAutoField                                                       | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                  |
| OnetoOne          | user<br>     | OneToOneField(User, id)                                                      | Conceptually, this is similar to a ForeignKey with unique=True, but the "reverse" side of the relation will directly return a single object.                            |
|                 | default_additional_email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                                                                                                         |
|      | default_country   | CountryField | A country field for Django models that provides all ISO 3166-1 countries as choices. CountryField is based on Django's CharField, providing choices corresponding to the official ISO 3166-1 list of countries .                                                                          |
|  | default_county   | CharField                                             | A field to store text based values.  |
|                 | default_email      | EmailField                                                          | It is a CharField that checks that the value is a valid email address.                                                                                                                                         |
|                 | default_full_name  | CharField                                             | A field to store text based values.                                                                                                                                  |
|            |  default_phone_number  | CharField                                             | A field to store text based values.                                             
||  default_postcode  | CharField                                             | A field to store text based values.                                             |
| |default_street_address1 | CharField                                             | A field to store text based values.                                             |
| |default_street_address2 | CharField                                             | A field to store text based values.                                             |
| |default_town_or_city| CharField                                             | A field to store text based values.                                             |

## Shopping Bag App
The Shopping Bag App is utilised to house the views for the shopping bag templates. It does not contain any models  from the Store App and DJStripe are utilised to store the data.

## Store App
The Store App is utilised to store the data for the music store and  house the views for the music store templates.

### 1. The Category Model
 Category model used to store all categories
  for music products

| Key        | Name         | Type                                                               | Explanation                                                                                                                                                |
|------------|--------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>       | BigAutoField                                                       | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                  |
|  | call_name   | CharField                                             | A field to store text based values.  |
|                 | name  | CharField                                             | A field to store text based values.                                                                                                                                  |


### 2. The Music Product Model
 Model used to store all music product
 items for the music store

| Key        | Name         | Type                                                               | Explanation                                                                                                                                                |
|------------|--------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            | id<br>       | BigAutoField                                                       | It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.                                  |
|ForeignKey | category   | ForeignKey(Category, id) |  A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.                                                                                      |
|            | description       | TextField                                                           | 	A large text field. The default form widget for this field is a Textarea.                                                        |   
|       | has_sizes | BooleanField                  | A true/false field. <br>The default form widget for this field is a CheckboxInput.                                               |
|            |image    | ImageField                                                          | 	A field to store the image                      |
|            |image_alt     | CharField                                             | A field to store text based values.                     |
|            |image_url     | URLField                                                          | 	A field to store the image url                                              |
|            |name    | CharField                                             | A field to store text based values.                     |
|                 | price      | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.                                                                                                                           |
|                 | rating        | DecimalField                                                              | DecimalField is a field which stores a fixed-precision decimal number, represented in Python by a Decimal instance. It validates the input using DecimalValidator.                                                                                                                           |
|            |sku   | CharField                                             | A field to store text based values.                     |


## DJStripe Models
The database is synced with the djstripe database to include the relevant djstripe models. The models are Stripe models in whihc the data has been created either on the Stripe dashboard or through the stripe API. Please see the database model diagramme for DJSTripe for a view of the the models used through the API.









