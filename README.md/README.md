# LMS Web Scraper Chatbot

A prototype of a chatbot that scrapes web content based on user commands. This project demonstrates a full-stack application with a clean frontend and a backend that uses Python for web scraping.

## ✨ Features

- *Conversational Interface:* A user-friendly chat interface built with HTML, CSS, and JavaScript.
- *Rule-Based Backend:* The chatbot responds to simple commands like "news" and "tech".
- *Web Scraping:* Fetches and summarizes content from websites using Python.
- *API-First Design:* Frontend and backend communicate via a simple REST API.

## 🚀 Technologies Used

*Frontend:*
- *HTML5:* For the page structure.
- *CSS3:* For styling the chat interface.
- *JavaScript (ES6+):* For handling user interactions and API calls.

*Backend:*
- *Python:* The core programming language.
- *FastAPI:* A modern, fast web framework for building the API.
- *requests & BeautifulSoup4:* Libraries used to fetch and parse HTML for web scraping.

## 📦 Getting Started

### Prerequisites

- Python 3.9+
- A code editor like VS Code

### Installation & Setup

1.  *Clone the repository:*
    bash
    git clone [https://github.com/your-username/LMS_Chatbot.git](https://github.com/your-username/LMS_Chatbot.git)
    cd LMS_Chatbot
    

2.  *Set up the backend:*
    - Navigate to the backend directory.
    - Create a virtual environment and activate it:
      bash
      cd backend
      python -m venv venv
      # On Windows
      .\venv\Scripts\activate
      # On macOS/Linux
      source venv/bin/activate
      
    - Install the required Python packages:
      bash
      pip install -r requirements.txt
      

### Running the Application

1.  *Start the backend server:*
    - Make sure your virtual environment is active.
    - Run the following command from the backend directory:
      bash
      uvicorn main:app --reload
      
    - The server will start on http://127.0.0.1:8000.

2.  *Open the frontend:*
    - Go to your web browser and navigate to http://127.0.0.1:8000. The frontend will be served by the FastAPI server.

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.