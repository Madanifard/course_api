# 📘 Course Selling API

## 🧠 Project Overview

This project involves building a simple RESTful API for a **course selling platform** using **FastAPI** and **MongoDB**.

The system support:

- Instructors creating and managing their courses  
- Students browsing and enrolling in courses  
- Basic CRUD operations for all core entities

> 🛠️ No authentication, tests, or CI/CD are required. Keep it clean and minimal.

----

## 📦 Folder Structure

```bash
course_api/
├─ crud/
│  ├─ course.py
│  ├─ enrollment.py
│  ├─ instructor.py
│  └─ student.py
├─ models/
│  ├─ course.py
│  ├─ enrollment.py
│  ├─ instructor.py
│  └─ student.py
├─ routers/
│  ├─ course.py
│  ├─ enrollment.py
│  ├─ instructor.py
│  └─ student.py
├─ .env.example
├─ .gitignore
├─ config.py
├─ database.py
├─ main.py
├─ readme.md
└─ requirements.txt
```

- `crud`: To create operations 3 on data in Mango based on each collection
- `models`: Using pydentics to model inputs and outputs based onUsing pydentics to model inputs and outputs based on
- `routers`: To implement the logic and logics that each section needs to implement
- `.env.example`: Sample file definition for initial values ​​for variables used throughout the project
- `config.py`: Inside this file are the values ​​placed in `.env`
- `database.py`: Settings related to creating collections and connectors have been implemented with MangDB.
- `main.py`: The starting point of the project is
- `requirements.txt`: List of packages used in the project
- `.gitignore`: Delete a set of files that do not need to be moved to Git


## 📦 run project

The following steps are required to implement the project:The following steps are required to implement the project:

- create .env

```bash
$ cp .env.example .env
```
After creating the file, we need to copy the desired values ​​into it.

- install requiremnt

```bash
$ pip install -r requirements.txt

```

- run project

```bash
$ fastapi dev main.py
```


**Note that there is no need to create collections in the database to run the program - they are created when the program is first run.**

