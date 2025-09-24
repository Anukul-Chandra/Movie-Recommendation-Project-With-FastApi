# 🎬 Movie Recommendation System with FastAPI

A production-ready Movie Recommendation Web API built using FastAPI.  
This project serves personalized movie suggestions powered by a Machine Learning model and exposes RESTful endpoints for easy integration with any frontend.

---

## ✨ Features
- ⚡ FastAPI backend with async endpoints
- 🎯 Content-based recommendation using movie similarity
- 🔍 Search API for finding movies by title
- 🤝 /predict endpoint for generating recommendations
- 🌐 CORS enabled for frontend integration
- 📜 Interactive API docs available at /docs (Swagger UI)
- 🐳 Docker-ready for consistent deployment
- ☁️ Deployable on Render

---

## 📂 Video & Image: 


https://github.com/user-attachments/assets/91a1e393-cbb4-4ae0-81fc-db29d3dbad9d



<img width="2540" height="2076" alt="screencapture-movie-recommendation-project-with-jpm2-onrender-2025-09-24-12_27_07" src="https://github.com/user-attachments/assets/49c1fb1d-d145-4348-a15d-c9bc66d290ec" />

<img width="2538" height="2076" alt="screencapture-movie-recommendation-project-with-jpm2-onrender-2025-09-24-12_29_13" src="https://github.com/user-attachments/assets/9ee91c89-0ee5-4b20-b8d8-cf1a7787b56e" />



## Download similarity.pkl file

The similarity matrix file (`similarity.pkl`) is too large to be stored in the repository. Please download it manually from the link below and place it in the project root directory:

[Download Cosine_ similarity.pkl](https://drive.google.com/file/d/1TzR82vf9JDxSZR04sX7lDdowTINbqoY0/view?usp=drive_link)

[Download Movies_dictionary.pkl](https://drive.google.com/file/d/1ELqd7chpU4LxhiLd1KEyeFHIKuEF5Ms1/view?usp=drive_link)

# Live Demo :

You can see the project here : https://movie-recommendation-project-with-jpm2.onrender.com/

## 🛠️ Installation & Run Guide

### Prerequisites

• Python 3.8+
• pip package manager
• Git

### Backend Setup (FastAPI)

1. Clone the repository:
```bash
git clone <repository-url>
cd movie-recommendation-system
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required files (see Download section above)

5. Run the FastAPI server:
```bash
uvicorn app:app --reload
```

### Frontend Setup (HTML, CSS, JS)

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Start local server:
```bash
python -m http.server 5501
```

3. Open in browser: [http://127.0.0.1:5501/index.html](http://127.0.0.1:5501/index.html)

## 🧭 API Reference

**Base URL:** `http://localhost:8000/` (or your deployed host)

### Get Movie Recommendations

**POST** `/predict`

| Parameter | Type   | Description          |
|-----------|--------|----------------------|
| movie     | string | Required. Movie title|

**Request Body:**
```json
{"movie": "Inception"}
```

**Response:**
```json
{
  "recommendations": [
    "The Matrix",
    "Interstellar",
    "The Dark Knight",
    "Fight Club",
    "Pulp Fiction"
  ]
}
```

### Search Movies

**GET** `/search?title={title}`

| Parameter | Type   | Description                    |
|-----------|--------|--------------------------------|
| title     | string | Required. Movie title to search|

### Interactive Documentation

**GET** `/docs`

Interactive Swagger UI to explore and test all endpoints.

## 📋 Example Usage

### Get Recommendations (cURL)
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"movie": "Inception"}'
```

### Search Movies (cURL)
```bash
curl -X GET "http://localhost:8000/search?title=Matrix"
```

### Python Example
```python
import requests

# Get recommendations
response = requests.post(
    "http://localhost:8000/predict",
    json={"movie": "Inception"}
)
recommendations = response.json()
print(recommendations)

# Search movies
response = requests.get(
    "http://localhost:8000/search",
    params={"title": "Matrix"}
)
results = response.json()
print(results)
```

### JavaScript Example
```javascript
// Get recommendations
fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({movie: 'Inception'})
})
.then(response => response.json())
.then(data => console.log(data));

// Search movies
fetch('http://localhost:8000/search?title=Matrix')
.then(response => response.json())
.then(data => console.log(data));
```

## 🚢 Deployment

**Production Environment:** This project is designed to run in production using Render cloud platform with GitHub integration, providing reliable, scalable hosting with automatic deployments.

### ☁️ Deploy on Render via GitHub Integration

Render with GitHub integration is the exclusive deployment method for this project.

1. **Connect your GitHub repository to Render:**
   1. Push your code to a GitHub repository
   2. Sign in to [Render](https://render.com/)
   3. Click "New +" and select "Web Service"
   4. Connect your GitHub account and select the repository

2. **Configure the deployment settings:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - Environment: Python 3

3. **Add environment variables (if needed):**
   - Set any required environment variables in the Render dashboard

4. **Deploy automatically:**
   - Render will automatically build and deploy your application
   - Future pushes to your main branch will trigger automatic redeployments

### Benefits of Render + GitHub deployment:
- Automatic deployments from GitHub commits
- Zero-downtime deployments with health checks
- Automatic HTTPS certificates for secure connections
- Built-in monitoring and logging for production insights
- Automatic scaling based on traffic demands
- Easy environment variable management through dashboard
- Branch-based deployments for testing different versions
- Docker-ready configuration for containerized deployment

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest tests/

# Run with coverage
pytest --cov=app tests/
```

## 🤝 Contributing

Contributions are always welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://readme.so/LICENSE) file for details.

## 🙏 Acknowledgements

• Built with [FastAPI](https://fastapi.tiangolo.com/)
• Machine Learning powered by [Scikit-learn](https://scikit-learn.org/)
• **Production deployment via [Render](https://render.com/) with GitHub integration**
• Frontend styling with modern CSS
• Movie data from [TMDB API](https://www.themoviedb.org/documentation/api)
• Markdown README generated by [readme.so](https://readme.so/)
• Special thanks to the open-source community
• Inspired by various movie recommendation tutorials

## 🔗 Links

• [Live Demo](https://movie-recommendation-project-with-jpm2.onrender.com/)
• [API Documentation](https://movie-recommendation-project-with-jpm2.onrender.com/docs)
• [GitHub Repository](https://readme.so/editor)
• [Report Bug](https://readme.so/editor)
• [Request Feature](https://readme.so/editor)

## 📊 Tech Stack

**Backend:** FastAPI, Python, Uvicorn, Pandas, NumPy, Scikit-learn  
**Frontend:** HTML5, CSS3, JavaScript, Bootstrap  
**Database:** Pickle files for model storage  
**Deployment:** Render (GitHub Integration)  
**Development:** Git, GitHub, VS Code  

---

*Made with ❤️ by [Anukul-Chandra]*
