<!--
*** To avoid retyping too much info. Do a search and replace for the following:
*** BSAkash, AiBot, twitter_handle, email
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/BSAkash/ChatBot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h2 align="center">AiBot</h2>

  <p align="center">
    Chatbot to help you in your course selection
    <br />
    <br />
    <a href="https://rikilg.pythonanywhere.com/">View Demo</a>
  </p>
</p>


## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
- [Making Changes](#making-changes)
- [Performing requests to API](#performing-requests-to-api)
- [Project Layout](#project-layout)
- [Project Contributors](#project-contributors)
- [References](#references)


## About The Project

The aim of this assignment is to create a messenger bot which can provide intelligent dialog 
conversations with the user,similar to bots like ELIZA or Bot. The bot uses a knowledge base 
built using conversations stored in aiml files.

The main goal of this chatbot is to help students decide on which courses they should take based 
on their intrests and recent trends in the market. It also uses a corpus containing information 
about his current university to provide more relavent responses based on which classes he attends 
and which professor he likes.

This project is written in python. Any interactions performed with the user are stored in flat 
file database using sqlite. The bot is designed to interact with other online services and api's.
The front-end for this bot is an android app(flutter app added later) which interacts with a 
backend (a flask application which can be hosted on any cloud platform) using RESTful services.

You can interact with the bot hosted [here](https://rikilg.pythonanywhere.com)


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This project requires the following:
 - [python](https://www.python.org/) (version >= 3.7)
 - [sqlite3](https://www.sqlite.org/) (command-line utility to edit the database - optional)

### Dependencies

This is an example list of dependencies present/used in the project
 - [flask](https://palletsprojects.com/p/flask/)
 - [sqlite3](https://docs.python.org/3/library/sqlite3.html)
 - [python-aiml](https://pypi.org/project/python-aiml/)

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/BSAkash/ChatBot.git
cd AiBot
```
2. Install required python packages
```sh
pip install -r requirements.txt
```
3. Run the development server (or see next step to run locally)
```sh
python flask_app.py
```
3. Run the bot locally without any server
```sh
python conversation.py 
```

## Making Changes

Changes can be done to `Backend/databases/corpus.db` according to the courses 
and the faculty available which will be reflected by the bot. This can be done 
by running the `sqlite3 Backend/databases/corpus.db` command or by using any other GUI 
sqlite database editor of your choice.


## Performing requests to API

Bot responses can be obtained by performin a POST request to the API at 
rikilg.pythonanywhere.com/api/
```json
// Query format
{
  "query": "<user query here>"
}
```

```json
// Response format
{
  "response": "<reply from the bot>",
  "mode": "reply" 
  // currently mode is set to reply but can change by reply type for example audio or video by improving the bot in future.
}
```


## Project Layout

Folder structure:
```sh
AiBot
  ├── AndroidApp  # A Basic android app to talk to bot on server
  ├── FlutterApp  # A Better flutter app to talk to bot on server
  ├── Backend/src # Source code of the bot deployed on server
  │   ├── aiml    # holds all aiml files which serve as knowledgebase of the bot
  │   │   ├── conversation.aiml
  │   │   ├── dictionary.aiml
  │   │   ├── quote.aiml
  │   │   └── (other alice aiml)
  │   ├── apis    # python modules to interact with online apis
  │   │   ├── dictionary.py
  │   │   └── quotes.py
  │   ├── templates   # files served by the flask server for online bot access
  │   │   ├── main_page.css
  │   │   ├── main_page.js
  │   │   └── main_page.html
  │   ├── databases       # folder to store database files 
  │   ├── conversation.py # main bot file which abstracts the underlying aiml interaction
  │   ├── database.py     # python module to interact with the stored database
  │   ├── flask_app.py    # main file used to run flask server
  │   └── learningFileList.aiml # main aiml file which loads all other aiml files
  ├── README.md         # this README file
  └── requirements.txt  # contains of all the required python packages
```


## Project Contributors

 - Rikil Gajarla - 2017A7PS0202H
 - Naga Sai Bharath - 2017A7PS0209H
 - Akash Bonagiri - 2017AAPS0455H

Project Link: [https://github.com/BSAkash/ChatBot](https://github.com/BSAkash/ChatBot)


## References

 - [alice](https://github.com/mz026/aiml-en-us-foundation-alice.v1-0)
 - [aiml - reference](http://callmom.pandorabots.com/static/reference/)
 - [aiml - a brief tutorial](https://arxiv.org/abs/1307.3091)
 - [aiml - tutorialspoint](https://www.tutorialspoint.com/aiml/aiml_introduction.htm)
 - [aiml - example files](https://github.com/pandorabots/Free-AIML)
