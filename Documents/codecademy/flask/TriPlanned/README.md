# TriPlanned
A basic flask website where users can post cities that they plan to visit.

## To run on your computer

**1. Download the code**

**2. Navigate to the TriPlanned directory in the terminal**

`cd /path/to/TriPlanned`

**3. Install the requirements:**

`pip install -r requirements.txt`

**4. Initialize the database:**

Start a python console in your terminal:

`python` or `python3`

Then in the python console, run:

`from app import db`

`db.create_all()`

`exit()`

**5. Start the flask server:**

From the terminal, in the TriPlanned folder:

`flask run`  

Then visit the link that you're given in the terminal.

