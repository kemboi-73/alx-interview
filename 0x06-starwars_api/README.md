# Star Wars API Project

## Overview
This repository contains the implementation for the "Star Wars Characters" project, a short specialization within the curriculum. The project is designed to showcase your proficiency in interacting with an external API, specifically the Star Wars API, using JavaScript. The primary goal is to fetch and display information about Star Wars characters based on a provided movie ID.

## Project Details

- **Curriculum:** Short Specializations
- **Average Grade:** 73.99%
- **Project Weight:** 1
- **Instructor:** Alexa Orrico, Software Engineer at Holberton School
- **Project Dates:** Feb 12, 2024 - Feb 16, 2024

## Project Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- Mandatory README.md file at the root of the project folder
- Code should be semistandard compliant (Rules of Standard + semicolons on top, AirBnB style as reference)
- All files must be executable
- Length of files will be tested using `wc`
- Not allowed to use `var`

### Dependencies
- Install Node 10:
  ```bash
  $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```

- Install semistandard:
  ```bash
  $ sudo npm install semistandard --global
  ```

- Install request module:
  ```bash
  $ sudo npm install request --global
  $ export NODE_PATH=/usr/lib/node_modules
  ```

## Project Tasks

### 0. Star Wars Characters
- Write a script that prints all characters of a Star Wars movie.
- The first positional argument passed is the Movie ID.
- Display one character name per line in the same order as the "characters" list in the /films/ endpoint.
- Use the Star Wars API and the request module.

Example:
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## How to Run
1. Install dependencies: `sudo npm install semistandard --global` and `sudo npm install request --global`
2. Set the environment: `export NODE_PATH=/usr/lib/node_modules`
3. Run the script: `./0-starwars_characters.js <movie_id>`

## Repository Structure
- `0x06-starwars_api`: Main project directory
  - `0-starwars_characters.js`: Script for fetching and displaying Star Wars characters
  - `README.md`: Project documentation
  - ... (other project files)

