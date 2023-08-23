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

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ init _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>

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
   - Set necessary environment variables for MySQL credentials and database names.

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

To run the unittests & ensure code functionality and PEP8 compliance, use the following command:

```bash
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
```

## Contributors

- Original authors: [Faith Ampwera](https://github.com/Fayth7) and [Nicholas Otieno Odhiambo](https://github.com/Nicholas2023)

## License

This project is licensed under [MIT License](LICENSE).
