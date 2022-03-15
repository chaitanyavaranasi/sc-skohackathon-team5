Template
=======

# Details

**Project** : _insert project title here_  
**Team Number** : _insert team number here_  
**Team Name** : _insert team name here_  
**Demonstration Video** : _Insert link to demonstration video_

# Overview

_Insert Executive Overview of your application/demonstration_

# Justification

_Please explain why you decided to build the application/demonstration for this project. What inspired you? What problems does it solve or how will it make Presales activities easier?_
_What MongoDB competitive differentiators (developer productivity, resiliency, scalability, etc.) does this demonstration showcase?_

# Detailed Application Overview

_Describe the architecture of your application and include a diagram._
_List all the MongoDB components/products used in your demonstration._
_Describe what you application does and how it works_


# Roles and Responsibilities

_List all the team members and summarize the contributions each member made to this project_

# Demonstration Script

_Demonstration script (or link to script) goes here_

_The demonstration script should provide all the information required for another MongoDB SA to deliver your demonstration to a prospect. This should include:_


##Setup
* In a new terminal/shell from the base folder of this proof, run the following command to generate, partly templated, partly randomly generated JSON documents into the database collection _zynadit.items_
  ```bash
   mgeneratejs items_template.json -n 1000 | mongoimport --uri "mongodb+srv://<userId>:<password>@znaydit.padcu.mongodb.net/zynadit" --collection items
  ```
* In a new terminal/shell from the base folder of this proof, run the following command to generate, partly templated, partly randomly generated JSON documents into the database collection _zynadit.accounts_
  ```bash
   mgeneratejs accounts_template.json -n 100 | mongoimport --uri "mongodb+srv://<userId>:<password>@znaydit.padcu.mongodb.net/zynadit" --collection accounts
  ```


##Todo
* _step by step instructions on how to give the demonstration_
* _key points to emphasize at each point in the demonstration_
* _any tear down steps required to reset the demonstration so it is ready for the next time_
  hackathonReadme.md
  Displaying hackathonReadme.md.