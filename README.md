# Overview

In the pursuit of advancing my skills as a software engineer and exploring the integration of modern web technologies with cloud-based storage solutions, I have developed a comprehensive Inventory Management System. This project is a practical application of Python programming, specifically utilizing FastAPI for the backend and Firebase Firestore as the cloud database. The system is designed to facilitate real-time tracking of inventory transactions, supplier details, and product information, showcasing the powerful combination of FastAPI's asynchronous capabilities with Firestore's scalable and flexible database services.

The Inventory Management System is a RESTful API that provides a seamless interface for managing inventory data, including products, suppliers, and inventory transactions. Users can perform CRUD (Create, Read, Update, Delete) operations on products and suppliers, as well as record and retrieve inventory transactions, all through a clean and intuitive set of API endpoints.

The backend is built with FastAPI, chosen for its high performance and ease of use, particularly its automatic Swagger documentation, which simplifies testing and interaction with the API. The system integrates with Firebase Firestore, a NoSQL cloud database, to store and manage data. Firestore's real-time update capabilities are leveraged to monitor inventory changes, ensuring that users have access to the most current data.

## Usage

Start cloning this repository to your local machine to use the Inventory Management System. Ensure you have Python installed, and install the required dependencies:

```
pip install -r requirements.txt
```

Then, initialize the Firebase application with your Firebase project credentials by replacing "credentials.json" with the path to your Firebase service account key file.

Launch the FastAPI application by running:

```
uvicorn app.main:app --reload
```

This starts the local server and enables live reloading for development.

Access the Swagger UI documentation by navigating to http://localhost:8000/docs in your web browser. This interface allows you to test all available API endpoints, such as adding new products, creating suppliers, and recording inventory transactions.

The development of this Inventory Management System was motivated by a desire to deepen my understanding of asynchronous web frameworks and cloud-based data storage solutions. This project has provided valuable experience designing and implementing RESTful APIs, working with NoSQL databases, and employing real-time data synchronization techniques. Through this endeavor, I aimed to build a functional, real-world application that demonstrates effective data management practices and the integration of cloud services in software development.

[Software Demo Video](https://youtu.be/1rECmI4SRow)

# Cloud Database

I've chosen Firebase Firestore as the cloud database for this Inventory Management System. Firestore is a flexible, scalable mobile, web, and server development database from Firebase and Google Cloud Platform. It provides powerful querying, real-time data synchronization, and automatic multi-region data replication. Firestore is a NoSQL database that stores data in documents organized into collections. Documents can contain complex nested objects, and collections can contain documents pointing to subcollections, offering a rich, hierarchical way to organize data.

The database for the Inventory Management System is structured into three main collections: **products**, **suppliers**, and **inventory**. Each collection is designed to hold documents representing entities within the system, with fields tailored to the specific requirements of each entity type.

## Products Collection

-   Document ID: Auto-generated unique identifier for each product.
-   Fields:
    -   name: String, the name of the product.
    -   description: String, a brief description of the product.
    -   price: Float, is the price of the product.
    -   quantity: Integer, the current stock level of the product.

## Suppliers Collection

-   Document ID: Auto-generated unique identifier for each supplier.
-   Fields:
    -   name: String, the name of the supplier.
    -   contact_info: String, contact details of the supplier.
    -   products: Array of DocumentReferences, references to the products collection indicating which products the supplier provides.

## Inventory Collection

-   Document ID: Auto-generated unique identifier for each inventory transaction.
-   Fields:
    -   product_id: DocumentReference, a reference to a product in the products collection affected by the transaction.
    -   type: String, the type of transaction (e.g., "restock", "sale").
    -   quantity: Integer, the amount involved in the transaction.
    -   date: Timestamp, when the transaction occurred.

# Development Environment

Python 3.12.1  
Visual Studio Code  
Git & Github  
Firebase Admin SDK

# Useful Websites

-   [An Introduction to Cloud Databases](https://www.oreilly.com/library/view/an-introduction-to/9781492044857/ch01.html)
-   [Firestore Tutorial](https://firebase.google.com/docs/firestore)
-   [Get started with Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart#locked-mode)
-   [FastAPI Docs](https://fastapi.tiangolo.com/)

# Future Work

-   Enhance API Documentation.
-   Refine notifications System.
-   Create Fronted for the API.
-   Implement User Authentication and Authorization.
-   Optimize Database Queries.
-   Expanding Reporting and Analytics.
