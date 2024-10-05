# Gemini Pro Q&A App

## Overview

The **Gemini Pro Q&A App** is a web application that leverages the capabilities of Google Gemini Pro to provide interactive and intelligent responses to user queries. Built using Streamlit and Python, this application offers a user-friendly interface for asking questions and receiving AI-generated answers in real-time.

## Features

- **Interactive Q&A**: Engage with the AI by entering your questions.
- **Real-time Responses**: Get instant answers powered by Google Gemini Pro.
- **User-Friendly Interface**: Clean and intuitive design for a seamless experience.
- **Error Handling**: Alerts users if they attempt to submit an empty question.

## Technologies Used

- **Python**: The primary programming language for the application.
- **Streamlit**: A powerful framework for building web applications with minimal effort.
- **Google Gemini Pro**: The AI model used for generating responses.
- **python-dotenv**: For managing environment variables securely.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HananeNadi/Gemini-Pro-Q-A-App.git
   cd /Gemini-Pro-Q-A-App
   ```

2. **Create and Activate a Virtual Environment:**
    It's recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
   ``` 

3. **Set Up Your Environment Variables:**

    Create a .env file in the root directory of your project and include your Google API key:
     ```bash
    GOOGLE_API_KEY=your_google_gemini_pro_api_key
    ``` 

4. **Run the Application:**

     ```bash
    streamlit run App.py
    ``` 

5. **Access the App:**
     Open your web browser and navigate to http://localhost:8501/ to interact with the application.



## Authors

- [@HananeNadi](https://github.com/HananeNadi)

## Contact Me

Feel free to contact me at:

- Email: nadi.hanane01@gmail.com
- LinkedIn: [Hanane Nadi](https://www.linkedin.com/in/hanane-nadi-32089a251/)
