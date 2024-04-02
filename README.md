# basic_crud_server

This server-side application provides authentication and authorization functionality for user management. It supports sign-up, sign-in, and role-based access control for various endpoints.

## Features

- User sign-up with secure storage of username, password, and role.
- User sign-in with username and password authentication.
- Role-based access control:
  - Admin users have access to all endpoints.
  - Guest users have limited access to specific endpoints.

## Technologies Used

- Python
- FastAPI
- bcrypt (for password hashing)
- JSON Web Tokens (JWT) for authentication
  
## Usage
1. Run the server:
```bash
uvicorn app:app --reload
```
2. Access the provided endpoints using a web browser or an API testing tool like Postman or 'curl'.

## Endpoints
### Sign-up
* **URL**: `/auth/sign_up`
* **Method**: `POST`
* **Description**: Registers a new user with a username, password, and role.
Request Body:
```json
{
  "username": "example_user",
  "password": "example_password",
  "role": "admin"
}
```
* **Response**: Returns a message confirming user creation and a authentication token.
* **Curl Command**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "example_user", "password": "example_password", "role": "admin"}' http://localhost:8000/auth/sign_up
```

### Sign-in
* **URL**: `/auth/sign_in`
* **Method**: `POST`
* **Description**: Authenticates a user with a username and password.
Request Body:
```json
{
  "username": "example_user",
  "password": "example_password"
}
```
**Response**: Returns a message indicating sign-in success or failure, along with an authentication token.
* **Curl Command:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "example_user", "password": "example_password"}' http://localhost:8000/auth/sign_in
```

### Add Student (Accessible only for Admins)

- **URL:** `/students`
- **Method:** `POST`
- **Description:** Adds a new student to the system.
- **Authentication:** Only accessible for admin users.
- **Request Body:** Provide student details.

  ```json
  {
    "id": 123,
    "name": "John Doe",
    "class": "Math"
  }


### Get Students by Class (Accessible only for Admins)

- **URL:** `/students/{class_name}`
- **Method:** `GET`
- **Description:** Retrieves students belonging to a specific class.
- **URL Parameters:** `class_name` - The name of the class to retrieve students for.
- **Authentication:** Accessible for all authenticated users.
- **Response:** Returns a list of students in the specified class.

  ```json
  [
    {
      "id": 123,
      "name": "John Doe",
      "class": "Math"
    },
    {
      "id": 124,
      "name": "Jane Smith",
      "class": "Math"
    },
    ...
  ]


### Get All Students

- **URL:** `/students`
- **Method:** `GET`
- **Description:** Retrieves all students.
- **Authentication:** Accessible for all authenticated users.
- **Response:** Returns a list of all students.

  ```json
  [
    {
      "id": 123,
      "name": "John Doe",
      "class": "Math"
    },
    {
      "id": 124,
      "name": "Jane Smith",
      "class": "History"
    },
    ...
  ]


### Get Student by ID

- **URL:** `/students/{student_id}`
- **Method:** `GET`
- **Description:** Retrieves a student by their ID.
- **URL Parameters:** `student_id` - The ID of the student to retrieve.
- **Authentication:** Accessible for all authenticated users.
- **Response:** Returns the student with the specified ID.

  ```json
  {
    "id": 123,
    "name": "John Doe",
    "class": "Math"
  }




