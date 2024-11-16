# Spy Cat Agency Management System

This is a RESTful API for managing spy cats, missions, and targets for the **Spy Cat Agency (SCA)**. The application allows managing spy cats, creating missions, assigning cats to missions, and handling target data.

## Features

- **Spy Cats**
  - Create, update, and delete spy cats
  - Each cat has a name, years of experience, breed, and salary
  - Assign a cat to a mission
  
- **Missions**
  - Create, update, and delete missions
  - A mission can have multiple targets
  - Mark targets as complete
  - Assign a cat to a mission (one cat per mission)

- **Targets**
  - Each mission contains targets to track
  - Update notes for targets, mark them as complete

## Setup

### Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite or PostgreSQL database (SQLite by default)

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/spy-cat-agency.git
cd spy-cat-agency
```

**2. Create a virtual environment:**

```bash
python -m venv venv```
Activate the virtual environment:
```

*On Windows:*
```bash
.\venv\Scripts\activate
```

*On macOS/Linux:*
```
source venv/bin/activate
```

**Install the dependencies:**
```
pip install -r requirements.txt
```

**Run the FastAPI server:**
```
uvicorn main:app --reload
```

**The API should now be running at http://127.0.0.1:8000.**



### API Endpoints

**POST** /cats/: *Create a new cat.*

**GET** /cats/{id}/: *Get details of a cat by ID.*

**PUT** /cats/{id}/: *Update cat information (e.g., salary).*

**DELETE** /cats/{id}/: *Delete a cat.*

**POST** /missions/: *Create a new mission along with targets.*

**GET** /missions/{id}/: *Get mission details by ID.*

**PUT** /missions/{mission_id}/assign-cat/{cat_id}: *Assign a cat to a mission.8

**DELETE** /missions/{id}/: *Delete a mission.*

# Database Models

### Cat

**id (int): Unique identifier**\
**name (str): Name of the cat**\
**years_of_experience (int): Experience in years**\
**breed (str): Breed of the cat**\
**salary (float): Salary of the cat**

### Mission

**id (int): Unique identifier**\
**is_completed (bool): Status of the mission**\
**cat_id (int, optional): ID of the cat assigned to the mission**\


### Target

**id (int): Unique identifier**\
**name (str): Name of the target**\
**country (str): Country of the target**\
**notes (str): Notes about the target**\
**is_complete (bool): Target completion status**\


# Testing
You can test the endpoints using tools like Postman or cURL. Alternatively, you can use Invoke-RestMethod (PowerShell) or requests (Python) for API testing.

## Notes
The cat's breed is validated using TheCatAPI.
A mission can have multiple targets, and once all targets are marked as complete, the mission is also marked as complete.
Once a target is marked as complete, the notes cannot be updated.

