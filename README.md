# Healthify: Disease Prediction Using Machine Learning Models

Welcome to Healthify, an innovative project focused on predicting five different diseases using various machine learning models. Healthify utilizes state-of-the-art techniques to forecast the likelihood of Diabetes, Heart Disease, Pneumonia, Parkinson's Disease, and Breast Cancer. This project implements Random Forest Classifier, Extra Trees Classifier, Light GBM Classifier, Gradient Boosting Classifier, and a Convolutional Neural Network (CNN) model, all wrapped in a user-friendly web application built with Django, a popular web development framework in Python.

## About Healthify

Healthify aims to empower individuals by providing them with insights into their health risks for common diseases. By leveraging machine learning algorithms, Healthify analyzes relevant medical data to offer predictions with high accuracy. Whether you're looking to take proactive steps towards preventive care or seeking early detection for potential health issues, Healthify serves as a valuable tool for health assessment and monitoring.

## Features

*   **Multi-Disease Prediction**: Healthify is capable of predicting the likelihood of five different diseases: Diabetes, Heart Disease, Pneumonia, Parkinson's Disease, and Breast Cancer.
*   **Machine Learning Models**: The project incorporates various machine learning models, including Random Forest Classifier, Extra Trees Classifier, Light GBM Classifier, Gradient Boosting Classifier, and a Convolutional Neural Network (CNN) model, to ensure robust and accurate predictions.
*   **User-Friendly Interface**: Healthify offers a user-friendly web interface built with Django, making it easy for users to input their medical data, receive predictions, and interpret the results.

## Getting Started

To run Healthify locally and explore its functionalities, follow these steps:

### Prerequisites

*   Python 3.8 or higher
*   pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Healthify.git
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
    Open your preferred web browser and navigate to `http://127.0.0.1:8000/`.

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

*   `ml_modules/`: Contains the Jupyter notebooks used for training the machine learning models and the saved model files.
*   `source/`: Contains the Django web application code.