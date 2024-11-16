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

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/spy-cat-agency.git
   cd spy-cat-agency
   
2. Create a virtual environment:
  ```python3
   python -m venv venv
   
3. Activate the virtual environment:

  On Windows:
    ```bash
    .\venv\Scripts\activate

    On macOS/Linux:
    ```bash
    source venv/bin/activate

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt

5. Run the FastAPI server:
  ```bash
  uvicorn main:app --reload
