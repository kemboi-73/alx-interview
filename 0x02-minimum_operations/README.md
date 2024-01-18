# Minimum Operations - Overview

This repository contains a Python project focusing on solving the "Minimum Operations" problem. The project is part of the Short Specialization Curriculum and is designed to enhance algorithmic and Python programming skills. Below is an overview of the project details:

## Curriculum Overview

### 0x02. Minimum Operations

- **Specialization**: Short Specializations
- **Average Completion**: 28.34%

#### Project Details

- **Name**: Minimum Operations
- **Type**: Algorithm
- **Language**: Python
- **Author**: Carrie Ybay, Software Engineer at Holberton School
- **Weight**: 1

#### Project Schedule

- **Start Date**: Jan 15, 2024 6:00 AM
- **End Date**: Jan 19, 2024 6:00 AM
- **Checker Release Date**: Jan 16, 2024 6:00 AM
- **Auto Review Launch**: At the deadline

#### Requirements

##### General

- Allowed editors: vi, vim, emacs
- Files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files end with a new line
- The first line of all files is `#!/usr/bin/python3`
- Mandatory `README.md` file at the root of the project folder
- Code documentation and adherence to PEP 8 style (version 1.7.x)
- All files must be executable

#### Tasks

##### 0. Minimum Operations

- **Description**: In a text file, there is a single character H. The text editor can execute only two operations: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
- **Prototype**: `def minOperations(n)`
- **Returns**: An integer
- **Conditions**:
  - If n is impossible to achieve, return 0

##### Example

```python
n = 9
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6
```

#### Testing

```python
# Testing the provided main file
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```
