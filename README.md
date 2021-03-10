University of Dayton

Department of Computer Science

CPS 491 Capstone II - Spring 2021

Team 1


## Capstone II


# Project Topic

Mattermost Chat Bot - Question Answer System
A chatbot that will answer any questions that are asked on a Mattermost server.


# Team members


1.  Sydney Jenkins, jenkinss4@udayton.edu
2.  Devin Porter, porterd3@udayton.edu
3.  David Puzder, puzderd1@udayton.edu
4.  Brandon Wong, wongb2@udayton.edu


# Company Mentors

Mentors: Kathryn Rebecca Servaites, Ian Cannon, Colin Leong, Alexander Graves

Company name: UD Research Institute 

# Project homepage

Homepage: <https://cps491s21-team1.bitbucket.io//>


# Overview

* Send questions typed into Mattermost server to an API (provided by UDRI), receive reply from the API and post reply to the chat.
* Save Mattermost chat from other users in the chat to the original question in the database as a possible answer to the question.
* Organise similar questions and determine which questions received the desired answer (reply).

# Project Context and Scope

It is difficult to keep documentation up-to-date when working in a fast-paced environment with
rapidly changing technologies. It is difficult to keep documentation organized and housed in a
central location that is accessible and searchable. Our solution to this problem is to create a
question-answer system in a chat application. This way, a researcher can type a question and
quickly receive an answer.

# System Analysis
## High-level Requirements

* Base Goals
	- Create a chatbot that will take questions from a user and send them to an API endpoint.
	- Get response from the RESTful API endpoint and display it in the chat.
	- The chatbot shall function in a Mattermost application.
	- Python programming language.
	- Bitbucket repository (because private repo can be used for free) to house code and changes.
* Extended Goals
    - Store the questions and related answers in a database.
	- Organize similar questions, determine which ones received desired answer.


## Technology

* Swagger
* RESTful API
* Python
* Mattermost
* Docker
* Conda (Python package manager)
* Unit and functional testing
* Bitbucket
* Database management
* Linux, preferably Ubuntu 18 (Can install a partition on computer; use VM; Windows Subsystem for Linux)
* VS Code (preferred IDE)


# Project Management

BitBucket Repository URL: <https://bitbucket.org/cps491s21-team1/cps491s21t1-src/src/master/>

Trello URL: <https://trello.com/b/M0fvt0rZ/cps491s21-team1/>

We will follow the Scrum approach, thus your team needs to identify the task in each sprint cycles, team meeting schedules, including this Fall and next Spring semester. The planned schedule and sprint cycles for Spring 2021 are as follows. 

![Spring 2021 Timeline](https://capstones-cs-udayton.bitbucket.io/imgs/cps491s21timeline.png "Spring 2021 Timeline")


Below is the example of the Trello board timeline (Gantt chart) with sprint cycles but without tasks for Spring 2021: 

![Spring 2021 Timeline on Trello](https://capstones-cs-udayton.bitbucket.io/imgs/trello.png "Spring 2021 Timeline")


# Company Support

* API endpoint in which to send the questions and receive answers
* Guidance on how to use the different technologies
* Regular product owner meetings


# Team Activities

* Set up flowchart describing the overall process
* Set up Mattermost Server
* Set up Database (Amazon RDS or DynamoDB). This will be a long-term goal, separate from a base goal of providing the chatbot.
* Set up API via OpenAPI/SwaggerHub
* Work with outgoing and incoming webhooks in Mattermost to integrate our external application (the chatbot).
* Connect Mattermost and Database
* Learn how existing Python chatbots function - Study and track open source code for similar projects.
* Train chatbot
* Working with an example API from UDRI Team Member Alex


# Contributions: 

1.  Sydney Jenkins, 1200 minutes, contributed in OpenAPI research, MatterMost research, presentation, report
2.  David Puzder, 1200 minutes, contributed in OpenAPI research, MatterMost research, use cases, webhooks, 
3.  Devin Porter, 1200 minutes, contributed in OpenAPI research, MatterMost research, presentation, database
4.  Brandon Wong, 1200 minutes, contributed in OpenAPI research, MatterMost research, use cases, Trello

# Release Retrospective:

* Release retrospective for Release 1:
	* Sprint 0 consisted of meeting with UDRI to discuss first steps of the project, putting together our use case diagram and descriptions, and updating our Trello board accordingly.
	* Sprint 1 consisted of developing a flowchart describing the logic behind our project and set up the MatterMost server.
	* Sprint 2 consisted of setting up the AWS database and learning about incoming and outgoing webhooks using Mattermost.
	* Sprint 3 consisted of experimenting with SwaggerHub, learning more about OpenAPI (RESTful API), and learning more about outgoing webhooks.
	* Sprint 4 consisted of SwaggerHub researching and Flask server endpoint experiementation
	* Sprint 5 consisted of SwaggerHub blueprinting and codegen
	* Sprint 6 consisted of Endpoint functionality implementation and mock UDRI API implementation all locally

# Flowchart of Chatbot Process

![Flowchart](https://trello-attachments.s3.amazonaws.com/5faaedaf4b1bc338640acb11/60196585b257f670f0d21222/fa26c2d442d1acab9b4aa68a5303c778/Chatbot_FlowChart_Draft.png)

# Use Case Diagram

![Use Case Diagram](https://trello-attachments.s3.amazonaws.com/60099e9b2e8fbb6c29146a6e/301x253/e56c2b8008bcd09ad5ae2ba0f9f12557/Capstone_II_Use_Case_Diagram.png)


# Use Case Descriptions

![Ask Question Use Case](https://trello-attachments.s3.amazonaws.com/5faaedaf4b1bc338640acb11/6009997fffd5ef45959553d6/6824156bc97d505be7e5e802cc21b234/Screen_Shot_2021-01-21_at_10.09.11_AM.png)
![Ask Question Use Case](https://trello-attachments.s3.amazonaws.com/5faaedaf4b1bc338640acb11/6009997fffd5ef45959553d6/ae80136365ca98b56de3c66d48725000/Screen_Shot_2021-01-21_at_10.09.31_AM.png)

# System Design
## Use Case Realization
Our uses cases are realized in the implementation of our chatbot and how we created a flowchart.

# Implementation
Up to this point, we have implemented a simple, Swagger generated API endpoint which reacts to a POST request from any source with a valid JSON body. 

Upon receving a valid POST request, the endpoint will send the question included in the JSON body to a mock UDRI API, which currently returns a random string. Our endpoint then posts the answer to the "Town Square" Mattermost chat room via a pre-configured incoming webhook.

# Acknowledgements
We would like to thank UDRI for the oppurtunity to work on this project and Professor Phung for the continued support we have recieved throughout this release.


