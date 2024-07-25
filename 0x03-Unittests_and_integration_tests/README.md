# ALX Backend: Testing in Python

## Project Overview

This project focuses on writing unit tests in Python. It covers essential testing techniques and tools, including parameterized testing, mocking, and integration testing. The project is divided into several tasks, each aimed at testing different functions and classes to ensure their correctness and reliability.

## File Structure

├── client.py
├── fixtures.py
├── README.md
├── test_client.py
├── test_utils.py
└── utils.py


- `client.py`: Contains the `GithubOrgClient` class that interacts with the GitHub API.
- `fixtures.py`: Contains fixture data for integration testing.
- `test_client.py`: Contains unit and integration tests for the `GithubOrgClient` class.
- `test_utils.py`: Contains unit tests for utility functions in `utils.py`.
- `utils.py`: Contains utility functions used throughout the project.

## Setup

### Prerequisites

- Python 3.x
- `requests` library
- `parameterized` library

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/uwen-godwin/alx-backend-python.git
   cd alx-backend-python


## Install the required packages:
    
    pip install requests parameterized



## Usage

Running Tests
  To run all tests, execute the following command:
  ```sh
     python3 -m unittest discover
    
To run individual test files:
    ```sh
      python3 test_utils.py 
      python3 test_client.py

