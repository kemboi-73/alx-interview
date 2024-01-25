# Log Parsing Script

## Overview

This repository contains a Python script (`0-stats.py`) designed to parse log files in a specific format and compute various metrics based on the input. The script reads stdin line by line, processes the log entries, and outputs statistics after every 10 lines or a keyboard interruption (CTRL + C).

## Short Specialization Information

- **Name:** Log Parsing
- **Average Score:** 65.39%
- **Instructor:** Alexa Orrico, Software Engineer at Holberton School
- **Weight:** 1

## Project Details

- **Project Start:** Jan 22, 2024 6:00 AM
- **Project Deadline:** Jan 26, 2024 6:00 AM
- **Checker Release:** Jan 23, 2024 6:00 AM
- **Auto Review:** An auto review will be launched at the deadline

## Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Interpretation/Compilation Environment:** Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Endings:** All files should end with a new line
- **Shebang:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** A `README.md` file at the root of the project folder is mandatory
- **PEP 8 Style:** Code should adhere to PEP 8 style (version 1.7.x)
- **File Execution:** All files must be executable
- **Length of Files:** File length will be tested using `wc`

## Tasks

### Log Parsing (Task 0)

- **Description:** Write a script that reads stdin line by line and computes metrics based on the given input format.
  
- **Input Format:**
  ```
  <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
  ```
  (If the format is not this one, the line must be skipped)

- **Metrics to Compute:**
  - Total file size
  - Number of lines by status code (possible status codes: 200, 301, 400, 401, 403, 404, 405, 500)

- **Output Format:**
  ```
  Total file size: File size: <total size>
  <status code>: <number>
  ```

- **Additional Information:**
  - After every 10 lines and/or a keyboard interruption (CTRL + C), print the specified statistics from the beginning.

## Sample Usage

```bash
./0-generator.py | ./0-stats.py
```

## Sample Output

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3

File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3

File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4

...

^C
File size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Copyright

Copyright © 2024 ALX, All rights reserved.
