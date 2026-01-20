# Haus Kitchen

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
- [Wireframes](#wireframes)
- [AI Usage](#ai-usage)
- [User Stories](#user-stories)
- [Credits](#credits)
- [License](#license)

## Project Overview
Haus Kitchen is a web application designed to help users discover recipes. The project aims to provide a user-friendly platform for home cooks and food enthusiasts to manage their personal recipe collections and explore new dishes. A responsive site allows for ease of use for a range of users.

### Desktop
![Desktop screenshot](static/assets/images/readme/homess.png)

### Tablet
![Tabelt screenshot](static/assets/images/readme/tabss.png)

### Mobile
![Mobile screenshot](static/assets/images/readme/mobss.png)



## Features
- Home page
![Home](static/assets/images/readme/homess.png)
- Add Recipe
![Add recipe](static/assets/images/readme/addss.png)
- Favourite
![Favourite](static/assets/images/readme/favss.png)
- Admin 
![Admin](static/assets/images/readme/adminss.png)
- Sign up
![Signup](static/assets/images/readme/signupss.png)
- Sign in
![Signin](static/assets/images/readme/signinss.png)
- Sign out
![Signout](static/assets/images/readme/signoutss.png)
- Footer
![Footer](static/assets/images/readme/footerss.png)
- Navbar
![Nav](static/assets/images/readme/navss.png)



## Tech Stack
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap


## Getting Started
### Prerequisites
- Python version
- Django version
- Other dependencies

### Installation
```bash
# Clone the repository
git clone <repo-url>
cd haus_kitchen

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```
## Deployment
To deploy Haus Kitchen on Heroku:

### 1. Prepare for Deployment
- Ensure `requirements.txt` and `Procfile` are present in your project root.
- Add `gunicorn` to your `requirements.txt`:
    ```
    gunicorn
    ```
- Update `ALLOWED_HOSTS` in `settings.py` to include your Heroku app domain.

### 2. Configure Static Files
- Install `whitenoise` and add it to `requirements.txt`.
- Update `MIDDLEWARE` in `settings.py`:
    ```python
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ```
- Set static files settings:
    ```python
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```

### 3. Set Up Heroku
- Login and create a connect Github:
    ```bash
    heroku login
    Connect app via Github
    ```

### 4. Configure Environment Variables
- Set Django secret key and other environment variables:
    ```bash
    heroku config:set SECRET_KEY='your-secret-key'
    heroku config:set DEBUG=False
    ```

### 5. Add PostgreSQL
- Add Heroku Postgres:
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

### 6. Deploy
- Push your code to Heroku:
    ```bash
    git push heroku main
    ```
- Run migrations:
    ```bash
    heroku run python manage.py migrate
    ```
- (Optional) Create a superuser:
    ```bash
    heroku run python manage.py createsuperuser
    ```

### 7. Open Your App
- Visit your deployed app:
    ```bash
    heroku open
    ```

For more details, see the [Heroku Django deployment guide](https://devcenter.heroku.com/articles/deploying-python).

## Usage
Instructions and examples for using the application.

## Testing
### 🧪 Manual Testing Table - Haus Kitchen

## **Authentication & User Management**

| Feature | Expected Result | Result |
|---------|----------------|--------|
| User Registration | New user can register with username and password | ✅ Pass |
| User Login | Registered user can log in with valid credentials | ✅ Pass |
| User Logout | Logged-in user can successfully log out | ✅ Pass |

---

## **Recipe Browsing & Viewing**

| Feature | Expected Result | Result |
|---------|----------------|--------|
| Browse Recipes (Guest) | Visitors can view recipes without logging in | ✅ Pass |
| Recipe Pagination | Recipes display in paginated format | ✅ Pass |
| View Recipe Details | Complete recipe information displays (ingredients, instructions, time) | ✅ Pass |
| Mobile Responsive | All pages display correctly on mobile devices | ✅ Pass |

---

## **User Interactions**

| Feature | Expected Result | Result |
|---------|----------------|--------|
| Add Comment | Logged-in user can add comment to a recipe | ✅ Pass |
| Edit Comment | User can edit their own comment | ✅ Pass |
| Delete Comment | User can delete their own comment | ✅ Pass |
| Save Favorite Recipe | Logged-in user can save recipe to favorites | ✅ Pass |
| View Favorites | User can view all saved recipes on Favorites page | ✅ Pass |

---

## **Admin Functions**

| Feature | Expected Result | Result |
|---------|----------------|--------|
| Add Recipe (Admin) | Admin can add new recipe from front end | ✅ Pass |
| Edit Recipe (Admin) | Admin can edit existing recipes | ✅ Pass |
| Delete Recipe (Admin) | Admin can delete recipes | ✅ Pass |
| Moderate Comments | Admin can view, edit, and delete user comments | ✅ Pass |
| Admin Dashboard Access | Only logged-in admins can access admin functions | ✅ Pass |

---

## **Legend**
- ✅ **Pass** - Feature works as expected
- ❌ **Fail** - Feature does not work as expected
- 🔄 **Pending** - Feature not yet implemented
- ⚠️ **Issue** - Feature works with minor issues

---

## **Test Summary**
- **Total Tests:** 24
- **Passed:** 18 ✅
- **Pending:** 0 🔄
- **Failed:** 0 ❌

---
 
## Responsiveness testing
Boostrap was useed to achieve CSS responsiveness and Chrome Dev Tools were used regularly to check responsiveness across all device sizes

## Lighthouse
![Lighthouse screenshot](static/assets/images/readme/lhss.png)

## HTML Validator
![HTML screenshot](static/assets/images/readme/htmlvalss.png)

## CSS Validator
![CSS screenshot](static/assets/images/readme/cssval.png)

## AI Unit test
![Unit test screenshot](static/assets/images/readme/unittest.png)
![Python test screenshot](static/assets/images/readme/pythontest.png)


## Entity Relationship Diagram (ERD)
![ERD image](static/assets/images/readme/ss8.png)

## Wireframes
![Wireframe screenshot](static/assets/images/readme/ss1.png)
![Wireframe screenshot](static/assets/images/readme/ss2.png)
![Wireframe screenshot](static/assets/images/readme/ss3.png)
![Wireframe screenshot](static/assets/images/readme/ss4.png)
![Wireframe screenshot](static/assets/images/readme/ss5.png)
![Wireframe screenshot](static/assets/images/readme/ss6.png)
![Wireframe screenshot](static/assets/images/readme/ss7.png)

## AI Usage
Describe any AI/ML features, models, or APIs used in the project.

## User Stories
https://github.com/users/hauvoong/projects/9

## Bugs
- Integrating Summernote SummernoteTextField() into my recipe model and having incompatibility issues with Bleach. 
Solution: Downgrade Bleach to bleach==4.1.0

## Credits
- List contributors, libraries, or resources to credit.

## License
Specify the license for your project.
# Haus-Kitchen
