# crowdfunding_back_end
by: Roberta De Cecco

### Live website link: [EDUKidz](https://crowdfunding-back-end12345.fly.dev/projects/)


## Planning: 
A repo to contain my She Codes Crowdfunding backend project.
This project used:
* Django Rest framework to build the backbone of the website/APIs. 
* Insomnia to show the APIs/Endpoints functionalities
* Fly.io to deploy the live version


## Concept/Name
**'EDUKidz'** is a platform that empowers individuals to crowdfund initiatives for underprivileged children, enabling them to access education and pursue their dreams. These children, filled with aspirations for themselves, their families, and their communities, often face financial barriers or geographic limitations that prevent them from attending school. EDUKidz bridges this gap by providing the tools and resources they need to unlock their full potential.



## Intended Audience/User Stories
 
EDUKidz platform likely targets two main audiences:

**1. Potential donors:**

**- Individuals passionate about education and supporting underprivileged children:** This could include people who have themselves benefited from good education or who simply believe in its transformative power.
**- Parents and families:** Parents who value education and might be looking for ways to support children in need, potentially even families who have emigrated from similar situations.
**-Philanthropic organizations and foundations:** Groups seeking to support educational causes and empower underprivileged communities.

**2. Potential beneficiaries:**

**-Children in need of financial assistance for education:** This could include children from low-income families, orphans, or children living in remote areas with limited access to schools.
**- Schools and educational institutions:** These institutions could utilize the platform to raise funds for specific needs or projects, improving their facilities or resources for students.

It's important to note that EDUKidz might also target individuals who can raise awareness for the platform and its causes. This could include educators, social media influencers, or celebrities who can help spread the word and attract potential donors and beneficiaries.


## Front End Pages/Functionality - COMING SOON
- {{ A page on the front end }}    
- {{ A list of dot-points showing functionality is available on this page }}    
    - {{ etc }}    
    - {{ etc }}
- {{ A second page available on the front end }}    
- {{ Another list of dot-points showing functionality }}    
    - {{ etc }}


## API Specs:

| **HTTP Method** | **URL**         | **Purpose**                                          | **Request Body** | **Successful Response Code** | **Authentication/Authorization**                |
|-----------------|-----------------|------------------------------------------------------|------------------|------------------------------|-------------------------------------------------|
| POST            | api-token-auth/ | Returns a token for authenticate the user logging in | User object      | 200                          | N/A                                             |
| GET             | /projects/      | Returns all projects.                                | N/A              | 200                          | N/A                                             |
| GET             | /projects/1     | Returns the project with ID = 1                      | N/A              | 200                          | N/A                                             |
| POST            | /projects/      | Creates a new project                                | Project object   | 201                          | Must be logged in.                              |
| PUT             | /projects/1/    | Updates the project with ID = 1                      | Project object   | 200                          | Must be logged in. Must be the project owner.   |
| DELETE          | /projects/1/    | Deleted the project with ID = 1                      | N/A              | 200                          | Must be logged in. Must be the project owner.   |
| GET             | /users/         | Returns all users.                                   | N/A              | 200                          | N/A                                             |
| GET             | /users/1        | Returns the user with ID = 1                         | N/A              | 200                          | N/A                                             |
| POST            | /users/         | Creates a new user.                                  | User object      | 201                          | N/A                              |
| PUT             | /users/1/       | Updates the user with ID = 1                         | User object      | 200                          | Must be logged in. Must be the user with ID = 1 |
| GET             | /pledges/       | Returns all pledges.                                 | N/A              | 200                          | N/A                                             |
| GET             | /pledges/1      | Returns the pledge with ID = 1                       | N/A              | 200                          | N/A                                             |
| POST            | /pledges/       | Creates a new pledge.                                | Pledge object    | 201                          | Must be logged in.                              |
| PUT             | /pledges/1/     | Updates the pledge with ID = 1                       | Pledge object    | 200                          | Must be logged in. Must be the pledge owner     |



## Project Requirements

This crowdfunding project must:
* [x] Be separated into two distinct projects: an API built using the Django RestFramework and a website built using React.
* [x] Have a cool name, bonus points if it includes a pun and/or missing vowels. See https://namelix.com/ for inspiration. (Bonus Points are meaningless)
* [x] Have a clear target audience.
* [x] Have user accounts. A user should have at least the following attributes:
    * [x] Username
    * [x] Email address
    * [x] Password
        * I also added:
            * First name
            * Last name

* [x] Ability to create a “project” to be crowdfunded which will include at least thefollowing attributes:
    * [x] Title
    * [x] Owner (a user)
    * [x] Description
    * [x] Image
    * [x] Target amount to fundraise
    * [x] Whether it is currently open to accepting new supporters or not
    * [x] When the project was created
* [x] Ability to “pledge” to a project. A pledge should include at least the followingattributes:
    *   [x] An amount
    *   [x] The project the pledge is for
    *   [x] The supporter/user (i.e. who created the pledge)
    *   [x] Whether the pledge is anonymous or not
    *   [x] A comment to go along with the pledge
    *   [x] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description? Yes, allowed to update project details and delete project if it is the owner.
* [x] Implement suitable permissions, e.g. who is allowed to delete a pledge? No one but I allowed to update Pledge details.
* [x] Return the relevant status codes for both successful and unsuccessful requeststo the API.
* [x] Handle failed requests gracefully (e.g. you should have a custom 404 pagerather than the default error page).
* [x] Use Token Authentication.
* [x] Implement responsive design.


## Submission requirements:

* [x] A link to the deployed project. 
    * Go to the top for the [Live Website link](#live-website-link-edukidz).
* [x] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
    * See the 'Images' folder in my Repo: [GitHub Crowdfunding Repo](https://github.com/RobyOneJ/crowdfunding_back_end).
* [x] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
    * See the 'Images' folder in my Repo: [GitHub Crowdfunding Repo](https://github.com/RobyOneJ/crowdfunding_back_end).
* [x] A screenshot of Insomnia, demonstrating a token being returned.
    * See the 'Images' folder in my Repo: [GitHub Crowdfunding Repo](https://github.com/RobyOneJ/crowdfunding_back_end).
* [x] Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

| **_Create New User_**    | **URL**                    | **Request Body in JSON format**                                                                                                                                                                                                                                     | **Request Body Example**                                                                                                                                                                                                                                     | **Successful Response** | **Authentication** |
|--------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------|
|                          | POST {{env_url}}/users/    | {     "is_superuser": false,     "username": "a_username",     "password": "a_password",     "first_name": "a_name",     "last_name": "a_surname",     "email": "an_email_address",     "is_staff": false,     "is_active": true,     "date_joined": "timestamp"  } | {    "is_superuser": false,    "username": "testusn",    "password": "testpwd",    "first_name": "Test",    "last_name": "User",    "email": "test@test.com",    "is_staff": false,    "is_active": true,    "date_joined": "2024-01-26T04:13:17.227000Z"  } | 201                     | N/A                |
| **_Create New Project_** | **URL**                    | **Request Body in JSON format**                                                                                                                                                                                                                                     | **Request Body Example**                                                                                                                                                                                                                                     | **Successful Response** | | **Authentication** |
|                          | POST {{env_url}}/projects/ | {    "title": "a_title for the project",    "description": "a_description",    "goal": an_amount,    "image": "a_url_image",    "is_open": true,    "date_created": "timestamp" }                                                                                   | {     "title": "Project One",     "description": "My first project!",     "goal": 10,     "image": "https://via.placeholder.com/300.jpg",     "is_open": true,     "date_created": "2020-03-20T14:28:23.382748Z" }                                           | 201                     | Token Authentication |


**Detailed steps for Create User:**
1. Use the api: 'POST{{env_url}}/users/'
2. In the JSON tab, add the 'Request Body Example' payload as shown in the above table (don't need a bearer token for this action as this is a new user signing up)
3. Click on 'Send' button to run the api call
Expected result: You should get a '200 OK' code and a response body with details
Check screenshots: StepsBySteps_CreateUser.PNG in the'Images' folder in my Repo


**Detailed steps to Create Project:**
1. User needs to be logged in -> generate a token 
2. Use the api: 'POST{{env_url}}/projects/'
3. Set up the JSON tab, add the 'Request Body Example, payload as shown in the above table - requires the token generated above in the Bearer tab
4. Click on 'Send' button to run the api call
Expected result: You should get a '201 Created' Code and a response body that looks like the on in screenshot: StepsBySteps_CreateProject.png
Check screenshots: StepsBySteps_CreateProject.PNG in the'Images' folder in my Repo

    * See also the screenshots in the'Images' folder in my Repo: [GitHub Crowdfunding Repo](https://github.com/RobyOneJ/crowdfunding_back_end).

* [x] Your refined [API Specification](#api-specs) table and Database Schema.
    * For the Database Schema, check the 'ERD.png' screenshot in the 'Images' folder.







