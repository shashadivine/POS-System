# About
This project is a simple Point-of-Sale System for MSYS 42 (Business Applications Development III). This has front-end and back-end functionalities tied with database integrations. 

# Demo Information
1. Download the files or clone the repository to your local machine.
2. Set up a Python virtual environment by running python -m venv msys.
3. Activate virtual environment by running source msys/bin/activate for macOS, and msys\Scripts\activate for Windows.
4. Install Django by running pip install Django in your IDE terminal. (pip commands may differ based on your machine, e.g. pip3)
5. Navigate to manage.py by running cd m3_act1
6. Run the system through the command python manage.py runserver
7. The system supports CRUD (Create, Read, Update, Delete) for managing inventory items. You may add, view, update, and delete items in the system, and these will reflect in the database. You may also add items with SQL commands (e.g. use posdb; insert into posapp_item (item_name, item_price) values ('insulin', 400.00);)
