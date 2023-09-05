echo "Installing packages.."
pip install -r requirements.txt
echo "✅ Packages installed successfully"

echo "Running migrations..."
python manage.py migrate
python manage.py collectstatic --no-input
