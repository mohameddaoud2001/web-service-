# TBS REST API Project

## Overview
This project implements a REST API for managing `Specializations` and their associated `Course Items`. The API uses Flask, Flask-Smorest for API management, and Marshmallow for data validation.

## Features
- Manage `Specializations` and `Course Items`.
- Swagger-UI for API documentation.
- Dockerized for easy deployment.

---

## Prerequisites
- Python 3.10+
- Docker and Docker Compose

---

## Installation

### Clone the Repository
```bash
# Clone this repository
git clone <repository-url>
cd <repository-folder>
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application Locally
```bash
python app.py
```
Access Swagger-UI at: [http://localhost:5000/swagger-ui](http://localhost:5000/swagger-ui)

### Run the Application with Docker
```bash
# Build and run the application
docker-compose up --build
```

The app will be available at [http://localhost:5000](http://localhost:5000).

---

## Folder Structure
```
project/
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── models/                 # Database models
│   ├── __init__.py         # Models initialization
│   ├── course_item.py      # Course Item model
│   ├── specialization.py   # Specialization model
├── resources/              # API resources
│   ├── __init__.py         # Resources initialization
│   ├── course_item.py      # Course Item resource
│   ├── specialization.py   # Specialization resource
├── schemas.py              # Marshmallow schemas for validation
├── db.py                   # Database connection setup
```

---

## API Endpoints

### Specialization Endpoints
- `GET /specialization`: Retrieve all specializations.
- `POST /specialization`: Add a new specialization.
- `GET /specialization/<string:specialization_id>`: Retrieve a specialization by ID.
- `DELETE /specialization/<string:specialization_id>`: Delete a specialization by ID.

### Course Item Endpoints
- `GET /course_item`: Retrieve all course items.
- `POST /course_item`: Add a new course item.
- `GET /course_item/<string:course_item_id>`: Retrieve a course item by ID.
- `PUT /course_item/<string:course_item_id>`: Update a course item by ID.
- `DELETE /course_item/<string:course_item_id>`: Delete a course item by ID.

---

## Environment Variables
You can use a `.env` file to manage environment variables.

Example `.env` file:
```
FLASK_ENV=development
DATABASE_URL=sqlite:///data.db
```

---

## Docker Usage
### Build the Docker Image
```bash
docker build -t rest-apis-flask-python .
```

### Run the Docker Container
```bash
docker run -d -p 5000:5000 rest-apis-flask-python
```

### Use Docker Compose
```bash
docker-compose up
```

---

## Technologies Used
- Flask
- Flask-Smorest
- Marshmallow
- Docker
- SQLAlchemy

---

## Future Enhancements
- Add database migrations with Alembic.
- Implement user authentication and authorization.
- Expand API to include additional entities and features.

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

