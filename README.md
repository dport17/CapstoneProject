# CPS 491 - Capstone II

University of Dayton

Department of Computer Science

CPS 491 Capstone II - Spring 2021

Team 1


## Capstone II Project


# Mattermost Chat Bot - Question Answer System
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

# Project Management Information

BitBucket Repository URL: <https://bitbucket.org/cps491s21-team1/cps491s21t1-src/src/master/>

Trello URL: <https://trello.com/b/M0fvt0rZ/cps491s21-team1/>


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

## Use Case Diagram

![Use Case Diagram](https://trello-attachments.s3.amazonaws.com/60099e9b2e8fbb6c29146a6e/211x180/c6d425882a18bfc5f5691e84e6a47693/Untitled_Diagram.png)

## Use Case Descriptions

![Ask Question Use Case](https://trello-attachments.s3.amazonaws.com/5faaedaf4b1bc338640acb11/6009997fffd5ef45959553d6/6824156bc97d505be7e5e802cc21b234/Screen_Shot_2021-01-21_at_10.09.11_AM.png)


## Flowchart of Chatbot Process

![Flowchart](https://trello-attachments.s3.amazonaws.com/5faaedaf4b1bc338640acb11/60881dd7a92fe01b720df6e9/f8a2412511309373f31ec951a9e30ced/Chatbot_FlowChart_Draft.png)


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


# Company Support

* API endpoint in which to send the questions and receive answers
* Guidance on how to use the different technologies
* Regular product owner meetings


# Team Activities

* Research various APIs, Mattermost, and Swaggerhub
* Set up flowchart describing the overall process
* Set up Mattermost Server
* Set up Database (Amazon RDS or DynamoDB). This will be a long-term goal, separate from a base goal of providing the chatbot.
* Set up API via OpenAPI/SwaggerHub
* Work with outgoing and incoming webhooks in Mattermost to integrate our external application (the chatbot).
* Connect Mattermost and Database
* Learn how existing Python chatbots function - Study and track open source code for similar projects.
* Train chatbot
* Working with an example API from UDRI Team Member Alex


# System Design
## Use Case Realization
In the flowchart and use case diagram above, we aim to show the logic from User's request to how an outgoing webhook on Mattermost will handle the request, communicate with UDRI's provided API, from which their API will send back a randomly generated response through an incoming webhook that will be displayed through Mattermost.

## User Interface
In order to call the chatbot, the user will use the #ask trigger word followed by the question in the Mattermost server
![UI](https://trello-attachments.s3.amazonaws.com/5faaedaf4b1bc338640acb41/950x248/6495ba8f12110ceaae410aa78bd13ff8/Screen_Shot_2021-04-13_at_10.04.44_AM.png)

# Implementation
## Release 2
Up to this point, we have implemented a simple, Swagger generated API endpoint which reacts to a POST request from any source with a valid JSON body. 
Upon receving a valid POST request, the endpoint will send the question included in the JSON body to a mock UDRI API, which currently returns a random string. Our endpoint then posts the answer to the "Town Square" Mattermost chat room via a pre-configured incoming webhook.

## Release 3
Now we have deployed our Swagger generated API onto Heroku after Dockerizing our code. We have also deployed UDRI's mock API onto Heroku using the method used in Capstone I. In one case, we needed a Dockerfile which laid out commands needed to run our application. In the other case, we needed a Procfile which also specified how run our application without Docker.

![Dockerfile](https://trello-attachments.s3.amazonaws.com/5f58131b90edaf09eab4ac6b/606b74040dbe628942e68885/3bb6878bc0f58655007b88832e47205a/dockerfile.JPG)

In the main file in which we did our coding (default_controller.py), there were two main sections. the receive_url_post method which contains what will be executed once a POST request is made to https://udri-chatbot.herokuapp.com/apis/puzderd1/MattermostChatbot/1.0.0/receive_url.
The other section is the getAnswer method in which we specify which other endpoint we are trying to reach. In our case, it is https://cps-491-mattermost-chatbot.herokuapp.com/receive_chat, which is the UDRI mock API.

![Dockerfile](https://trello-attachments.s3.amazonaws.com/5f58131b90edaf09eab4ac6b/606b74040dbe628942e68885/3f95b2424769fcdd743fde1bdb9408a8/receiveURL.JPG)
![Dockerfile](https://trello-attachments.s3.amazonaws.com/5f58131b90edaf09eab4ac6b/606b74040dbe628942e68885/d87bf09141d87e96b96b67e95ec1cd21/getAnswer.JPG)

# Software Process Management

We will follow the Scrum approach, thus our team identified each task in each sprint cycles. The planned schedule and sprint cycles for Spring 2021 are as follows. 

![Spring 2021 Timeline](https://capstones-cs-udayton.bitbucket.io/imgs/cps491s21timeline.png "Spring 2021 Timeline")


Below is our Trello board timeline (Gantt chart) with sprint cycles but without tasks for Spring 2021: 

![Spring 2021 Timeline on Trello](https://capstones-cs-udayton.bitbucket.io/imgs/trello.png "Spring 2021 Timeline")

# Contributions: 

1.  Sydney Jenkins, 3900 minutes, contributed in OpenAPI research, MatterMost research, presentation, report, UDRI liason, openAPI research, presentation preparation
2.  David Puzder, 3900 minutes, contributed in OpenAPI research, MatterMost research, use cases, webhooks, SwaggerHub API Blueprinting, outgoing webhooks, and codegen
3.  Devin Porter, 3900 minutes, contributed in OpenAPI research, MatterMost research, presentation, database, endpoint functionality implementation, mock UDRI API call, JOSN customization
4.  Brandon Wong, 3900 minutes, contributed in OpenAPI research, MatterMost research, use cases, Trello, Demo testing, flask RESTful API research, Heroku deployment

# Release Retrospective:

* Release retrospective for Release 1:
	* Sprint 0 consisted of meeting with UDRI to discuss first steps of the project, putting together our use case diagram and descriptions, and updating our Trello board accordingly.
	* Sprint 1 consisted of developing a flowchart describing the logic behind our project and set up the MatterMost server.
	* Sprint 2 consisted of setting up the AWS database and learning about incoming and outgoing webhooks using Mattermost.
	* Sprint 3 consisted of experimenting with SwaggerHub, learning more about OpenAPI (RESTful API), and learning more about outgoing webhooks.
	* Sprint 4 consisted of SwaggerHub researching and Flask server endpoint experiementation
	* Sprint 5 consisted of SwaggerHub blueprinting and codegen
	* Sprint 6 consisted of Endpoint functionality implementation and mock UDRI API implementation all locally


# Acknowledgements
We would like to thank UDRI for the oppurtunity to work on this project and Professor Phung for the continued support we have recieved throughout this release.


