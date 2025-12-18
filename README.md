# Reflections

**A collaborative blog platform for sharing reflections and insights on the Code Institute Full Stack Bootcamp experience.**

🔗 **Live Site:** [https://hackathon-fullstack-207046bedb7e.herokuapp.com](https://hackathon-fullstack-207046bedb7e.herokuapp.com)

![Reflections Homepage](README_assets/wireframeV1.png)

---

## Table of Contents

- [Project Overview](#project-overview)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Early Design](#early-design)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [CRUD Functionality](#crud-functionality)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks & Libraries](#frameworks--libraries)
  - [Tools & Services](#tools--services)
- [Database Structure](#database-structure)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)
- [License](#license)

---


## Project Overview

**Reflections** is a full-stack Django web application developed as a group hackathon project for the Code Institute Full Stack Bootcamp. The platform enables students to share their experiences, insights, and reflections about the bootcamp journey through blog posts and engage with each other through comments.

### Purpose

The project was inspired by our collective experiences on the bootcamp. It serves as:
- A platform for students to document their learning journey
- A space for sharing knowledge and insights
- A demonstration of skills learned throughout the course
- A collaborative team project showcasing agile development practices

### Key Highlights

- **Full CRUD Functionality**: Users can create, read, update, and delete blog posts and comments
- **User Authentication**: Secure registration and login system using Django Allauth
- **Content Moderation**: Admin approval system for posts and comments to maintain quality
- **Responsive Design**: Mobile-first approach ensuring accessibility across all devices
- **Image Management**: Cloudinary integration for efficient image hosting and delivery
- **Rich Text Editing**: Summernote integration for enhanced content creation

### Technologies and Methodologies

- **Backend**: Python with Django 4.2 framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: PostgreSQL (production), SQLite (development)
- **Media Storage**: Cloudinary API
- **Authentication**: Django Allauth
- **Deployment**: Heroku
- **Version Control**: Git & GitHub
- **Project Management**: Agile methodology with user stories and sprints
- **AI Assistance**: GitHub Copilot and ChatGPT for planning and debugging

---


## User Experience (UX)

### Target Audience

- Current Code Institute bootcamp students
- Alumni wanting to share their experiences
- Prospective students researching the bootcamp
- Instructors and mentors engaging with student reflections

### User Goals

- **Students**: Share experiences, learn from peers, track personal growth
- **Readers**: Gain insights into the bootcamp experience, engage with content
- **Administrators**: Moderate content, manage the community platform


### User Stories

Our development followed an agile approach with user stories prioritized using the MoSCoW method:

#### Must-Have Features ✅

1. **Post Reading**: As a Site User, I can click on a post so that I can read the full content
2. **User Registration**: As a Site User, I can register an account so that I can comment on posts
3. **Post Management**: As a Site Admin, I can create, read, update and delete posts so that I can manage blog content
4. **Draft Posts**: As a Site Admin, I can create draft posts so that I can finish writing content later
5. **Documentation**: As a Developer, I want to create comprehensive README documentation

#### Should-Have Features ✅

1. **Pagination**: As a Site User, I can view a paginated list of posts so that I can easily browse content
2. **View Comments**: As a Site User/Admin, I can view comments on posts so that I can read conversations
3. **Leave Comments**: As a Site User, I can leave comments on posts so that I can participate in discussions
4. **Manage Comments**: As a Site User, I can modify or delete my comments so that I can control my contributions
5. **Comment Moderation**: As a Site Admin, I can approve or disapprove comments so that I can filter inappropriate content
6. **About Page**: As a Site User, I can access an About page so that I can learn about the platform
7. **About Page Management**: As a Site Admin, I can update the About page content
8. **Blog Content**: As a Site Admin, I can add blog posts so that users can engage with content

#### Could-Have Features ✅

1. **Collaboration Requests**: As a Potential Collaborator, I can submit a collaboration request through a contact form
2. **Request Storage**: As a Site Owner, I can store collaboration requests in the database for review
3. **Request Management**: As a Site Owner, I can mark requests as "read" to track processing status

#### Won't-Have Features (Future Scope)

- User profiles with avatars and bios
- Post categories and tags
- Search functionality
- Email notifications for comments
- Social media sharing integration
- Like/upvote system for posts

---


## Early Design

### Design Philosophy

The design focuses on:
- **Simplicity**: Clean, distraction-free reading experience
- **Accessibility**: WCAG compliant with semantic HTML
- **Responsiveness**: Mobile-first approach for all devices
- **Consistency**: Bootstrap components for familiar UX patterns

### Wireframes

![Homepage Wireframe](README_assets/wireframeV1.png)

![Mobile Homepage Wireframe](README_assets/wireframeMobileV1.png)

## Features

### Existing Features

#### 🏠 Home Page (`/`)

The homepage serves as the central hub for browsing blog posts:
- **Responsive navbar** with site logo and navigation links
- **Authentication status** clearly displayed
- **Paginated blog posts** (6 posts per page) displaying:
  - Post title and author
  - Featured image (via Cloudinary)
  - Excerpt preview
  - Creation date
- **Card-based layout** for easy scanning
- **Footer** with social media links
- **Dynamic content** based on user authentication status

#### 📝 Post Detail Page (`/post/<slug>/`)

Individual post pages provide full content and interaction:
- **Full blog post** with rich text formatting
- **Author and metadata** (creation/update dates)
- **Featured image display**
- **Comments section** showing approved comments
- **Comment form** for authenticated users
- **Edit/Delete options** for comment owners
- **Approval status indicator** for pending comments

#### 👤 User Authentication

Secure authentication system using Django Allauth:
- **Registration** (`/accounts/signup/`): Create new account with email verification
- **Login** (`/accounts/login/`): Secure sign-in for existing users
- **Logout** (`/accounts/logout/`): Safe sign-out with confirmation
- **Password Management**: Reset and change password functionality
- **Multi-Factor Authentication**: Optional MFA support

#### ℹ️ About Page (`/about/`)

Informational page about the platform:
- **Dynamic content** managed through admin panel
- **Profile image** display
- **Collaboration request form** for potential contributors
- **Contact information**

#### 🛠️ Admin Dashboard (`/admin/`)

Comprehensive content management system:
- **Post Management**: Create, edit, delete blog posts; set status (Draft/Published)
- **Comment Moderation**: Approve/disapprove comments
- **User Management**: Manage user accounts and permissions
- **About Page Editor**: Update site information
- **Collaboration Requests**: Review and manage contact form submissions
- **Summernote Integration**: Rich text editor for content creation

#### 💬 Interactive Features

- **Success Messages**: User-friendly confirmation notifications
- **Error Handling**: Clear validation and error messages
- **Responsive Design**: Seamless experience across all devices
- **Accessibility**: ARIA labels and semantic HTML structure

### CRUD Functionality

The platform implements full CRUD (Create, Read, Update, Delete) operations:

#### Posts (Admin Only)
- **Create**: Admins can create new blog posts through the admin panel
- **Read**: All users can view published posts
- **Update**: Admins can edit existing posts
- **Delete**: Admins can remove posts from the platform

#### Comments (Authenticated Users)
- **Create**: Logged-in users can add comments to posts
- **Read**: All users can view approved comments
- **Update**: Users can edit their own comments
- **Delete**: Users can delete their own comments

#### About Page Content (Admin Only)
- **Create/Update**: Admins manage the About page content
- **Read**: All users can view the About page

#### Collaboration Requests (All Users)
- **Create**: Anyone can submit collaboration requests
- **Read**: Admins can view all requests in admin panel
- **Update**: Admins can mark requests as read

---

## Testing

### Manual Testing

Comprehensive manual testing was conducted throughout the development process and after deployment. Testing covered:

#### Functionality Testing

| Feature | Test Case | Expected Result | Status |
|---------|-----------|-----------------|--------|
| User Registration | Create new account | Account created, user logged in | ✅ Pass |
| User Login | Login with valid credentials | User authenticated, redirected to home | ✅ Pass |
| User Logout | Logout | User signed out, session cleared | ✅ Pass |
| View Posts | Browse post list | Posts displayed with pagination | ✅ Pass |
| Read Post | Click on post | Full post content displayed | ✅ Pass |
| Create Comment | Submit comment (logged in) | Comment saved, pending approval | ✅ Pass |
| Edit Comment | Update own comment | Changes saved successfully | ✅ Pass |
| Delete Comment | Remove own comment | Comment deleted, confirmation shown | ✅ Pass |
| Admin Create Post | Create post via admin | Post saved to database | ✅ Pass |
| Admin Approve Comment | Approve comment | Comment visible on site | ✅ Pass |
| Collaboration Form | Submit request | Request saved, confirmation shown | ✅ Pass |

#### Browser Compatibility

Tested on:
- ✅ Google Chrome (latest)
- ✅ Mozilla Firefox (latest)
- ✅ Microsoft Edge (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

#### Responsive Design Testing

Tested on multiple device sizes:
- ✅ Desktop (1920x1080, 1366x768)
- ✅ Tablet (768x1024)
- ✅ Mobile (375x667, 414x896)

### Validator Testing

#### HTML Validation
- ✅ All templates validated using [W3C HTML Validator](https://validator.w3.org/)
- ✅ No errors found

#### CSS Validation
- ✅ Stylesheet validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- ✅ No errors found

#### Python/Django
- ✅ Code follows PEP 8 style guidelines
- ✅ No linting errors in Python files
- ✅ All Django tests pass

#### JavaScript
- ✅ Code validated using JSHint
- ✅ No significant errors

#### Accessibility
- ✅ Lighthouse accessibility score: 90+
- ✅ WCAG 2.1 Level AA compliant
- ✅ Semantic HTML structure
- ✅ ARIA labels where appropriate

---

## Technologies Used

### Languages

- **Python 3.11**: Backend logic and server-side processing
- **HTML5**: Structure and content markup
- **CSS3**: Styling and visual presentation
- **JavaScript**: Client-side interactivity

### Frameworks & Libraries

#### Backend
- **Django 4.2.26**: Python web framework
- **django-allauth 0.57.2**: Authentication and user management
- **django-crispy-forms 2.5**: Form styling
- **crispy-bootstrap5 0.7**: Bootstrap 5 integration for forms
- **django-summernote 0.8.20.0**: WYSIWYG rich text editor
- **psycopg2 2.9.11**: PostgreSQL database adapter
- **dj-database-url 0.5.0**: Database configuration from environment
- **gunicorn 20.1.0**: WSGI HTTP server for production
- **whitenoise 5.3.0**: Static file serving

#### Frontend
- **Bootstrap 5**: CSS framework for responsive design
- **Font Awesome**: Icon library
- **jQuery**: DOM manipulation (required by Summernote)

### Tools & Services

- **Cloudinary**: Cloud-based image and media management
- **PostgreSQL**: Production database (via Heroku)
- **SQLite**: Development database
- **Git**: Version control
- **GitHub**: Code repository and collaboration
- **Heroku**: Cloud platform for deployment
- **VS Code**: Primary code editor
- **GitHub Copilot**: AI-assisted coding
- **ChatGPT**: Planning and debugging assistance

---

### Database Structure

![ERD](README_assets/erdV1.png)

The database schema consists of the following models:

#### Post Model
```python
- id: Primary Key
- title: CharField (max 200, unique)
- slug: SlugField (unique)
- author: ForeignKey (User)
- featured_image: CloudinaryField
- content: TextField
- excerpt: TextField
- status: IntegerField (Draft=0, Published=1)
- approved: BooleanField
- created_on: DateTimeField
- updated_on: DateTimeField
```

#### Comment Model
```python
- id: Primary Key
- post: ForeignKey (Post)
- author: ForeignKey (User)
- body: TextField
- approved: BooleanField
- created_on: DateTimeField
```

#### About Model
```python
- id: Primary Key
- title: CharField (max 200)
- content: TextField
- profile_image: CloudinaryField
- updated_on: DateTimeField
```

#### CollaborateRequest Model
```python
- id: Primary Key
- name: CharField (max 200)
- email: EmailField
- message: TextField
- read: BooleanField
```

### Relationships
- One User can have many Posts (One-to-Many)
- One User can have many Comments (One-to-Many)
- One Post can have many Comments (One-to-Many)

---

## Deployment

### Local Development

1. **Clone the repository**:
  ```bash
  git clone https://github.com/yourusername/reflections.git
  cd reflections
  ```

2. **Create virtual environment**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. **Install dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

4. **Create `env.py` file** in the root directory:
  ```python
  import os

  os.environ["DATABASE_URL"] = "your-database-url"
  os.environ["SECRET_KEY"] = "your-secret-key"
  os.environ["CLOUDINARY_URL"] = "your-cloudinary-url"
  ```

5. **Run migrations**:
  ```bash
  python manage.py migrate
  ```

6. **Create superuser**:
  ```bash
  python manage.py createsuperuser
  ```

7. **Run development server**:
  ```bash
  python manage.py runserver
  ```

### Heroku Deployment

1. **Create Heroku app**:
  - Sign up/login to [Heroku](https://heroku.com)
  - Click "New" > "Create new app"
  - Choose app name and region

2. **Add PostgreSQL database**:
  - Go to Resources tab
  - Search for "Heroku Postgres"
  - Select free plan

3. **Configure environment variables** in Settings > Config Vars:
  ```
  DATABASE_URL: (automatically added by Postgres)
  SECRET_KEY: your-secret-key
  CLOUDINARY_URL: cloudinary://...
  DISABLE_COLLECTSTATIC: 1 (during development)
  ```

4. **Deploy from GitHub**:
  - Go to Deploy tab
  - Connect to GitHub repository
  - Enable automatic deploys from main branch
  - Click "Deploy Branch"

5. **Run migrations** (in Heroku console or locally):
  ```bash
  heroku run python manage.py migrate
  ```

6. **Create superuser**:
  ```bash
  heroku run python manage.py createsuperuser
  ```

### Important Notes
- Set `DEBUG = False` in production
- Keep `SECRET_KEY` and database credentials secure
- Ensure all dependencies are in `requirements.txt`
- Use environment variables for sensitive data

---

## Future Enhancements

Potential features for future development:

### High Priority
- **User Profiles**: Extended profiles with avatars, bio, and activity history
- **Post Categories/Tags**: Organize posts by topics (e.g., HTML/CSS, JavaScript, Python, Django)
- **Search Functionality**: Full-text search for posts and comments
- **Email Notifications**: Alerts for comment replies and post updates

### Medium Priority
- **Like/Upvote System**: Allow users to like posts and comments
- **Social Sharing**: Share posts on social media platforms
- **Draft Autosave**: Automatic saving of draft comments
- **Markdown Support**: Alternative to WYSIWYG for tech-savvy users
- **Code Syntax Highlighting**: Better display of code snippets in posts

### Low Priority
- **User Following**: Follow other users to see their posts
- **Bookmarks**: Save favorite posts for later reading
- **Dark Mode**: Theme toggle for better readability
- **RSS Feed**: Subscribe to blog updates
- **Analytics Dashboard**: Track post views and engagement

---

## Credits

### Team Members
This project was developed as a collaborative team effort during the Code Institute Full Stack Hackathon.

### Code & Resources
- **Code Institute**: Codestar blog walkthrough project provided foundational structure
- **Django Documentation**: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **Bootstrap Documentation**: [https://getbootstrap.com/](https://getbootstrap.com/)
- **Django Allauth**: [https://django-allauth.readthedocs.io/](https://django-allauth.readthedocs.io/)
- **Cloudinary**: [https://cloudinary.com/documentation](https://cloudinary.com/documentation)

### AI Assistance
- **GitHub Copilot**: Code completion and suggestions
- **ChatGPT 4.0**: Planning, debugging, and problem-solving

### Media & Assets
- Default placeholder images from [Cloudinary](https://cloudinary.com)
- Icons from [Font Awesome](https://fontawesome.com)

### Acknowledgments
- Code Institute instructors and mentors
- Fellow bootcamp students for inspiration and support
- Stack Overflow community for troubleshooting assistance

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ by Code Institute Bootcamp Students | December 2025**