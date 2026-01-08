# 🚗 Drive Now System
![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)

A robust microservices architecture for managing car rentals. This system consists of two isolated services
**Car Inventory** and **Booking** communicating via REST APIs and utilizing dedicated PostgreSQL databases.

## My System Architecture
<p>
  <img src="media_files/system_architecture2.png" width="998" title="Project Logo" alt="">
</p>
The system is designed as a Microservices Architecture, that split to few services. 
This design prioritizes Separation of Concerns, Scalability, and Data Integrity.

- Booking Service - handles the business logic of renting cars, Validates and creates new rental reservations.
- Car Inventory service - manager of the cars stock. It is the only service authorized to modify cars data, responds to 
HTTP requests from the Booking Service to confirm if a specific car is currently available.
- API Gateway - Acts as the single entry point for all client requests. and load balancer
- User Service - handle the lifecycle of the user object  
- Auth & payment - additional services that can be integrated as future features to the car rental system. 
These are built-in services that require only configuration to be enabled, and they offer multiple options depending 
on the environment in which the system is deployed

### Why PostgreSQL?
PostgreSQL was selected as the relational database for this system for the following reasons:

- Structured Relational Data: The main objects (Cars and Rentals) are structured and have strict schema, 
making a relational database superior to a NoSQL DB.

- ACID Compliance: PostgreSQL provides robust ACID compliance. 
Transactions will be automic, leave the DB in a consistent state, not interfere with each other, and the DB will be durable.

- PostgreSQL is less suitable for horizontal scaling because it doesn't provide built-in sharding and replication features. 
As a result, these features must be managed manually if we'd like to introduce them, which increases operational complexity.
Although, if we choose not to introduce them, the database will only have one instance and will become less reliable.
Despite this, for now one instance of PostgreSQL (which can be vertically scaled) will satisfy our system requirements, 
as correctness is the most critical requirement in our system.

### Why use blocking Request-Response communication between booking and car inventory services?
Between the booking service and the car inventory service we require request-response communication because, 
when a user attempts to book a car, the system must **immediately** return a response indicating whether the operation succeeded or failed. 
message brokers are unidirectional communication that occur eventually and are therefore not suitable in this scenario
because it cannot return an immediate response, making it impossible to provide real time response to the user.



## 🏗 Architecture


* **Inventory Service (Port 3131):**
    * Manages the fleet of cars (CRUD).
    * Handles availability status logic.
    * Folder: `car_inventory_service/`
* **Booking Service (Port 1313):**
    * Handles customer reservations.
    * Communicates synchronously with Inventory to lock cars.
    * Folder: `booking_service/`
* **Infrastructure:**
    * **2 Databases:** `cars_inventory_db` and `booking_db` (PostgreSQL).
    * **Orchestration:** Docker Compose.
    * **Metrics:** Prometheus metrics.

---

## 🚀 How to Run the Project
Open your terminal in the project root folder (where `docker-compose.yml` is located) and run:

```bash

docker-compose up -d --build
```

## 📖 How to Use the API (Swagger UI)

The easiest way to interact with the system is via the automatic documentation pages provided by FastAPI.

| Service               | URL | Description                       |
|:----------------------| :--- |:----------------------------------|
| **Car Inventory API** | [http://localhost:3131/docs](http://localhost:3131/docs) | Add car, update status, all cars. |
| **Booking API**       | [http://localhost:1313/docs](http://localhost:1313/docs) | start new rentals and end them.   |

## 💻 How to Use via CLI (Terminal)

If you prefer using `curl` or Postman, here are the commands.

### 1. Add a Car (Inventory)

```bash
curl -X 'POST' \
  'http://localhost:3131/car' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "550e0085-e28b-41d4-a716-446655440000"
  "model": "Tesla Model 3",
  "year": 2024,
  "status": "available"
}'
```

## 💻 Screenshots usage 
Figure 1: Integration test result showing successful retrieval of all cars stored in the database
<p>
  <img src="media_files/usage_screenshots/car_inventory.get_all_cars.png" width="200" alt="">
</p>
Figure 2: Docker Compose setup showing successful provisioning of all dependent services required by the system. 
<p>
  <img src="media_files/usage_screenshots/docker-compose%20results.png" width="200" alt="">
</p>
Figure 3: Monitoring metrics showing the performance and health of the Car Inventory service.
<p>
  <img src="media_files/usage_screenshots/metrics.png" width="200" alt="">
</p>
Figure 4: Test execution results for the car inventory service, showing running and passed tests.
<p>
  <img src="media_files/usage_screenshots/tests.png" width="100" alt="">
</p>