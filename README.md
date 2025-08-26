# Healthify: Disease Prediction Using Machine Learning

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/naitri/healthify-django)

Welcome to Healthify, an innovative project focused on predicting five different diseases using various machine learning models. Healthify utilizes state-of-the-art techniques to forecast the likelihood of Diabetes, Heart Disease, Pneumonia, Parkinson's Disease, and Breast Cancer. This project implements Random Forest Classifier, Extra Trees Classifier, Light GBM Classifier, Gradient Boosting Classifier, and a Convolutional Neural Network (CNN) model, all wrapped in a user-friendly web application built with Django.

## Live Demo

You can try out a live version of Healthify hosted on Hugging Face Spaces:

[https://huggingface.co/spaces/naitri/healthify-django](https://huggingface.co/spaces/naitri/healthify-django)

## About Healthify

Healthify aims to empower individuals by providing them with insights into their health risks for common diseases. By leveraging machine learning algorithms, Healthify analyzes relevant medical data to offer predictions with high accuracy. Whether you're looking to take proactive steps towards preventive care or seeking early detection for potential health issues, Healthify serves as a valuable tool for health assessment and monitoring.

## Features

*   **Multi-Disease Prediction**: Predicts the likelihood of five different diseases: Diabetes, Heart Disease, Pneumonia, Parkinson's Disease, and Breast Cancer.
*   **Machine Learning Models**: Incorporates various models, including Random Forest, Extra Trees, LightGBM, Gradient Boosting, and a CNN for robust and accurate predictions.
*   **User-Friendly Interface**: A clean and simple web interface built with Django, making it easy to input medical data and understand the results.
*   **Dockerized**: Comes with a `Dockerfile` and `docker-compose.yml` for easy setup and deployment.

## Screenshots

*A preview of the main page:*

![Healthify Home Page](screenshots/home.png)

*An example of the disease prediction form:*

![Disease Prediction Form](screenshots/prediction-form.png)

*Showing the prediction result:*

![Prediction Result](screenshots/result.png)


## Getting Started

You can run Healthify on your local machine in two ways:

### Option 1: Using Docker (Recommended)

This is the easiest way to get Healthify running.

**Prerequisites:**
*   Docker
*   Docker Compose

**Installation:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Healthify.git
    cd Healthify
    ```

2.  **Run with Docker Compose:**
    ```bash
    docker-compose up
    ```

3.  **Access the web application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

### Option 2: Manual Installation

**Prerequisites:**
*   Python 3.10
*   pip

**Installation:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/naitridoshi/Healthify.git
    cd Healthify
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Django development server:**
    ```bash
    cd source
    python manage.py runserver
    ```

5.  **Access the web application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1.  **General Questionnaire**: Start by answering the general questionnaire to get a preliminary assessment and recommended tests.
2.  **Disease Prediction**: Navigate to the specific disease prediction page you are interested in.
3.  **Input Data**: Fill in the required medical data in the provided form.
4.  **Get Prediction**: Submit the form to receive a prediction and recommendations.

## Models Used

*   **Diabetes**: Extra Trees Classifier
*   **Heart Disease**: Gradient Boosting Classifier
*   **Pneumonia**: Convolutional Neural Network (CNN)
*   **Parkinson's Disease**: Light GBM Classifier
*   **Breast Cancer**: Random Forest Classifier

## Project Structure

*   `ml_modules/`: Contains the Jupyter notebooks for model training and the saved model files.
*   `source/`: Contains the Django web application code.
*   `Dockerfile`: Defines the Docker image for the application.
*   `docker-compose.yml`: Defines the services, networks, and volumes for Docker.

---