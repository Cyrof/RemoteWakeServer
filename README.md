# Wake-on-LAN HTTP Server

A simple project that allows you to send Wake-on-LAN (WoL) magic packets via HTTP requests. It consists of two scripts: `main.py` for sending the WoL packets and `server.py` for handling HTTP requests that trigger the `main.py` script.

## Prequisites

1. **Python:** Ensure you have [Python](https://www.python.org/downloads/) installed in your machine.

2. **Dependencies:** Install the required dependencies using the provided `requirements.txt`.

## Setup Instructions
### Using Docker
This project includes a Docker image that can be found on Docker Hub. You can set up and run the project using Docker without needing to manually configure a Python environment.

### 1. **Pull the Docker image**
Pull the Docker image from Docker Hub:
```sh
$ docker pull cyrof/remotewakeserver:latest
```

### 2. **Run the Docker Container**
Run the Docker container with the necessary environment variables for the MAC address and broadcast IP:
```sh
$ docker run -d -p 8000:8000 --env MAC="xx-xx-xx-xx-xx-xx" --env BROADCAST="xxx.xxx.255.255 cyrof/remotewakeserver:latest
```
Replace `xx-xx-xx-xx-xx-xx` with the target MAC address and `xxx.xxx.255.255` with the appropriate broadcast address.

### Using Docker Compose 
Alternatively, you can use Docker Compose to set up and run the project. Create a `docker-compose.yaml` file with the following content:
```yaml
version: '3'
services: 
    wol-server:
        image: cyrof/remotewakeserver:latest
        ports:
          - "8000:8000"
        environment:
          MAC: "xx-xx-xx-xx-xx-xx"
          BROADCAST: "xxx.xxx.255.255"
```
Then, run the following command to start the service:
```sh
$ docker-compose up -d 
```

### Standard Setup (Non-Docker)
### 1. **Create a `.env` File**
For `main.py` to function correctly, create a `.env` file in the root directory of the project. The `.env` file must contain the MAC address of the target computer and the broadcast IP in the following format: 
```makefile
MAC="xx-xx-xx-xx-xx-xx"
BROADCAST="xxx.xxx.255.255"
```
Replace `xx-xx-xx-xx-xx-xx` with the target MAC address and `xxx.xxx.255.255` with the appropriate broadcast address.

### 2.  **Install Dependencies**
If is recommended to use a virtual environment for managing dependencies.
Follow the steps below to set up a virtual environment and install the necessary packages: 

#### **Using Virtual Environment:**

 1. **Create a virtual environment:**
     ```sh
     $ Python -m venv <venv-name>
     ```

 2. **Activate the virtual environment:**

     - On Windows
     
         ```sh
         $ <venv-name>\Scripts\activate
         ```

     - On macOS/Linux:
     
         ```sh
         $ source <venv-name>\bin\activate
         ```

 3. **Install the dependencies:**
     ```sh
     $ pip install -r requirements.txt
     ```

#### **Globally (Not Recommended):**
If you prefer to install the dependencies globally, use:

```sh 
$ pip install -r requirements.txt
```

### 3. **Running the Server**
To start the HTTP server, run the `server.py` script:
```sh
$ python server.py
```
The server will start on 'localhost' at port '8000'.

## Usage
### Handling Get Requests
Send a Get requests to the server:
```sh
$ curl http://localhost:8000
```
The server will respond with:
```kotlin
Hello this is working
```

### Handling POST Requests
Send a POST request to the server: 
```sh
$ curl -X POST http://localhost:8000
```
The server will respond with: 
```kotlin
Post is working
```
Additionally, this will trigger the execution of the `main.py` script, which sends the Wake-on-LAN magic packet using the details specified in the `.env` file.

## Project Structure

- **main.py:** Script to send Wake-on-LAN magic packets.
- **server.py:** Simple HTTP server that handles GET and POST requests.
- **requirements.txt:** List of dependencies required for the project.
- **Dockerfile:** Dockerfile to create a Docker image for the project.
- **docker-compose.yaml:** Docker compose configuration file.

## Contributing 
Feel free to contribute to this project by forking this reopsitory and creating a pull request with your changes.

## Issues
If you encounter any issues of have suggestions for improvements, please open an issue in the repository 

## License
This project is licensed under the MIT license.
