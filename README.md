# Streaming Platform

A Django-based streaming platform demo that shows movie listings and detail pages
with a simple UI and local data.

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
