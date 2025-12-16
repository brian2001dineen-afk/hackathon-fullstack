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

## Table of Contents

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

### User Experience (UX)

### User Stories

#### Must-Have Features

#### Should-Have Features

#### Could-Have Features

#### Wont-Have Features

---

## Early Design

### Wireframes

---

## Features

### Landing Page

### Navigation & User Experience

### CRUD Features

### Design Philosophy

### Accessibility Features

---

## Testing

### Manual Testing

### Browser Testing

### Validator Testing

---

## Technologies Used

### Database Structure

### Future Features

### Known Bugs

---

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

---
