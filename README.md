# crudiDB
A generalized interface to a relational database, designed to be highly customizable and easy to use. This project provides a boilerplate codebase using FastAPI and SQLAlchemy, allowing you to quickly set up a RESTful API for your database.

## Features
* FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
* SQLAlchemy: The Python SQL toolkit and Object Relational Mapper.
* Pydantic: Data validation and settings management using Python type annotations.
* Modular Structure: Easily extendable and maintainable project structure.
* Lifespan Event Handlers: Modern approach to handle application startup and shutdown events.
* Getting Started
### Prerequisites
* Python 3.7+
* SQLite (for prototyping)
* Graphviz (for generating ERD diagrams)

## Getting Started

### Setup python environment
```python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt


# Running the server
uvicorn server_app.main:app --reload
```
