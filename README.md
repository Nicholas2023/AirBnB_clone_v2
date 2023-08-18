# AirBnB Clone v2 :smile:

This is a Python project that aims to create an improved version of an AirBnB clone using MySQL as the database storage engine. The project involves implementing various features, improving the command-line interface, and utilizing SQLAlchemy for database interactions.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Contributors](#contributors)
- [License](#license)

## Description

This project involves enhancing an existing AirBnB clone codebase by implementing new features and utilizing MySQL as the database storage engine. It includes:

- Updating the command-line interface to allow object creation with given parameters.
- Implementing unittests to ensure code functionality and PEP8 compliance.
- Setting up development and test databases for MySQL.
- Integrating SQLAlchemy for improved database interactions.
- Enhancing the storage engine to support object deletion.
- Adding classes for States, Cities, Users, and Places with proper database mappings.

## Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- Pycodestyle 2.8.*
- MySQL database

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/AirBnB_clone_v2.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone_v2
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your MySQL database:
   - Run `setup_mysql_dev.sql` and `setup_mysql_test.sql` to create the development and test databases and users.

6. Configure environment variables:
   - Set the necessary environment variables for MySQL credentials and database names.

## Usage

1. Activate the virtual environment (if created):
   ```bash
   source venv/bin/activate
   ```

2. Run the command-line interface:
   ```bash
   ./console.py
   ```

3. Use various commands to interact with the AirBnB clone. For example:
   ```bash
   (hbnb) create State name="California"
   (hbnb) all State
   (hbnb) create City state_id="state_id_here" name="San_Francisco"
   ```

## Tests

To run the unittests and ensure code functionality and PEP8 compliance, use the following command:

```bash
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
```

## Contributors

- Original authors: [Faith Ampwera](https://github.com/Fayth7) and [Nicholas Otieno Odhiambo](https://github.com/Nicholas2023)

## License

This project is licensed under the [MIT License](LICENSE).
