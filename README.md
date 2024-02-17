# Job Portal Project

## Description

This is a job portal project developed using Django. In this application:

- Users can create an account and choose to be either an employer or a job applicant.
- Users can log in to their account.

If a user chooses to be an employer, they can:
- Create, update, and delete job listings.
- View submitted applications for their job listings.
- Reach out to job applicants

If a user chooses to be a job applicant, they can:
- View all of the job listings and details.
- Apply for jobs.
- Withdraw their job application

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gerardo0915/JobPortalProject.git
    ```
2. Navigate to the project directory:
    ```bash
    cd JobPortalProject
    ```
3. Create a virtual environment:

    On Unix or MacOS, run:
    ```bash
    python3 -m venv env
    ```
    On Windows, run (use `python` or `py` depending on your installation):
    ```bash
    python -m venv env
    ```
    or
    ```bash
    py -m venv env
    ```
4. Activate the virtual environment:

    On Unix or MacOS, run:
    ```bash
    source env/bin/activate
    ```
    On Windows, run:
    ```bash
    .\env\Scripts\activate
    ```
5. Install the required dependencies:

    On Unix or MacOS, run:
    ```bash
    pip install -r requirements.txt
    ```
    On Windows, run (use `python -m pip` or `py -m pip` depending on your installation):
    ```bash
    python -m pip install -r requirements.txt
    ```
    or
    ```bash
    py -m pip install -r requirements.txt
    ```

## Running the Project

1. Apply the migrations:

    On Unix or MacOS, run:
    ```bash
    python3 manage.py migrate
    ```
    On Windows, run (use `python` or `py` depending on your installation):
    ```bash
    python manage.py migrate
    ```
    or
    ```bash
    py manage.py migrate
    ```
2. Run the server:

    On Unix or MacOS, run:
    ```bash
    python3 manage.py runserver
    ```
    On Windows, run (use `python` or `py` depending on your installation):
    ```bash
    python manage.py runserver
    ```
    or
    ```bash
    py manage.py runserver
    ```
3. Open your web browser and navigate to the server shown (typically http://127.0.0.1:8000/).
 
