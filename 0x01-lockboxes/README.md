# 0x01. Lockboxes

## Algorithm

### Overview
This project involves implementing an algorithm in Python to solve a problem related to lockboxes. The goal is to determine if all the boxes can be opened, where each box may contain keys to other boxes.

### Project Information
- **Author:** Carrie Ybay
- **Role:** Software Engineer at Holberton School
- **Weight:** 1
- **Start Date:** Jan 8, 2024, 6:00 AM
- **End Date:** Jan 12, 2024, 6:00 AM
- **Checker Release Date:** Jan 9, 2024, 6:00 AM
- **Auto Review Deadline:** Deadline will trigger an auto review.

## Requirements

### General
- **Allowed Editors:** vi, vim, emacs
- **Interpreter/Compiler:** Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Format:** All files should end with a new line
- **First Line:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** A README.md file at the root of the project folder is mandatory
- **Documentation:** Code should be documented
- **Style:** Code should use the PEP 8 style (version 1.7.x)
- **Execution:** All files must be executable

## Tasks

### 0. Lockboxes (mandatory)

#### Description
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to other boxes.

Write a method that determines if all the boxes can be opened.

#### Prototype
```python
def canUnlockAll(boxes)
```

- `boxes` is a list of lists.

A key with the same number as a box opens that box. You can assume all keys will be positive integers. There can be keys that do not have boxes. The first box `boxes[0]` is unlocked.

#### Returns
Return `True` if all boxes can be opened, else return `False`.

### Usage Example
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Execution
```bash
$ ./main_0.py
True
True
False
```

## Conclusion
This project aims to implement an efficient algorithm to solve the lockboxes problem in Python. Follow the specified requirements, guidelines, and examples to successfully complete the task.
