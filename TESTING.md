# Contents

* [Manual Testing](#manual-testing)

* [Validation](#validation)

* [Lighthouse](#lighthouse)

* [Wave](#wave)


# Manual Testing

## Desktop

### Nav Bar

| Feature | User Action | Expected Result | Pass/Fail |
| :---| :---| :---| :---|
| Logo | Clicking on the Inked Clippers Logo | Redirects to the Home page | Pass |
| Home | Clicking on the home link | Redirects to the Home page | Pass |
| About | Clicking on the about link | Navigates to the About page | Pass |
| Barbers | Clicking on the barbers link | Navigates to the Barbers page | Pass |
| Tattoo | Clicking on the tattoo link | Navigates to the Tattoo page | Pass |
| Register | Clicking on the Register link | Navigates to the Register page | Pass |
| Login | Clicking on the Login link | Navigates to the Login page | Pass |
| Profile | Clicking on the Profile link | Navigates to the Profile page | Pass |
| Logout | Clicking on the logout link | Logs out the user | Pass |

### Footer

| Feature | User Action | Expected Result | Pass/Fail |
| :---| :---| :---| :---|
| Facebook Icon | Clicking on the Facebook icon | Opens Facebook.com | Pass |
| Twitter Icon | Clicking on the Facebook icon | Opens Twitter.com | Pass |
| Linkedin Icon | Clicking on the Facebook icon | Opens my Linkedin profile | Pass |
| Github Icon | Clicking on the Facebook icon | Opens the Inked Clippers repository | Pass |
| Phone number link | Clicking on Inked Clippers phone number | Asks the user to make a call with there chosen application | Pass |
| Email Address link | Clicking on Inked Clippers email address | Asks the user to open mail or gmail for sending an email | Pass |


### Home Page

| Feature | User Action | Expected Result | Pass/Fail |
| :---| :---| :---| :---|
| Down Arrow Button | When the user clicks the arrow pointing down | The user will be brought down to the testimonials section | Pass |
| Paignation buttons for testimonials | When the user clicks the button 1, 2 or 3, | The user will be brought to the next section of testimonials | Pass |
| Location Area | None | Location is displaying and the user can zoom and move around the map  | Pass |


### Tattoo Page

| Feature | User Action | Expected Result | Pass/Fail |
| :---| :---| :---| :---|
| Faq's buttons | The user clicks the arrow button to see more information for the common question | The Box extends to show the answer to the question | Pass |
| | The user clicks the arrow button to hide the answer to the question | The Box closes | Pass |
|  | The user clicks the arrow button for another question while having the last question box open | The previously viewed question will close and the new question will open | Pass |


### Register Page

| Feature | User Action | Expected Result | Pass/Fail |
| :---| :---| :---| :---|
| Account registration form | The user fills out the form to create an account | An account is created for the user | Pass |
| | The user trys to create an account with a username that is already registered | An error pops up in red telling the user "A user with that username already exists" | Pass |
| |  If the user trys to sign up with an email already registered | The user is unable to create an account and has to pick a email that is not already registered | Fail
| Sign up button | The user clicks the sign up button to create an account | The users account is created and they are logged in and redirected to the home page | Pass
| Already have an account? Sign in | When the user already has an account and click the sign in link | The user is redirected to the login page | Pass

### Login Page

| Feature | User Action | Expected Result | Pass/Fail |
| :---| :---| :---| :---|
| Login form | The user trys to login with an account that doesnt exist or with the wrong password | An error message pops up telling the user to "Please enter a correct username and password. Note that both fields may be case-sensitive." | Pass
| Sign up button | The user click enters there login information and clicks Login | The user is logged in and redirected to the home page | Pass
| Create An Account? Sign up link | The user doesnt have an account and clicks sign up | The user is redirected to the Register page | Pass


### Profile Page

| Feature | User Action | Expected Result | Pass/Fail |
| :---| :---| :---| :---|
| Update profile form | The user updates there profile | The page refreshes and the profile is updated | Pass
| The user try to change there name to an already taken name | An error message pops up telling the user "A user with that username already exists." | Pass
| Update button | After changing the user information the user click update | The page refreshes and the profile is updated | Pass
| Leave a review button | The user clicks the leave review button | The user is redirected to the add testimonial page | Pass
| User testimonial link | The user clicks the content inside there own testimonial | The user is redirected two the testimonial detail page | Pass
| Edit testimonial button | The user clicks the edit testimonial button | The user is redirected to the edit testimonial page | Pass
| Delete testimonial button | The user clicks the delete testimonial button | The user is redirected to the delete testimonial page | Pass


### Add Testimonial Page

| Feature | User Action | Expected Result | Desktop Pass/Fail | Mobile Pass/Fail
| :---| :---| :---| :---| :---|
| Add Testimonial Form | The user has a section to leave a review | The user can leave a review in the box | Pass | Pass
| | The user wants to leave a rating | The website has a select box with a star rating system | Pass | Pass
| | The user wants to rate the employee that they got a service from | The page has a drop down box with the employees name | Pass | Pass
| | The user wants to choose the service they got | The user has the option from Barber Tattoo Artist or Piercer | Pass | Pass
| Submit Button | When the user is finshed they press the Submit button | The review is added to the home page and to the users profile | Pass | Pass


### Testimonial Detail Page

| Feature | User Action | Expected Result | Desktop Pass/Fail | Mobile Pass/Fail
| :---| :---| :---| :---| :---|
| Edit button | The user clicks the edit button | The user is take to the edit testimonial page | Pass | Pass
| Delete button | The user clicks the delete button | The users testimonial is deleted | Pass | Pass


### Edit Testimonial Page

| Feature | User Action | Expected Result | Desktop Pass/Fail | Mobile Pass/Fail
| :---| :---| :---| :---| :---|
| Edit testimonial form | The user wants to edit there own testimonial | The testimonial form comes pre filled with the selected testimonial information | Pass | Pass
| Update button | The user has updated there testimonial and clicked update | The testimonial is updated and the user is redirected to the testimonial detail page | Pass | Pass

### Delete Testimonial Page

| Feature | User Action | Expected Result | Desktop Pass/Fail | Mobile Pass/Fail
| :---| :---| :---| :---| :---|
| Delete button | The user clicks the delete button | The users testimonial is deleted | Pass | Pass
| Retun home button | The user clicks the return home button | The users testimonial remains the same and the user is redirected to the home page | Pass | Pass

### Logout Page

| Feature | User Action | Expected Result | Desktop Pass/Fail | Mobile Pass/Fail
| :---| :---| :---| :---| :---|
| Sign in link | The user logs out and click the sign in link | The user is redirected to the login page | Pass | Pass

# Validation

## HTML Validation

<details>
<summary>Home page</summary>

* ![Home page](./static/images/readme/home-html-v.png)

</details>

<details>
<summary>About page</summary>

* ![About page](./static/images/readme/html-about-page-v.png)

</details>

<details>
<summary>Barber page</summary>

* ![Barber page](./static/images/readme/barbers-html-v.png)

</details>

<details>
<summary>Tattoo page</summary>

* ![Tattoo page](./static/images/readme/tattoo-html-v.png)

</details>

<details>
<summary>Register page</summary>

* ![Register page](./static/images/readme/register-html-v.png)

</details>

<details>
<summary>Login page</summary>

* ![Login page](./static/images/readme/login-html-v.png)

</details>

<details>
<summary>Logout page</summary>

* ![Logout page](./static/images/readme/logout-html-v.png)

</details>

<details>
<summary>Profile page</summary>

* ![Profile page](./static/images/readme/profile-html-v.png)

</details>

<details>
<summary>Add testimonial</summary>

* ![Add testimonial page](./static/images/readme/add-testimonial-html-v.png)

</details>

<details>
<summary>Edit testimonial</summary>

* ![Edit testimonial page](./static/images/readme/edit-testimonial-html-v.png)

</details>

<details>
<summary>Testimonial detail</summary>

* ![Testimonial detail page](./static/images/readme/testimonial-detail-html-v.png)

</details>

<details>
<summary>Delete testimonial</summary>

* ![Delete testimonial page](./static/images/readme/delete-testimonial-html-v.png)

</details>

## CSS Validation


<details>
<summary>Main CSS</summary>

* ![Main CSS](./static/images/readme/css/main-css-v.png)

</details>

## Python Validation

### Inked clippers app

<details>
<summary>Inked clippers app settings.py</summary>

* ![Inked clippers app settings](./static/images/readme/inked-clippers-settings-v.png)

</details>

<details>
<summary>Inked clippers app urls.py</summary>

* ![Inked clippers app urls](./static/images/readme/inked-clippers-urls-v.png)

</details>


<details>
<summary>Core app models.py</summary>

* ![Core app models](./static/images/readme/core-models-v.png)

</details>

### Core app

<details>
<summary>Core app urls.py</summary>

* ![Core app url](./static/images/readme/core-urls-v.png)

</details>

<details>
<summary>Core app views.py</summary>

* ![Core app views](./static/images/readme/core-views-v.png)

</details>

<details>
<summary>Core app forms.py</summary>

* ![Core app forms](./static/images/readme/core-forms-v.png)

</details>


### Users app

<details>
<summary>Users app models.py</summary>

* ![Users app models](./static/images/readme/users-models-v.png)

</details>

<details>
<summary>Users app views.py</summary>

* ![Users app views](./static/images/readme/users-views-v.png)

</details>

<details>
<summary>Users app forms.py</summary>

* ![Users app forms](./static/images/readme/users-forms-v.png)

</details>

<details>
<summary>Users app signals.py</summary>

* ![Users app signals](./static/images/readme/users-signals-v.png)

</details>

### barber_services.py

<details>
<summary>barber_services.py</summary>

* ![Barber services](./static/images/readme/barber-services-v.png)

</details>

### tattoo_services.py

<details>
<summary>tattoo_services.py</summary>

* ![Tattoo services](./static/images/readme/tattoo-services-v.png)

</details>

###

# Lighthouse 

<details>
<summary>Home page</summary>

* Desktop
  * ![Home page desktop](./static/images/readme/lighthouse/home-page-desktop.png)

* Mobile
  * ![Home page mobile](./static/images/readme/lighthouse/home-page-mobile.png)


</details>

<details>
<summary>About page</summary>

* Desktop
  * ![About page desktop](./static/images/readme/lighthouse/about-page-desktop.png)

* Mobile
  * ![Home page mobile](./static/images/readme/lighthouse/about-page-mobile.png)
</details>

<details>
<summary>Barbers page</summary>

* Desktop
    * ![Barbers page desktop](./static/images/readme/lighthouse/barbers-page-desktop.png)

* Mobile
    * ![Barbers page mobile](./static/images/readme/lighthouse/barbers-page-mobile.png)
</details>

<details>
<summary>Tattoo page</summary>

* Desktop
    * ![Tattoo page desktop](./static/images/readme/lighthouse/tattoo-page-desktop.png)

* Mobile
    * ![Home page mobile](./static/images/readme/lighthouse/tattoo-page-mobile.png)
</details>

<details>
<summary>Profile page</summary>

* Desktop
    * ![Profie page desktop](./static/images/readme/lighthouse/profile-page-desktop.png)

* Mobile
    * ![Profile page mobile](./static/images/readme/lighthouse/profile-page-mobile.png)
</details>

<details>
<summary>Register page</summary>

* Desktop
    * ![Register page desktop](./static/images/readme/lighthouse/register-page-desktop.png)

* Mobile
    * ![Register page mobile](./static/images/readme/lighthouse/register-page-mobile.png)
</details>

<details>
<summary>Login page</summary>

* Desktop
    * ![Login page desktop](./static/images/readme/lighthouse/login-page-desktop.png)

* Mobile
    * ![Login page mobile](./static/images/readme/lighthouse/login-page-mobile.png)
</details>

<details>
<summary>Add testimonial page</summary>

* Desktop
    * ![Add testimonial page desktop](./static/images/readme/lighthouse/add-testimonial-desktop.png)

* Mobile
    * ![Add testimonial page mobile](./static/images/readme/lighthouse/add-testimonial-mobile.png)
</details>

<details>
<summary>Edit testimonial page</summary>

* Desktop
    * ![Edit testimonial page desktop](./static/images/readme/lighthouse/edit-testimonial-desktop.png)

* Mobile
    * ![Edit testimonial page mobile](./static/images/readme/lighthouse/edit-testimonial-mobile.png)
</details>

<details>
<summary>Delete testimonial page</summary>

* Desktop
    * ![Delete testimonial page desktop](./static/images/readme/lighthouse/delete-testimonial-desktop.png)

* Mobile
    * ![Delete testimonial page mobile](./static/images/readme/lighthouse/delete-testimonial-mobile.png)
</details>

<details>
<summary>Testimonial detail page</summary>

* Desktop
    * ![Testimonial detail page desktop](./static/images/readme/lighthouse/testimonial-detail-desktop.png)

* Mobile
    * ![Testimonial detail page mobile](./static/images/readme/lighthouse/testimonial-detail-mobile.png)
</details>

<details>
<summary>Logout page</summary>

* Desktop
    * ![Logout page desktop](./static/images/readme/lighthouse/logout-desktop.png)

* Mobile
    * ![Logout page mobile](./static/images/readme/lighthouse/logout-mobile.png)
</details>

###

# Wave

<details>
<summary>Home page</summary>

* ![home page wave results](./static/images/readme/wave/home-page-wave.png)
</details>

<details>
<summary>About page</summary>

* ![About page wave results](./static/images/readme/wave/about-page-wave.png)
</details>

<details>
<summary>Barbers page</summary>

* ![Barbers page wave results](./static/images/readme/wave/barbers-page-wave.png)
</details>

<details>
<summary>Tattoo page</summary>

* ![Tattoo page wave results](./static/images/readme/wave/tattoo-page-wave.png)
</details>

<details>
<summary>Register page</summary>

* ![Register page wave results](./static/images/readme/wave/register-page-wave.png)
</details>

<details>
<summary>Login page</summary>

* ![Login page wave results](./static/images/readme/wave/login-wave.png)
</details>

<details>
<summary>Profile page</summary>

* ![Profile page wave results](./static/images/readme/wave/profile-wave.png)
</details>

<details>
<summary>Add testimonial page</summary>

* ![Add testimonial page wave results](./static/images/readme/wave/add-testimonial-wave.png)
</details>

<details>
<summary>Testimonial detail page</summary>

* ![Testimonial detail page wave results](./static/images/readme/wave/testimonial-detail-wave.png)
</details>

<details>
<summary>Edit testimonial page</summary>

* ![Edit testimonial page wave results](./static/images/readme/wave/edit-testimonial-wave.png)
</details>

<details>
<summary>Delete testimonial page</summary>

* ![Delete testimonial page wave results](./static/images/readme/wave/delete-testimonial-wave.png)
</details>

<details>
<summary>Logout page</summary>

* ![Logout page wave results](./static/images/readme/wave/logout-wave.png)
</details>