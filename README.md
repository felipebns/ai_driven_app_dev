# AI-Driven Application Development - Personal Classwork Repository 

## About Me

Hello! I'm Felipe, a developer currently in my 4th year of computer engineering and very interested in coming up with a AI driven app that could give me revenue in a near future

---

## Possible Skills & Tools in this project 

### Programming Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Libraries & Frameworks
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

### Tools & Platforms
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## Directory Structure

```
ai_driven_app_dev/
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
│
├── backend/                  # FastAPI backend
│   ├── main.py              # FastAPI application entry point
│   ├── api/                 # API routes and endpoints
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models/              # ML models and data models
│   │   ├── __init__.py
│   │   └── ml_models.py
│   ├── services/            # Business logic and services
│   │   ├── __init__.py
│   │   └── predictions.py
│   └── config.py            # Configuration settings
│
├── frontend/                 # Streamlit frontend
│   ├── app.py               # Main Streamlit application
│   ├── pages/               # Multi-page app structure
│   │   ├── 1_dashboard.py
│   │   └── 2_predictions.py
│   └── components/          # Reusable UI components
│       └── widgets.py
│
├── data/                     # Data files and datasets
│   ├── raw/                 # Raw, unprocessed data
│   ├── processed/           # Cleaned and processed data
│   └── models/              # Trained model files (.pkl, .h5)
│
│
├── tests/                    # Unit and integration tests
│   ├── test_api.py
│   └── test_models.py
│
└── utils/                    # Utility scripts and helpers
    ├── __init__.py
    ├── data_processing.py
    └── helpers.py
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git installed on your system

### Clone the Repository
```bash
git clone https://github.com/[your-username]/ai_driven_app_dev.git
cd ai_driven_app_dev
```

### Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Running the Application

### Option 1: Run Backend and Frontend Separately

#### Start the FastAPI Backend
```bash
# From the root directory
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
The API will be available at `http://localhost:8000`  
API documentation (Swagger UI) at `http://localhost:8000/docs`

#### Start the Streamlit Frontend
```bash
# Open a new terminal, from the root directory
cd frontend
streamlit run app.py
```
The Streamlit app will open automatically in your browser at `http://localhost:8501`

### Option 2: Run Both Services with One Command (Optional)

Create a simple startup script or use process managers like `tmux` or `screen`:
```bash
# Install tmux (if not installed)
# sudo apt install tmux  # Linux
# brew install tmux      # macOS

# Run both services
tmux new-session -d -s backend 'cd backend && uvicorn main:app --reload'
tmux new-session -d -s frontend 'cd frontend && streamlit run app.py'

# To stop services
tmux kill-session -t backend
tmux kill-session -t frontend
```

### Testing
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_api.py
```

---

## Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/felipebns)

---