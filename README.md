# todo-drf
A simple to-do app built with Django and DRF  

## Features  
- **CRUD Operations** (Create, Read, Update, Delete) for Todos  
- **RESTful API Endpoints**  
- **Django + DRF** for easy API development  

## Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/dead1x/todo-drf.git
   cd todo-drf
   ```

2. **Install dependencies using Poetry**  
   ```bash
   poetry install
   ```

3. **Apply migrations**  
   ```bash
   poetry run python manage.py migrate
   ```

4. **Run the server**  
   ```bash
   poetry run python manage.py runserver
   ```

## API Endpoints  

- **GET** `/api/todos/` → List all todos  
- **POST** `/api/todos/` → Create a new todo  
- **GET** `/api/todos/{id}/` → Retrieve a specific todo  
- **PUT** `/api/todos/{id}/` → Update a specific todo  
- **DELETE** `/api/todos/{id}/` → Delete a specific todo  

## ⚡ License  
This project is licensed under the **MIT License**.  