<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Reflections](#reflections)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
    - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
      - [Must-Have Features](#must-have-features)
      - [Should-Have Features](#should-have-features)
      - [Could-Have Features](#could-have-features)
      - [Wont-Have Features](#wont-have-features)
  - [Early Design](#early-design)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Landing Page](#landing-page)
    - [Navigation & User Experience](#navigation--user-experience)
    - [CRUD Features](#crud-features)
    - [Design Philosophy](#design-philosophy)
    - [Accessibility Features](#accessibility-features)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Browser Testing](#browser-testing)
    - [Validator Testing](#validator-testing)
  - [Technologies Used](#technologies-used)
    - [Database Structure](#database-structure)
    - [Future Features](#future-features)
    - [Known Bugs](#known-bugs)
  - [Deployment Instructions](#deployment-instructions)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Reflections

> A blog for sharing our reflections and insights on the full-stack code institute course.

You can access the blog [here](https://hackathon-fullstack-207046bedb7e.herokuapp.com).


...

## Project Overview

<details>
A website built using Django which allows users to share blogs about their Reflections on the Bootcamp and to comment on the Reflections shared. Our group were inspired to build Reflections by our experiences on the Bootcamp. Reflections is our Full Stack Hackathon project. This project uses and demonstrates a culmination of our learning  on the course.

Technologies and Methodologies used:

- PostgreSQL, integrated through Django - for Database Management
- HTML, CSS, JavaScript - for Frontend Development
- Python, Django framework - for Backend Development
- Cloudinary - for API
- Using AI tools, e.g. Copilot and  ChatGPT 4.0 in the planning and debugging process
- Agile methodology - for Project planning and tracking
- Git & GitHub - for Version Control
- Heroku - for deployment
</details>

## User Experience (UX)

<details>

### User Stories

#### Must-Have Features
1. As a Site User, I can click on a post so that I can read the full text.
2. As a Site User I can register an account so that I can comment on a post.
3. As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
4. As a Site Admin I can create draft posts so that I can finish writing the content later
5. As a Developer I want to create a README.md so that anyone looking at the project has the required documentation.

#### Should-Have Features
1. As a site user, I can view a paginated list of posts so that I can select which post I want to view.
2. As a Site User / Admin I can view comments on an individual post so that I can read the conversation
3. As a Site User I can leave comments on a post so that I can be involved in the conversation
4. As a Site User I can modify or delete my comment on a post so that I can be involved in the conversation
5. As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
6. As a Site User, I can click on the About link so that I can read about the site.
7. As a Site Admin, I can create or update the about page content so that it is available on the site.
8. As a Site Admin I want to add some actual blog content so that site users can see it and comment on it on the site.


#### Could-Have Features

1. As a Potential Collaborator I can fill in a contact form so that I can submit a request for collaboration.
2. As a Site Owner I can store collaboration requests in the database so that I can review them.
3. As a Site Owner I can mark collaboration requests as "read" so that I can see how many I still need to process

#### Wont-Have Features

</details>


## Early Design

<details>

### Wireframes


</details>

## Features

<details>
### Landing Page

### Navigation & User Experience

### CRUD Features

### Design Philosophy

### Accessibility Features

</details>

## Testing

<details>

### Manual Testing

### Browser Testing

### Validator Testing

</details>

## Technologies Used

<details>

- PostgreSQL, integrated through Django - for Database Management
- HTML, CSS, JavaScript - for Frontend Development
- Python, Django framework - for Backend Development
- Cloudinary - for API
- USING AI TOOLS, e.g. .......
- Git & GitHub - for Version Control
- Heroku - for deployment
</details>

### Database Structure

### Future Features

### Known Bugs

</details>

## Deployment Instructions
<details>

- Deployment is to Heroku
- High-Level Steps to deploy to Heroku: 
  1. Configure the Django settings to handle both development and production environments.
  2. Environment variables are used to manage sensitive information and configuration settings. 
  3. PostgreSQL is the database used for production on Heroku.
  4. WhiteNoise middleware is used to manage static files in production.
  5. Debug mode is set to False in the settings file before commiting and pushing to Github.
  6. The project is deployed to Heroku using Github integration. Deployment is from the main branch. 
  7. The requirements.txt file handles the dependecies to ensure that all required packages are installed in the production environment.
  8. The deployed to Heroku project is tested to check that the functionality and design are consistent with those on the development environment.
  9. Testing and validation is carried out on the deployed to Heroku project.
  10. To emphasise again environment variables store sensitive data and DEBUG is set to False in the production environment.
</details>

## Credits
<details>

### Code
<details>
Extra code from Codestar walkthrough project from Code Institute 
</details>