Getting Started
These instructions will guide you through setting up and running the project on your local machine for development and testing purposes.

Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x installed on your system
pip (Python package installer), which typically comes with Python
Setting Up the Development Environment
Create a Python Virtual Environment

Navigate to your project directory in the terminal and run the following command to create a virtual environment named venv:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On macOS/Linux:

bash
Copy code
source venv/bin/activate
On Windows:

cmd
Copy code
.\venv\Scripts\activate
Install Required Packages

With the virtual environment activated, install the required Python packages using pip:

bash
Copy code
pip install -r requirements.txt
Make sure you have a requirements.txt file in your project directory containing all the necessary packages.

Set Up Environment Variables

Create a .env file in your project root directory and add your configuration variables. For example:

plaintext
Copy code
DATABASE_URL=your_database_connection_url
ODOO_URL=your_odoo_url
ODOO_DB=your_odoo_db_name
ODOO_USERNAME=your_odoo_username
ODOO_PASSWORD=your_odoo_password
Replace the placeholders with your actual data.

Configure a Cron Job

Set up a cron job to run the script periodically. Open the crontab for editing:

bash
Copy code
crontab -e
Add the following line to run your script every 30 minutes. Make sure to replace /path/to/your/script with the actual path to cron_service.py:

cron
Copy code
_/30 _ \* \* \* /usr/bin/python3 /path/to/your/script/cron_service.py
Launch the Server

Run the following command to start the FastAPI server:

bash
Copy code
uvicorn main:app --reload
