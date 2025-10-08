# Research AI API

Django REST API that uses OpenAI to search for peer-reviewed research articles and provide summaries.

## Features

- Search for high-quality, peer-reviewed research articles
- Get article titles and links
- Receive brief 200-word summaries
- REST API endpoint for easy integration

## Prerequisites

- Docker and Docker Compose
- OpenAI API key

## Setup

1. Clone the repository

2. Create `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. Build and run with Docker:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /api/ask/

Search for a research article and get a summary.

**Request:**
```json
{
  "prompt": "machine learning in healthcare"
}
```

**Response:**
```json
{
  "first_answer": "Article title and link",
  "second_answer": "200-word summary of the article"
}
```

**Example using curl:**
```bash
curl -X POST http://localhost:8000/api/ask/ \
  -H "Content-Type: application/json" \
  -d '{"prompt": "quantum computing applications"}'
```

## Development

### Local Setup (without Docker)

1. Create virtual environment:
```bash
python -m venv .venv
```

2. Activate virtual environment:
- Windows: `.venv\Scripts\activate`
- Linux/Mac: `source .venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file with your OpenAI API key

5. Run migrations:
```bash
python manage.py migrate
```

6. Run development server:
```bash
python manage.py runserver
```

## Project Structure

```
research_ai/
├── api/                    # API application
│   ├── views.py           # API endpoints
│   └── urls.py            # API routes
├── research_ai/           # Django project settings
│   ├── settings.py        # Project configuration
│   └── urls.py            # Main URL configuration
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## Technologies

- Django 5.2.7
- Django REST Framework 3.15.2
- OpenAI API
- Python 3.11
- Docker

