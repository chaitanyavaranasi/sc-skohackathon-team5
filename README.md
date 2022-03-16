Template
=======

# Details

**Project** : PROJECT ZNAYDIT
**Team Number** : 5 
**Team Name** : Anonymous  
**Demonstration Video** : _Insert link to demonstration video_

# Overview

Our application is named Proekt Znaydit; Ukrainian for Project Locate.  It's purpose is to power a "Craiglist-style" website where Ukrainians can quickly find (locate) critical goods and services (e.g. food, water, medicine, fuel, shelter, etc.) during the war with Russia.  It has a minimalist, simple, intuitive UI to allow non-technical individuals to easily search for, claim and retrieve goods over what are likely high latency, low bandwith internet connections.  The core idea is to quickly and easily connect people in need with those who are able to help them.


# Justification

While the war in Ukraine is 1000s of miles from many of us at MongoDB - although we do have co-workers who are much closer geographically to the conflict - there might seem to be little that we can do besides donate money and support our government's efforts to provide aid.  In times of armed conflict, civilian access to the most basic goods and services is among the first things to be disrupted.  We can leverage the power of the MongoDB Atlas platform - starting with it's multi-cloud capabilities - by regionally distributing data closest to those who need access to it.  Further we can leverage multiple components of the platform -Search, Realm, etc. to quickly provide multiple application requirements without multiple integrations to 3rd party products (which complicates and lengthens deployment time)

Overall this project demonstrates how quickly a basic humanitarian application could be created and deployed in times of crisis.  By leveraging the power of the ADP (MongoDB Atlas, Atlas Search, Realme, etc.) along with 3rd party providers (MapBox API) we can quickly apply technology to help solve a problem that unfolded very quickly and continues to expand rapidly.  So developer productivity is a big benefit. Time to deploy is crucial.   Other differentiators that aren't specficially showcased in a demo - but are nonethless critical - are the scalability (perhaps tens of thousands of users daily) and resiliency (multi-cloud, multi-region capabilities built into Atlas).

# Detailed Application Overview

Describe the architecture of your application and include a diagram.

MongoDB Atlas, Atlas Search (Ukraninan language analyzer), Realm, Aggregation Framework

The application has two interfaces (pages).  One page is a data entry form where those who have goods, services, etc. to offer others can post what they have and where they are located.  The geolocation of the poster is automatically captured and becomes part of the document.  The creation date is also timestamped and stored in the document.  A map is provided showing the location of both the requester and provider.  A communcation method between provider and requester (email, WhatsApp, SMS, etc.) is also captured and included.

Future versions of the application would include directions overlaid on the map


# Roles and Responsibilities

Paul Leury - architecture, documentation, data generation
Matt Richmond - architecture, UI, documentation, Realm
Chai Varanasi - MapBox, UI, aggregation
Stephen Hwang - UI, data modeling, Realm
Andrew Grzekowiak - data modeling, search, data generation
Albert Wong - aggregation, search

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
