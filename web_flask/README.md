# AirBnB Clone - Flask Web Application :smile:

This project is a simple AirBnB clone implemented using Flask, a popular Python web framework. It provides several routes with different functionalities, including displaying text, handling dynamic URLs, and rendering HTML templates.

## Project Structure

The project consists of Python scripts for the Flask application and a folder for HTML templates. Here's an overview of the project structure:

- `0-hello_route.py`: Implements a simple "Hello HBNB!" route.
- `1-hbnb_route.py`: Adds an additional route for "HBNB."
- `2-c_route.py`: Implements a dynamic route that takes a variable and displays it.
- `3-python_route.py`: Extends the application to handle dynamic routes with optional parameters.
- `4-number_route.py`: Adds a route that validates and displays if a variable is a number.
- `5-number_template.py`: Introduces rendering HTML templates based on a dynamic variable.
- `templates/`: A folder containing HTML templates used in the Flask application.
  - `5-number.html`: A template for displaying a number.
  - `6-number_odd_or_even.html`: A template to determine if a number is odd or even.

## Running the Application

To run the Flask web application, follow these steps:

1. Ensure you have Python and Flask installed in your environment.
2. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/Nicholas2023/airbnb-clone-flask.git
   ```

3. Navigate to the project directory.

   ```bash
   cd airbnb-clone-flask
   ```

4. Run the desired Python script for the specific task you want to test. For example, to run the "Number Odd/Even" task:

   ```bash
   python 6-number_odd_or_even.py
   ```

5. The Flask development server will start, and you can access the application in your web browser at `http://localhost:5000`.

## Available Routes

- `/`: Displays "Hello HBNB!".
- `/hbnb`: Displays "HBNB".
- `/c/<text>`: Takes a dynamic `text` parameter and displays "C " followed by the sanitized text.
- `/python/` and `/python/<text>`: Handles Python-related routes and displays "Python " followed by the sanitized text.
- `/number/<int:n>`: Validates if `n` is a number and displays the result.
- `/number_template/<int:n>`: Renders an HTML template (`5-number.html`) with the number.
- `/number_odd_or_even/<int:n>`: Renders an HTML template (`6-number_odd_or_even.html`) to determine if the number is odd or even.

Feel free to explore and test each route to see how the Flask application works.

Happy coding!
