# Airbnb Clone Project

This is a simplified Airbnb clone project for managing property rentals. The project includes a console-based command-line interface (CLI) to interact with the system.

## Getting Started

These instructions will help you set up and run the Airbnb clone on your local machine.

### Prerequisites

- Python 3.x
- [Pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hellena254/AirBnB_clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd airBnB_clone
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the console:

    ```bash
    python console.py
    ```

2. You'll now be in the (hbnb) prompt. Here, you can interact with the Airbnb clone using various commands.

### Available Commands

- **create**: Create a new instance of a specified class.
    ```bash
    create BaseModel
    ```

- **show**: Display the string representation of an instance based on the class name and ID.
    ```bash
    show BaseModel 1234-5678
    ```

- **destroy**: Delete an instance based on the class name and ID.
    ```bash
    destroy BaseModel 1234-5678
    ```

- **all**: Display string representations of all instances or instances of a specific class.
    ```bash
    all
    all BaseModel
    ```

- **update**: Update an instance based on the class name and ID by adding or updating an attribute.
    ```bash
    update BaseModel 1234-5678 email "newemail@example.com"
    ```

3. To exit the console, use either `quit` or `Ctrl + D`.

## Project Structure

The project follows the structure below:

- **models**: Contains the various classes representing different entities (BaseModel, User, Place, etc.).
- **models/engine**: Includes the FileStorage class responsible for serialization and deserialization.
- **tests**: Holds the unit tests for the classes.

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover tests
```

## Acknowledgments

- This project is part of an educational exercise and is inspired by the Airbnb platform.

