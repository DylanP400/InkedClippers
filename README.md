# Inked Clippers Barbershop & Tattoo Studio

![Am I responsive image](./static/images/readme/am_i_responsive.png)

Welcome to Inked Clippers!

Inked Clippers is your one-stop destination for all things barbershop and tattoo studio. Our platform brings together skilled barbers, talented tattoo artists, and expert piercers to showcase their services and connect with potential clients. Whether you're looking for a fresh haircut, a unique tattoo, or a stylish body piercing, Inked Clippers has got you covered.

[View live website](https://inked-clippers-6a7245ad63c3.herokuapp.com/)


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

  * [Agile Methodology](#agile-methodology-moscow-and-kanban-board)

  * [User Stories](#user-stories)

* [Features](#features)

* [Testing](#testing)

* [Technologies Used](#technologies-used)

* [Deployment](#deployment)

  * [ElephantSQL](#elephantsql-database-setup)
  * [Heroku](#heroku)
  * [Local Deployment](#local-deployment)


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


## Agile Methodology, MOSCOW, and Kanban Board

### My Agile Approach

This project was developed using **Agile methodologies** to facilitate flexibility and iterative progress. Embracing an adaptive planning process allowed me to continuously improve and respond to evolving project needs.

### User Stories and MOSCOW Prioritization

To outline project features, I defined user stories short descriptions from an end user's perspective. Employing the MOSCOW technique helped me prioritize these features effectively:

* **Must-Have:** Identified critical features essential for project success.
* **Should-Have:** Important features that were not immediately critical.
* **Could-Have:** Considered features that could be included if time allowed.
* **Wont-Have:** Acknowledged nice-to-haves that were intentionally excluded from the current scope.

MOSCOW prioritization guided me in managing expectations, focusing on key deliverables, and navigating the development process.

### Kanban Board for Task Management

I utilized a Kanban board to visually manage the flow of work throughout the project. The board's columns included:

* **To Do:** Tasks (user stories) planned for development.
* **In Progress:** Tasks actively being worked on.
* **Done** Tasks that have been finished.
* **Future Features:** Tasks that will be added in the future.
* **Wont Have** Tasks that wont be included in the project.

This Kanban board provided a clear visual representation of my project's progress, making it easier to track and manage tasks.
[Link to project Kanban board.](https://github.com/users/DylanP400/projects/7/views/1)


[Back to top](#inked-clippers-barbershop--tattoo-studio)

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

## Existing Features

* Nav

  * The nav bar is at the top of every page and has the logo with links to the About page, Barbers page, Tattoo page, Register and Log in pages.

    * Once the user is logged in the link to the About page is hidden and the Register link changes to profile while Login changes to Log out.

    <details>
      <summary>Desktop view</summary>

      * ![Nav Bar Desktop View](./static/images/readme/website/navbar-desktop.png)

    </details>

    <details>
        <summary>Mobile view</summary>

      * ![Nav Bar Mobile View](./static/images/readme/website/navbar-mobile.png)

      </details>

* The Footer
  * The footer is at the bottom of every page and has the address, opening times and the contact details of Inked Clippers. Underneath the barbershop information it has social media links to find the barbers on Facebook, Twitter(X), Github and Linkedin.

    <details>
    <summary>Desktop view</summary>

      * ![Footer Desktop View](./static/images/readme/website/footer-desktop.png)

    </details>

    <details>
    <summary>Mobile view</summary>

      * ![Footer Page Mobile View](./static/images/readme/website/footer-mobile.png)

    </details>

* Home Page
  * The Landing page Image

    * When the website first loads you see an image of a man getting hes hair cut with writing that says "Precision Cuts, Timeless Tattoos
    Unleash Your Style at Inked Clippers!" underneath the callout there is a white button blinking if you click this button it will scroll down and take you to the testimonials section.

      <details>
      <summary>Desktop view</summary>

      * ![Landing Page Desktop View](./static/images/readme/website/home-page-desktop.png)

      </details>

      <details>
      <summary>Mobile view</summary>

      * ![Landing Page Mobile View](./static/images/readme/website/home-page-mobile.png)

      </details>

  * Testimonials
    * Testimonials is a section where people that have signed up for Inked Clippers can leave a review and tell there experience with the store and staff. If you are logged in there is a button that allows you to add your own review to the site.

    * The testimonials are made up of a star rating system, staff member, review and username.

      <details>
      <summary>Desktop view</summary>

        * ![Testimonails Desktop View](./static/images/readme/website/testimonials-1-desktop.png)

        * ![Testimonails Desktop View](./static/images/readme/website/testimonials-2-desktop.png)
      
      </details>

      <details>
      <summary>Mobile view</summary>

        * ![Testimonails Mobile View](./static/images/readme/website/testimonials-mobile.png)

  * Location

    * After you scroll past the testimonial section you have the location of the shop at the bottom of the page just above the footer.

      <details>
      <summary>Desktop view</summary>

        * ![Location Desktop View](./static/images/readme/website/location-desktop.png)

      </details>

      <details>
      <summary>Desktop view</summary>

        * ![Location Mobile View](./static/images/readme/website/location-mobile.png)

      </details>

* About Page

  * The about page is broken into four sections. The first section is a introducion to Inked Clippers with an image of a standard barbershop pole

    <details>
    <summary>Desktop view</summary>

      * ![About Page section One Desktop View](./static/images/readme/website/about-page-1-desktop.png)

    </details>

    <details>
    <summary>Mobile view</summary>

      * ![About Page section One Mobile View](./static/images/readme/website/about-page-1-mobile.png)

    </details>

  * the second section is a continuation of the first section the introduction and it has an image of three barber chairs.

    <details>
    <summary>Desktop view</summary>

      * ![About Page section Two Desktop View](./static/images/readme/website/about-page-2-desktop.png)

    </details>

    <details>
    <summary>Mobile view</summary>

      * ![About Page section Two Mobile View](./static/images/readme/website/about-page-2-mobile.png)

    </details>

  * The third section has the history of Inked Clippers and how it transformed from Clippers to Inked Clippers. It has two photos of the store.

    <details>
    <summary>Desktop view</summary>

      * ![About Page section Three Desktop View](./static/images/readme/website/about-page-3-desktop.png)

    </details>

    <details>
    <summary>Mobile view</summary>

      * ![About Page section Three Mobile View](./static/images/readme/website/about-page-3-mobile.png)

    </details>

  * The fourth section is all about feeling welcome it explains the vibe and atmosphere of Inked Clippers.

    <details>
    <summary>Desktop view</summary>

      * ![About Page section Four Desktop View](./static/images/readme/website/about-page-4-desktop.png)

    </details>

    <details>
    <summary>Mobile view</summary>

      * ![About Page section Four Mobile View](./static/images/readme/website/about-page-4-mobile.png)

    </details>

* Barbers Page

  * The Barbers Page is made up of two sections the services of the barbershop and meet the the barbers.

    * The services is displayed as a table and it has all the services the barbershop provides with the price and a discount price for members that have created a page.

      <details>
      <summary>Desktop view</summary>

      * ![Barbers Page Services Desktop View](./static/images/readme/website/barbers-page-1-desktop.png)

      </details>

      <details>
      <summary>Mobile view</summary>

      * ![Barbers Page Services Mobile View](./static/images/readme/website/barbers-page-1-mobile.png)

      </details>

    * Meet the barbers has the 4 barbers profile displayed in cards it has the barbers name, image, role/nickname and a bio with there information.

      <details>
      <summary>Desktop view</summary>

      * ![Barbers Page Employees Desktop View](./static/images/readme/website/barbers-page-2-desktop.png)

      </details>

      <details>
      <summary>Mobile view</summary>

      * ![Barbers Page Employees Mobile View](./static/images/readme/website/barbers-page-2-mobile.png)

      </details>


* Tattoo Page

  * The Tattoo Page is broken into 3 sections piercing services, Meet the artist and piecer, and a FAQ's for commonly asked questions.

    * The first section is a set of 4 tables all showing the piecer services for Ear Piercings, Facial Piercings, Oral Piercings and Body Piercings

      <details>
      <summary>Desktop view</summary>

      * ![Tattoo Page Services Desktop View](./static/images/readme/website/tattoo-page-1-desktop.png)

      </details>

      <details>
      <summary>Mobile view</summary>

      * ![Tattoo Page Services Mobile View](./static/images/readme/website/tattoo-page-1-mobile.png)

      </details>

    * The second section is a meet the Tattoo shop employees its the same layout as seen on the barber page with artists name, image, role/nickname and a bio with there information.

      <details>
      <summary>Desktop view</summary>

      * ![Tattoo Page Employees Desktop View](./static/images/readme/website/tattoo-page-2-desktop.png)

      </details>

      <details>
      <summary>Mobile view</summary>

      * ![Tattoo Page Services Mobile View](./static/images/readme/website/tattoo-page-2-mobile.png)

      </details>

    * The third section is a FAQ's for commonly asked questions for getting a tattoo and the aftercare.

      <details>
      <summary>Desktop view</summary>

      * ![Tattoo Page FAQ's Desktop View](./static/images/readme/website/tattoo-page-3-desktop.png)

      * ![Tattoo Page FAQ's Desktop View](./static/images/readme/website/tattoo-page-4-desktop.png)

      </details>

      <details>
      <summary>Mobile view</summary>

      * ![Tattoo Page FAQ'S Mobile View](./static/images/readme/website/tattoo-page-3-mobile.png)
      * ![Tattoo Page FAQ'S Mobile View](./static/images/readme/website/tattoo-page-4-mobile.png)

      </details>

* Register Page

  * The register page has a form for making a account for Inked Clippers if you already have a account it has a link to the login page underneath the sign up button

    <details>
    <summary>Desktop view</summary>

    * ![Register Page Desktop View](./static/images/readme/website/register-page-1-desktop.png)
    * ![Register Page Desktop View](./static/images/readme/website/register-page-2-desktop.png)

    </details>

    <details>
    <summary>Mobile view</summary>

    * ![Register Page Mobile View](./static/images/readme/website/register-page-1-mobile.png)
    * ![Register Page Mobile View](./static/images/readme/website/register-page-2-mobile.png)

    </details>

* Login Page

  * The Login page has a form for loging into your account if you dont have a account it has a link to the register page underneath the Login button

    <details>
      <summary>Desktop view</summary>

      * ![Login Page Desktop View](./static/images/readme/website/login-page-desktop.png)

    </details>

    <details>
      <summary>Mobile view</summary>

      * ![Login Page Mobile View](./static/images/readme/website/login-page-mobile.png)

    </details>

* Profile Page

  * Once you Log in you have the option to visit your profile page. Your profile has a placeholder image your username, email phone number and location.

  * Underneath your profile information there is a form prepopulated with your information you have the option to update your details within this form.

    <details>
      <summary>Desktop view</summary>

      * ![Profile Page Desktop View](./static/images/readme/website/profile-page-1-desktop.png)
      * ![Profile Page Desktop View](./static/images/readme/website/profile-page-2-desktop.png)

    </details>

    <details>
      <summary>Mobile view</summary>

      * ![Profile Page Mobile View](./static/images/readme/website/profile-page-1-mobile.png)
      * ![Profile Page Mobile View](./static/images/readme/website/profile-page-2-mobile.png)
      * ![Profile Page Mobile View](./static/images/readme/website/profile-page-3-mobile.png)

    </details>

* Logout Page
  * Once you click logout in the navbar you are taken to the logout page which confirms you have been logged out and gives you the option the login again.

    <details>
      <summary>Desktop view</summary>

      * ![Logout Page Desktop View](./static/images/readme/website/logout-desktop.png)

    </details>

    <details>
      <summary>Mobile view</summary>

      * ![Login Page Mobile View](./static/images/readme/website/logout-page-mobile.png)

    </details>

* Add a testimonial page

  * If you are in your profile and click the leave a review button you will be redirected to the add testimonial page which has a form for creating a testimonial.

    <details>
      <summary>Desktop view</summary>

      * ![Add Testimonial Desktop View](./static/images/readme/website/add-testimonial-desktop.png)

    </details>

    <details>
      <summary>Mobile view</summary>

      * ![Add Testimonial Mobile View](./static/images/readme/website/add-testimonial-mobile.png)

    </details>

* Testimonial detail Page

  * If you click on your own testimonial in your profile it will bring you to the Testimonial Detail page which will show you the testimonial.

    <details>
      <summary>Desktop view</summary>

      * ![Testimonial Detail Desktop View](./static/images/readme/website/testimonial-detail-desktop.png)

    </details>

    <details>
      <summary>Mobile view</summary>

      * ![Testimonial Detail Mobile View](./static/images/readme/website/testimonial-detail-mobile.png)

    </details>

* Edit Testimonial Page

  * If you are in your profile there will be two buttons underneath your testimonial clicking edit will bring you to a form with your testimonial information pre populated

    <details>
      <summary>Desktop view</summary>

      * ![Edit Testimonial Desktop View](./static/images/readme/website/edit-testimonial-desktop.png)

    </details>

    <details>
      <summary>Mobile view</summary>

      * ![Edit Testimonial Mobile View](./static/images/readme/website/edit-testimonial-mobile.png)

    </details>

* Delete Testimonial Page

  * If you are in your profile and click the delete button under your testimonial you will be brought too add page asking if you are sure you want to delete. If you change your mind there is also a button to take you back to the home page.

    <details>
      <summary>Desktop view</summary>

      * ![Delete Testimonial Desktop View](./static/images/readme/website/delete-testimonial-desktop.png)

    </details>

    <details>
      <summary>Desktop view</summary>

      * ![Delete Testimonial Desktop View](./static/images/readme/website/delete-testimonial-mobile.png)

    </details>

[Back to top](#inked-clippers-barbershop--tattoo-studio)

# Testing

I have made a seperate file for testing Inked Clippers all testing results can be found here [TESTING.md](TESTING.md).


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

* [Responsive Design Checker](https://responsivedesignchecker.com/) - For checking the responsiveness across mulitiple devices and screen widths

* [Shields](https://shields.io/) - For the shields at the top of the README.

* [Favicon](https://www.favicon-generator.org/) - Used to make a Favicon for the website.

* [Favicon Generator](https://www.favicon-generator.org/) - Was
 used to make the favicon.

* [HTML Validator](https://validator.w3.org/) - For HTML validation.

* [Python validator](https://pep8ci.herokuapp.com/) - For Python validation.

* [W3 Jigsaw](https://jigsaw.w3.org/css-validator/) - For CSS validation.

* [Bootstrap5](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - For the sites layout.

* [Django3](https://docs.djangoproject.com/en/4.2/) - 

* [Cloudinary](https://cloudinary.com/) - For hosting Inked Clippers images.

* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Enhanced form rendering for Django.

* [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL adapter for Python.

* [Gunicorn](https://gunicorn.org/) - A Python HTTP server for running web applications.

* [sqlparse](https://pypi.org/project/sqlparse/) - A Python library for parsing and formatting SQL queries.

# Deployment

## ElephantSQL Database Setup

### Step 1: Obtain ElephantSQL Database URL

1. **Sign up or sign in to ElephantSQL:**
   * If you don't have an account, sign up otherwise, log in to your account.

2. **Create a new ElephantSQL instance:**
   * From the dashboard, click on `Create New Instance`.
   * Choose a plan based on your requirements.

3. **Retrieve your ElephantSQL Database URL:**
   * Once the instance is created, click on it to view details.
   * Find and copy the `URL` provided this is your `ElephantSQL Database URL`.

### Step 2: Configure Django Project

1. **Add DATABASE_URL to env.py:**
   * Open your `env.py` file.
   * Set `DATABASE_URL` to the value obtained from ElephantSQL.

### Step 3: Use DATABASE_URL in Django Settings

1. **Update Django Settings:**
   * Open your `settings.py` file in your Django project.
   * Locate the `DATABASES` configuration.
   * Comment out the orignal django database settings
   * Update the `DATABASES` setting to use the `dj_database_url` package:

     ```python
     import dj_database_url
     # At the top of settings.py with the other imports

     DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
      }
      # Replace the orignal database with what is above

     ```

   * This allows your Django project to use the ElephantSQL Database URL.

2. **Migrate Database Changes:**
   * Run the following commands in your terminal:

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

   * This ensures that your database is updated with the latest changes.

## Heroku

## Step 1: Prepare Environment Variables

Create an `env.py` file at the root level of your project. Copy and paste the following content into the file:

```python
import os

# Replace placeholders with your actual values
os.environ['DATABASE_URL'] = 'Your_ElephantSQL_Database_url'
os.environ['SECRET_KEY'] = 'Your_Django_secret_key'
os.environ['CLOUDINARY_URL'] = 'Your_Cloudinary_url'
```

## Step 2: Heroku App Setup

1. **Sign up or sign in to your Heroku account:**
   * If you don't have an account, sign up otherwise, log in to your account.

2. **Create a new app from the Heroku dashboard:**
   * Choose a name for your app.
   * Select the region that is most suitable for you.

3. **Configure app settings:**
   * In the app's settings, find and click on 'Reveal Config Vars'.
   * Add the following variables with their corresponding values:
     * `DATABASE_URL`: Your ElephantSQL Database URL
     * `SECRET_KEY`: Your chosen Django secret key
     * `CLOUDINARY_URL`: Your Cloudinary URL
     * `DISABLE_COLLECTSTATIC`: Set to `1` for initial deployment
     * `PORT`: Set to `8000`

## Step 3: Deployment from GitHub

1. **Choose the Deploy option:**
   * Go to the Deploy tab in your app dashboard.

2. **Connect to GitHub:**
   * Under Deployment method, choose Connect to GitHub.

3. **Select your GitHub repository:**
   * Find your GitHub repository by name and connect.

4. **Choose deployment method:**
   * At the bottom of the page, choose either Automatic Deployment or Manual Deployment (deploy by branch).

5. **Initiate deployment:**
   * Click on the option you prefer, and the deployment process should begin.

6. **Monitor deployment progress:**
   * After a while, your app should be deployed. You can check the progress in the Heroku dashboard.


## Local Deployment

### How to Fork

**To fork the repository:**

1. Log in to Github.
2. Go to the repository for this project, [DylanP400/InkedClippers](https://github.com/DylanP400/terminal-dice-pp3)
3. Click the Fork button in the top right corner.

### How to clone

**To clone the repository**

1. Log in to GitHub.
2. Go to the repository for this project, [DylanP400/InkedClippers](https://github.com/DylanP400/InkedClippers)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

[Back to top](#inked-clippers-barbershop--tattoo-studio)


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
