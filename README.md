<a href="https://fastapi.tiangolo.com/"><img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"></a>
<a href="https://www.postgresql.org/"><img alt="Postgres" src="https://img.shields.io/badge/Postgres-316192?style=for-the-badge&logo=postgresql&logoColor=white"></a>
<a href="https://redis.io/"><img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" alt="redis" > </a>
<a href="https://www.sqlalchemy.org/"><img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/></a>
<a href="https://www.docker.com/"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="docker" > </a>

# Tracking attendance

Our Tracking Attendance system is designed to streamline meeting check-ins and ensure fairness. It provides an efficient way for participants to mark their attendance while actively preventing common issues such as proxy attendance (checking in on behalf of others) and remote check-ins outside the meeting location. This helps organizations maintain accurate records, reduce fraud, and improve accountability in every session.


## Table of contents
* ✨[Features](#features)
* 🛠️[Prerequisites](#prerequisites)
* 🚀[Getting Started](#getting-started)
* 🔧[Configure Environment Variables](#configure-environment-variables)
* 🔗[References](#references)
* 📧[Contact](#contact)

## ✨Features

#### 1. Admin Management Dashboard  
- **Admin Account**: Centralized interface for creating and managing meetings, attendance sessions, and participants.  
- **Role-Based Login**: Users can log in with roles as either administrators or participants.  

#### 2. Attendance Tracking  
- **Accurate Logging**: Records attendance for each participant in real time.  
- **Fraud Prevention**: Prevents proxy attendance (check-ins on behalf of others) and remote check-ins outside the meeting location.  

#### 3. Reporting & Export  
- **Excel Export**: Generate and download attendance reports in Excel format for easy record-keeping and sharing.  
- **Detailed Statistics**: Provides summary statistics of participant attendance across sessions.  

#### 4. User Management  
- **Participant Profiles**: Store and manage participant information in a secure database.  
- **Account Suspension**: Administrators can lock participant accounts if misuse or fraud is detected.  

#### 5. Notifications  
- **Real-Time Alerts**: Notify participants about upcoming meetings or attendance confirmation.  
- **Fraud Alerts**: Notify administrators if suspicious activity is detected (e.g., multiple check-ins from one device).  

## 🛠️Prerequisites
What you need to run the project:  

- [Python 3.10+](https://www.python.org/downloads/) – Required to run the FastAPI backend and related dependencies.  
- [PostgreSQL](https://www.postgresql.org/download/) – Database engine used to store attendance and user data.  

## 🚀Getting Started
After installing Python, run the following commands to start experiencing this project:

```shell
# clone the project
git clone https://github.com/mpc-ou/tracking-attendance.git

# create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run database migrations
alembic upgrade head

# run server
uvicorn main:app --reload
```
## 🔧Configure Environment Variables

Create a `.env` file in the root directory based on `.example.env` and update the values as needed.

## 🔗References
Here are some helpful resources and references for further information:
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [React Documentation](https://react.dev/)
- [Docker Documentation](https://docs.docker.com/)


## 📧Contact
Don't hesitate to contact me if you have any confusion or questions
<a href="mailto:it.mpclub@ou.edu.vn" target="_blank">
  <img align="center" src="https://img.icons8.com/color/48/000000/gmail--v2.png" alt="it.mpclub@ou.edu.vn" height="30" width="40">
</a>
