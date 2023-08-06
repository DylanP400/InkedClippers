# Inked Clippers Barbershop & Tattoo Studio

Welcome to Inked Clippers!

Inked Clippers is your one-stop destination for all things barbershop and tattoo studio. Our platform brings together skilled barbers, talented tattoo artists, and expert piercers to showcase their services and connect with potential clients. Whether you're looking for a fresh haircut, a unique tattoo, or a stylish body piercing, Inked Clippers has got you covered.

[View live version](https://inked-clippers-6a7245ad63c3.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/DylanP400/InkedClippers)
![GitHub contributors](https://img.shields.io/github/contributors/DylanP400/InkedClippers)
![GitHub language count](https://img.shields.io/github/languages/count/DylanP400/InkedClippers)
![GitHub top language](https://img.shields.io/github/languages/top/DylanP400/InkedClippers)
![Code size](https://img.shields.io/github/languages/code-size/DylanP400/InkedClippers)
![Github files](https://img.shields.io/github/directory-file-count/DylanP400/InkedClippers)
![Github stars](https://img.shields.io/github/stars/DylanP400/InkedClippers)
![Github forks](https://img.shields.io/github/forks/DylanP400/InkedClippers)

## Contents

* [User Experience](#user-experience)

  * [Initial Discussion](#initial-discussion)

  * [User Stories](#user-stories)

* [Features](#features)

* [Technologies Used](#technologies-usedS)

* [Deployment](#deployment)




# User Experience

## Initial Discussion
Inked Clippers Barbershop & Tattoo Studio is the culmination of my passion for both barbershop aesthetics and tattoo artistry. Originally conceived as a barbershop, I quickly realized that I could expand the concept to include a tattoo parlor, making the project even more exciting and unique.

As a Django beginner, I embarked on this project with enthusiasm and determination. At first, I faced challenges connecting the various components, but through persistent trial and error, I gained a deeper understanding of the Django framework. Witnessing my vision gradually take shape was incredibly rewarding.

The primary goal for Inked Clippers was to create a captivating home page that features a stunning landing page image, a section dedicated to customer testimonials, and a clear representation of our studio's location. Additionally, I aimed to provide detailed and separate pages for both the barbershop and tattoo services, showcasing the full range of services and introducing the talented employees behind each craft.

Throughout the development process, I leveraged the power of Django, Bootstrap 5, and other essential technologies to ensure a seamless user experience. Combining frontend aesthetics with backend functionality, I strived to create an elegant and user-friendly platform that truly embodies the essence of our studio.

As a testament to my growth as a developer, Inked Clippers serves as my inaugural Django project, and it holds a special place in my heart. With this project, I not only honed my technical skills but also gained invaluable insights into the world of barbershops and tattoo studios. I'm proud to present Inked Clippers Barbershop & Tattoo Studio as a fusion of artistry, creativity, and technical prowess.

## Key information for this site

* **Navbar**: Easily navigate through the website and access different sections.

* **Footer**: Find contact details, address, and opening times for the shop.

* **Home Page**: Welcome with a captivating landing image, customer testimonials, and the shop's location.

* **About Page**: Introduction and a brief history of the barbershop and tattoo studio.

* **Barbers Page**: Explore a variety of barber services and meet the talented team of barbers.

* **Tattoo Page**: Explore piercing services, and get answers to common questions about getting a tattoo and aftercare from skilled artists and piercers on the Tattoo Page and FAQs section.

## User Stories

* As a **developer**, I want to **install Django on my local machine**, so that I can **start building web applications using the Django framework**

* As a **developer**, I want to **set up ElephantSQL in my workspace**, so that I can **use it as a cloud-based PostgreSQL database for my project**.

* As a **visitor**, I want to **read reviews and testimonials from previous customers**, so that **I can see the quality of the services offered**.

* As a **visitor**, I want to **learn more about the team behind the barbershop or tattoo studio**, so that **I can feel a connection and establish trust**.

* As a **visitor**, I want to **see a visually appealing header on the landing page**, so that **I can quickly understand the purpose and branding of the website**.

* As a **customer**, I want to **find the contact details of Inked Clippers, such as the address, phone number, and email**, so that **I can reach out to them for inquiries or appointments**.

* As a **customer**, I want to **easily find the location or address of the barbershop or tattoo studio**, so that **I can plan my visit or contact them if needed**.

* As a **visitor**, I want to **be greeted by an engaging hero image on the landing page**, so that **I can get a glimpse of the atmosphere and style of the barbershop or tattoo studio**.

* As a **customer**, I want to **view the list of services offered by the barbershop, along with their corresponding prices**, so that **I can choose the desired service within my budget**.

* As a **developer** I want to **perform an initial deployment of my Django project to Heroku**, so that **I can quickly test and verify its functionality in a live environment**.

* As a **customer**, I want to **register for the website** so that **I can access the features and functionalities**.

* As a **customer** I want to be **able to log in and log out of the website**, so that **I can have an account to save my information so I dont have to enter it every time**.

* As a **user**, I want to be **able to leave reviews for Inked Clippers services I have received** so that **I can share my experience and provide feedback to the barbershop and other potential customers**.

* As a **user**, I want to be **able to update my personal information on my profile page** so that **I can keep my details accurate and up to date**.

* As a **customer**, I want to **view the list of tattoo services offered by the studio, along with their corresponding prices**, so that **I can choose the desired service within my budget**.

* As a **customer**, I want to **browse a gallery of the barbershop's previous haircuts and styles**, so that **I can assess their expertise and find inspiration for my own haircut**.

* As a **customer**, I want to **browse a gallery of the tattoo studio's previous artworks**, so that **I can assess their style and find inspiration for my own tattoo design**.

# Features

## Exisiting Features

* Navigation Bar
  * The navigation bar is at the top of every page and has the logo with links to the About page, Barbers page, Tattoo page, Register and Log in pages.

    * Once the user is logged in the link to the About page disappears and the Register link changes to your profile while Login changes to Log out.

    * ![Nav Bar Desktop View]()

    * ![Nav Bar Mobile View]()

* Footer

  * The footer is at the bottom of every page and has the address, opening times and the contact details of Inked Clippers. Underneath the barbershop information it has social media links to find the barbers on Facebook, Twitter(X), Github and Linkedin.

* Home Page
  * The Landing page Image

    * When the website first loads you see an image of a man getting hes hair cut with writing that says "Precision Cuts, Timeless Tattoos
    Unleash Your Style at Inked Clippers!" underneath the callout there is a white button blinking if you click this button it will scroll down and take you to the testimonials section.

    * ![Landing Page Desktop View]()

    * ![Landing Page Mobile View]()

  * Testimonials
    * Testimonials is a section where people that have signed up for Inked Clippers can leave a review and tell there experience with the store and staff. If you are logged in there is a button that allows you to add your own review to the site.

    * The testimonials are made up of a star rating system, staff member, review and username.

    * ![Testimonails Desktop View]()

    * ![Testimonails Mobile View]()

  * Location
    * After you scroll past the testimonial section you have the location of the shop at the bottom of the page just above the footer.

    * ![Location Desktop View]()

    * ![Location Mobile View]()

* About Page
  * The about page is broken into three sections. The first section is a introducion to Inked Clippers with three images one of a barber pole, the second is of the town of Ennis and the third is a barber chair.

    * ![About Page section One Desktop View]()

    * ![About Page section One Mobile View]()

  * The second section has the history of Inked Clippers and how it transformed from Clippers to Inked Clippers. It has two photos of the store.

    * ![About Page section Two Desktop View]()

    * ![About Page section Two Mobile View]()

  * The third section is all about feeling welcome it explains the vibe and atmosphere of Inked Clippers.

    * ![About Page section Three Desktop View]()

    * ![About Page section Three Mobile View]()

* Barbers Page

  * The Barbers Page is made up of two sections the services of the barbershop and meet the the barbers.

    * The services is displayed as a table and it has all the services the barbershop provides with the price and a discount price for members that have created a page.

    * ![Barbers Page Services Desktop View]()

    * ![Barbers Page Services Mobile View]()

    * Meet the barbers has the 4 barbers profile displayed in cards it has the barbers name, image, role/nickname and a bio with there information.

    * ![Barbers Page Employees Desktop View]()

    * ![Barbers Page Employees Mobile View]()

* Tattoo Page
  * The Tattoo Page is broken into 3 sections piercing services, Meet the artist and piecer, and a FAQ's for commonly asked questions.

    * The first section is a set of 4 tables all showing the piecer services for Ear Piercings, Facial Piercings, Oral Piercings and Body Piercings

    * ![Tattoo Page services Desktop View]()

    * ![Tattoo Page services Mobile View]()

    * The second section is a meet the Tattoo shop employees its the same layout as seen on the barber page with artists name, image, role/nickname and a bio with there information.

    * ![Tatto page  employees Desktop View]()

    * ![Tattoo Page employees Mobile View]()

    * The third section is a FAQ's for commonly asked questions for getting a tattoo and the aftercare.

    * ![Tatto page  FAQ's Desktop View]()

    * ![Tattoo Page FAQ's Mobile View]()

* Register Page
  * The register page has a form for making a account for Inked Clippers if you already have a account it has a link to the login page underneath the sign up button

    * ![Register Page Desktop View]()

    * ![Register Page Mobile View]()

* Login Page
  * The Login page has a form for loging into your account if you dont have a account it has a link to the register page underneath the Login button

    * ![Login Page Desktop View]()

    * ![Login Page Mobile View]()

* Profile Page

  * Once you Log in you have the option to visit your profile page. Your profile has a placeholder image your username, email phone number and location.

  * Underneath your profile information there is a form prepopulated with your information you have the option to update your details within this form.

    * ![Profile Page Desktop View]()

    * ![Profile Page Mobile View]()

* Logout Page
  * Once you click logout in the navbar you are taken to the logout page which confirms you have been logged out and gives you the option the login again.

    * ![Logout Page Desktop View]()

    * ![Logout Page Mobile View]()

* Add a testimonial page
  * If you are logged in and clicked the add testimonial button on the home page you are taken to the add_testimonial page which has a form for creating a testimonial.

    * ![Add Testimonial Desktop View]()

    * ![Add Testimonial Mobile View]()

* Testimonial detail Page
  * If you click on a testimonial it will bring you to the Testimonial detail page which will show you the testimonial.

    * ![Testimonial Detail Desktop View]()

    * ![Testimonial Detail Mobile View]()

  * If you are logged in and clicked on your own testimonial you have the option to edit or delete your review.

    * ![Testimonial Detail Edit/Delete Desktop View]()

    * ![Testimonial Detail Edit/Delete Mobile View]()

* usertestimonial_form

  * If you are logged in and click edit on your own testimonial on the testimonial detail page you are taken to the usertestimonial_form which is a page that has a prepopluated form for updating your testimonial.

    * ![userestimonial_form Desktop View]()

    * ![userestimonial_form Mobile View]()

* usertestimonail_confirm_delete

  * If you are logged in and click delete on your own testimonial on the testimonial detail page you are taken to the usertestimonail_confirm_delete which is a page that confirms that you want to delete your testimonial. If you change your mind there is also a button to take you back to the home page.

    * ![usertestimonial_confirm_delete Desktop View]()

    * ![usertestimonial_confirm_delete Mobile View]()



# Technologies Used

## languages used

* HTML
* CSS
* Python
* Markdown

## Frameworks, Libraries & Programs Used

* [Git](https://git-scm.com/) - For version Control.

* [Github](https://github.com/) - Used to save and store the files for the website.

* [Gitpod](https://www.gitpod.io/) - Was used to created my code.

* [Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.

* [AM I Resposnsive?](https://amiresponsive.co.uk/) - Used to show the Website image on a range of devices.

* [Shields](https://shields.io/) - For the shields at the top of the README.

* [Favicon](https://www.favicon-generator.org/) - Used to make a Favicon for the website.

* [Coolors](https://coolors.co/808080-ff0000-ffffff-f5f5f5-000000) - For my colour scheme.

* [Lamba Testing](https://www.lambdatest.com/?fp_ref=ngan15&gclid=Cj0KCQjwocShBhCOARIsAFVYq0i7XM8lENlC8yIrumBcCkS42VLHZfT6Fjc5waFzBGuNk6OCc7kIBFUaAou3EALw_wcB) - Was used for testing resposiveness across various devices.

* [Favicon Generator](https://www.favicon-generator.org/) - Was
 used to make the favicon.

* [HTML Validator](https://validator.w3.org/) - For HTML validation.

* [Python validator](https://pep8ci.herokuapp.com/) - For Python validation.

* [W3 Jigsaw](https://jigsaw.w3.org/css-validator/) - For CSS validation.

* [Bootstrap5](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - For the sites layout.

* [Django3](https://docs.djangoproject.com/en/4.2/) - 

* [Cloudinary](https://cloudinary.com/) - For hosting Inked Clippers images.

* [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) - For hosting static files.

* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Enhanced form rendering for Django.

* [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL adapter for Python.

* [Gunicorn](https://gunicorn.org/) - A Python HTTP server for running web applications.

* [sqlparse](https://pypi.org/project/sqlparse/) - A Python library for parsing and formatting SQL queries.


# Deployment

## Heroku

* Steps for deployment.
* Fork or clone this repository.
* Create a new Heroku app.
* Link the Heroku app to the repository.
* Click on **Deploy**.

## Local Deployment

### How to Fork

To fork the repository:

1. Log in to Github.
2. Go to the repository for this project, [DylanP400/InkedClippers](https://github.com/DylanP400/terminal-dice-pp3)
3. Click the Fork button in the top right corner.

### How to clone

To clone the repository:

1. Log in to GitHub.
2. Go to the repository for this project, [DylanP400/InkedClippers](https://github.com/DylanP400/InkedClippers)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
