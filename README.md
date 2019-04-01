## KC Real Estate

This app uses Django's Framework with Python;built on Windows via Bash Shell and Vitual Enviroment; a PostgreSQL database is used; and basic HTML, Bootstrap, JQuery, and Lightbox were utilized for styling/functionality. 

## Description 

This is a simple business site that allows you to add real estate listings and associated property information to a Listings page and manage realtors and client inquiries. There is the ability for any user to register and make a profile; any site user can make inquiries about a specific property that with automatically populate with your email address and name if you are a registered user. There is a user dashboard for registered users that displays previous inquiries made, and a notification that appears if you have already made an inquiry to a specific property. 

## Admin MVC

Django Admin Model View Controller (MVC) allows you to set up a superuser and users with administrative purposes to add info and resources to you app. With KCRE the admin can add new listings and associated information in addition to managing realtors, users, and inquiries. A realtor of the month can also be designated to display on the About page of the App. This MVC is configured with a sub-App called Users to keep a record of clients who have registered and their inquiries. A sub-App for non-registered user inquiries is called Contacts. Anytime an inquiry is made the superuser is notified via email. 

Admin customization is complete with company colors and logo. 

## Full Search Functionality

The Search form on the Home Page allows you to search current listings by Keyword, City, State, Number of Bedrooms and Price. 


## Deployed to Heroku-Check it out! 

Live app is available at: https://kc-real-estate.herokuapp.com/

The admin login is available at: https://kc-real-estate.herokuapp.com/admin/   UN: admintest PW: test123
