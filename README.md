# Adoptly App

Adoptly is a web application built with Django that helps users find and adopt pets. This project aims to streamline the adoption process by providing a user-friendly interface and comprehensive pet information.

## Features

- User authentication and authorization
- Pet listing and search functionality
- Detailed pet profiles
- Adoption request management

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/adoptly-app.git
    cd adoptly-app
    ```

2. Create and activate a virtual environment:
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Register for an account or log in if you already have one
- Browse available pets and submit adoption requests

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.