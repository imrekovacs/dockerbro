# Ok-Bro-App

A simple REST API built with Flask that responds with "Ok Bro" when a text input is sent to it. This application is containerized with Docker for ease of deployment.

## Purpose
The purpose of this project is to demonstrate how to use Docker to containerize a simple Python application.

## Features
- Accepts JSON input via a POST request.
- Responds with a simple message: "Ok Bro".
- Lightweight and easy to set up.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- Basic knowledge of command-line tools

---

## Installation and Setup

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/<your-username>/ok-bro-app.git

# Navigate into the project directory
cd ok-bro-app
```

### Step 2: Verify Files
Ensure the following files exist in the project directory:

```
ok-bro-app/
├── app.py       # Main application file
├── Dockerfile   # Docker configuration file
```

### Step 3: Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t ok-bro-app .
```

This creates a Docker image tagged `ok-bro-app`.

---

## Running the Application

### Step 1: Start the Docker Container

Use the following command to start the application:

```bash
docker run -p 8080:5000 ok-bro-app
```

This maps port `5000` inside the container to port `8080` on your local machine.

### Step 2: Access the Application

You can now send a POST request to the `/message` endpoint of the application.

#### Example Using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello"}' http://localhost:8080/message
```

You should receive a response like this:

```json
{
  "response": "Ok Bro"
}
```

#### Example Using Postman:

1. Open Postman.
2. Create a new POST request.
3. Set the URL to `http://localhost:8080/message`.
4. Add the following JSON in the request body:
   ```json
   {
     "text": "Hello"
   }
   ```
5. Click **Send**.
6. The response will be:
   ```json
   {
     "response": "Ok Bro"
   }
   ```

---

## Stopping the Application

To stop the running Docker container, press `Ctrl+C` in the terminal where the container is running.

Alternatively, list the containers and stop it using:

```bash
# List running containers
docker ps

# Stop the container by container ID
docker stop <container-id>
```

---

## Notes

- **Development Mode**: This application is running on Flask's built-in development server. For production, consider using a WSGI server like `gunicorn`.
- **Port Conflicts**: If port `8080` is already in use on your system, change the host port in the `docker run` command. For example:
  ```bash
  docker run -p 8081:5000 ok-bro-app
  ```

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributions
Feel free to fork the repository and submit pull requests. Contributions are welcome!

