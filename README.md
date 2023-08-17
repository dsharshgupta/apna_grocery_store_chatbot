# Apna Grocery FastAPI Backend

This repository contains the backend code for the Apna Grocery application using FastAPI. The backend is responsible for handling user requests and interacting with the database to provide information about available categories and products.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Intents](#intents)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Apna Grocery FastAPI Backend is designed to provide responses to user queries related to available categories and products. It utilizes the FastAPI framework and interacts with a MySQL database to fetch and present relevant information.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Update the database connection URL in the `DATABASE_URL` variable within the `main.py` file.
4. Run the FastAPI server using `uvicorn main:app --host 0.0.0.0 --port 8000`.

## Usage

Once the server is up and running, you can send POST requests to the appropriate endpoint to get responses related to available categories and products.

## Endpoints

- `POST /`: This endpoint is used for Dialogflow fulfillment. It processes user queries and responds with relevant information about available categories and products.

## Intents

The following intents are supported:

- **Welcome Intent**: Greet the user and ask for their needs.

- **Fallback Intent**: Apologize for any confusion and guide the user to available options.

- **Available Categories Intent**: Provide a list of available categories from the database.

- **Available Products Intent**: Provide a list of available products and their prices from the database.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
