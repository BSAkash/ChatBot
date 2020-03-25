<!--
*** To avoid retyping too much info. Do a search and replace for the following:
*** RikilG, AiBot-Backend, twitter_handle, email
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/RikilG/AiBot-Backend">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h2 align="center">AiBot - Backend</h2>

  <p align="center">
    This repository holds the code hosted on backend for our AI bot project. 
    <!-- <br />
    <br />
    <a href="https://github.com/RikilG/AiBot-Backend">View Demo</a> -->
  </p>
</p>


## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
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
The front-end for this bot is an android app which interacts with a backend (a flask application which 
can be hosted on any cloud platform) using RESTful services.

<!-- If you have hosted your project (ex: Heroku) l -->
Project backend hosted [here](https://rikilg.pythonanywhere.com)


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This project requires the following:
 - [python3](https://www.python.org/)

### Dependencies

This is an example list of dependencies present/used in the project
 - [flask](https://palletsprojects.com/p/flask/)
 - [sqlite3](https://docs.python.org/3/library/sqlite3.html)
 - [aiml](https://pypi.org/project/aiml/)

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/RikilG/AiBot-Backend.git
cd AiBot-Backend
```
2. Install required python packages
```sh
pip install -r requirements.txt
```
3. Run the development server
```sh
python flask_app.py
```
3. (or) Run the bot locally without any server
```sh
python conversation.py 
```


## Project Layout

Folder structure:
```sh
AiBot-Backend
  ├── aiml        # holds all aiml files which serve as knowledgebase of the bot
  │   ├── conversation.aiml
  │   ├── dictionary.aiml
  │   └── quote.aiml
  ├── apis        # python modules to interact with online apis
  │   ├── dictionary.py
  │   └── quotes.py
  ├── templates   # files served by the flask server 
  │   └── main_page.html
  ├── conversation.py # main bot file which abstracts the underlying aiml interaction
  ├── database.py # python module to interact with the stored database
  ├── database.db # database which stores user interactions
  ├── flask_app.py # main file used to run flask server
  ├── learningFileList.aiml # main aiml file which loads all other aiml files
  ├── README.md   # this README file
  └── requirements.txt # contains of all the required python packages
```


## Project Contributors

 - Rikil Gajarla - 2017A7PS0202H
 - Naga Sai Bharath - 2017A7PS02XXH
 - Akash Bonagiri - 2017AAPS0455H

Project Link: [https://github.com/RikilG/AiBot-Backend](https://github.com/RikilG/AiBot-Backend)


## References

 - [alice](https://github.com/mz026/aiml-en-us-foundation-alice.v1-0)
 - [aiml - a brief tutorial](https://arxiv.org/abs/1307.3091)
 - [aiml - tutorialspoint](https://www.tutorialspoint.com/aiml/aiml_introduction.htm)