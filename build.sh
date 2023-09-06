echo "🚀 Installing packages..."
pip install -r requirements.txt
echo "✅ Packages installed successfully"

echo "🚀 Running migrations..."
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations --no-input
python3 manage.py migrate
