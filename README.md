# Chift test api

Brief description of what this project does and who it's for. Provide an overview of the project and any relevant background information.

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

#### 1. Virtual Environment Setup

First, clone the project repository and navigate to the project directory:

```bash
git clone https://your-repository-url.git
cd your-project-directory
Then, create and activate a Python virtual environment:

bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
2. Install Dependencies
With the virtual environment activated, install the required dependencies:

bash
pip install -r requirements.txt
3. Environment Configuration

Create a .env file in the project root directory. Add your environment variables like so:

makefile
DATABASE_URL="your_database_url"
ODOO_URL="your_odoo_url"
ODOO_DB="your_odoo_db_name"
ODOO_USERNAME="your_odoo_username"
ODOO_PASSWORD="your_odoo_password"
Replace the placeholders with your actual data.

4. Cron Job Setup
To set up a cron job that runs the script every 30 minutes, open your crontab file:

bash
crontab -e
And add the following line, making sure to replace /path/to/your/script with the actual path to cron_service.py:

cron
*/30 * * * * /usr/bin/python3 /path/to/your/script/cron_service.py
Running the Server
To start the FastAPI server:

bash
uvicorn main:app --reload
```
