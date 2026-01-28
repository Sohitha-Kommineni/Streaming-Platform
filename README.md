# Streaming Platform

A Django-based streaming platform demo that showcases movie listings, categories,
and detail pages. It is designed as a clean starter project with server-rendered
templates, static assets, and local in-memory data for quick setup.

### Structure (Top-Level)
```
Streaming Platform/
├─ manage.py
├─ db.sqlite3
├─ movie_streaming/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ movies/
│  ├─ data.py
│  ├─ urls.py
│  └─ views.py
├─ templates/
│  ├─ base.html
│  ├─ home.html
│  ├─ movies.html
│  └─ movie_detail.html
└─ static/
   ├─ css/
   │  └─ styles.css
   └─ images/
      ├─ banners/
      ├─ cast/
      └─ posters/
```

## Features
- Home page with featured content
- Movie listings and detail pages
- Static assets for posters and banners
- Clean HTML templates and custom CSS

## Tech Stack
- Python 3.x
- Django
- SQLite (local development)

## Screens
- Home page
- Movies list
- Movie detail

## How It Works
- Routes are defined in `movies/urls.py` and included in the project `urls.py`.
- Views render templates with data from `movies/data.py`.
- Static assets are served from the `static/` directory during development.

## Getting Started (Local)
1. Create and activate a virtual environment (recommended).
2. Install Django:
   ```bash
   pip install django
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the server:
   ```bash
   python manage.py runserver
   ```
5. Open in browser:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure
- `movie_streaming/` - Django project settings and URLs
- `movies/` - App logic: views, routes, and local movie data
- `templates/` - HTML templates
- `static/` - CSS and images

## Data
Movie data is stored locally in `movies/data.py` for simplicity. You can replace
this with a database model later if needed.

## Git Notes
- `db.sqlite3` is ignored by git.
- Add a `.env` file if you introduce secrets.

## License
MIT
