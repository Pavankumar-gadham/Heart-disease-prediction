Heart Disease Prediction

Overview:

The Heart Disease Prediction project aims to predict the likelihood of heart disease in patients using machine learning models. The application uses Python for data processing and modeling, Flask for web deployment, and MySQL for database management.

Features:

Predictive Modeling: Utilizes machine learning algorithms to predict heart disease risk.

Web Application: Provides an interactive user interface using Flask.

Database Integration: Stores patient data and prediction results using MySQL.

User-Friendly Interface: Allows users to input patient data and view predictions easily.

Tools and Technologies:

Python: Programming language used for data analysis and machine learning.

Scikit-Learn: Library for implementing machine learning algorithms.

Flask: Web framework for deploying the machine learning model as a web application.

MySQL: Database management system for storing patient data and results.

Pandas: Data manipulation and analysis library.

NumPy: Library for numerical computations.

Matplotlib: Library for data visualization.

Installation:

Prerequisites

Python 3.x
MySQL Server

Input Data:

Enter patient information into the provided fields. The application will use this data to predict the likelihood of heart disease.

View Results:

After submission, the application will display the prediction results and save the data to the MySQL database.

Code Structure:

app.py: Main Flask application file that handles web requests and integrates the machine learning model.

model.py: Contains the machine learning model training and prediction logic.

database.py: Manages database connections and operations.

static/: Directory for static files like CSS and JavaScript.

templates/: Directory for HTML templates used by Flask.

create_tables.sql: SQL script to set up the database schema.

requirements.txt: Lists all required Python packages.

Contributing:

We welcome contributions to improve this project! To contribute:

Fork the repository.

Create a new branch for your changes.

Make your modifications.

Submit a pull request with a clear description of your changes.
