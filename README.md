```
  _______                   __       ______        __                       _______           __    __ __              __                        _______       __              __       __ 
 |   _   .--.--.-----.-----|  |_    |   _  \ .----|__.--.--.-----.-----.   |   _   .----.----|  |--|__|  |_.-----.----|  |_.--.--.----.-----.   |       .--.--|  |_.-----.----|__.---.-|  |
 |.  1___|  |  |  -__|     |   _|   |.  |   \|   _|  |  |  |  -__|     |   |.  1   |   _|  __|     |  |   _|  -__|  __|   _|  |  |   _|  -__|   |.|   | |  |  |   _|  _  |   _|  |  _  |  |
 |.  __)_ \___/|_____|__|__|____|   |.  |    |__| |__|\___/|_____|__|__|   |.  _   |__| |____|__|__|__|____|_____|____|____|_____|__| |_____|   `-|.  |-|_____|____|_____|__| |__|___._|__|
 |:  1   |                          |:  1    /                             |:  |   |                                                              |:  |                                    
 |::.. . |                          |::.. . /                              |::.|:. |                                                              |::.|                                    
 `-------'                          `------'                               `--- ---'                                                              `---'                                    
                                                                                                                                                                                           
```
## Table Of Contents
* [Overview](#overview)
* [Dependencies](#dependencies)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Getting Started](#getting-started)
    * [Service](#service)
    * [Client](#client)
    * [Docker](#docker)
* [Things I Learned](#things-i-learned)

## Overview
**Event Driven Architecture** is a software paradigm that uses events to trigger and communicate amongst services and applications. An "event" is defined as a change in the state of the data. EDA can be applied to workflows like placing an order on Uber Eats, or being admitted into a hospital. 
In this tutorial ["Event Driven Architecture](https://www.youtube.com/watch?v=NVvIpqmf_Xc) by Free Code Camp, it gave me a high level understanding on how to implement this software paradigm.

## Dependencies
* Redis
* Python v3.8
* NodeJS v14.19.3
* pip3

## Prerequisites
### Redis
**Redis** is an in-memory data structure  database that is often used as a key-value, cache or message broker. There are two ways to download **Redis**.
* **via HomeBrew (macOs only)**
```
$ brew install redis
```
* via **[Redis Official Website](https://redis.io/download/)**

Once downloads have been completed start the Redis database.
* **via HomeBrew**
```
$ brew services start redis
```
* **via redis-cli**
```
$ redis-cli
```

This by default should start the Redis database at `http://localhost:6379`. To view the contents within the Redis database download [Redis Insight](https://redis.com/redis-enterprise/redis-insight/).

### Python v3.8
1. Download [Python v3.8](https://www.python.org/downloads/release/python-380/)
2. Install virtualenv to setup Python v3.8 environment by running `pip3 install virutalenv`
3. Switch into `server/` directory
```
$ cd server/
```
4. Run `virtual -p PATH_TO_PYTHONv3.8 venv`, like the example below:
```
$ virtualenv -p /usr/local/opt/python@3.8/bin/python3.8 venv
```
5. Activate the newly created environment with `source venv/bin/activate`

### Node v14.19.3
1. Download [NodeJS v14.19.3](https://nodejs.org/en/download/)
2. Switch into `client/` directory
```
$ cd client/
```
3. Run `nvm use` to point to the correct node version.

## Installation
Due to the simplicity of this tutorial I decided to combine both the server and client into a mono-repository. The client side of the application will be placed in the `client/` directory and the server side of the application will be placed in the `server/` directory.

### Client
1. Switch into `client` directory.
```
$ cd client/
```
2. Run `npm install` to download library dependencies

### Server
1. Switch into `server` directory
```
$ cd server/
```
2. Run `pip3 install -r requirements.txt` to install library dependencies.


## Getting Started
### Service
### Client
### Docker
## Things I Learned



