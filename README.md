# E-Cafe Project

## Overview
The E-Cafe project is a smart canteen management system that utilizes RFID technology for authentication and Arduino for hardware integration. The backend is built using Django, allowing for easy management of users, inventory, and transactions. This system aims to streamline the process of purchasing items in a canteen by automating the check-out process and providing a smooth user experience.

## Features
- **RFID Authentication:** Users can authenticate using RFID cards.
- **Canteen Inventory Management:** Items are managed in a database with their stock and price details.
- **Transaction History:** Keeps a record of all transactions.
- **Django Backend:** A robust backend to manage user accounts, transactions, and inventory.
- **Arduino Integration:** Arduino is used to manage hardware components, including RFID scanners and display systems.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript (for displaying user interface)
- **Backend:** Django (Python)
- **Database:** SQLite (or other database systems)
- **Hardware:** Arduino, RFID module, and other electronic components

## Installation

### Prerequisites:
- Python 3.x
- Django
- SQLite (or other database systems)
- Arduino IDE
- Required Arduino libraries
- RFID module and Arduino hardware setup

### Steps:
1. Clone the repository:
   ```bash
    git clone https://github.com/Sangamsilwal/RFIDbased_Payment_gateway.git
    cd e-cafe-project

    # Set up the virtual environment (recommended)
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    # Install required Python packages
    pip install -r requirements.txt

    # Set up the database
    python manage.py migrate

    # Run the Django server
    python manage.py runserver

  ```

