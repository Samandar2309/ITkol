#!/usr/bin/env bash
# Build script for Render.com

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running Django migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build complete."
