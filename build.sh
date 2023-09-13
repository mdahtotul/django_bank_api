echo "🚀 Installing packages..."
pip install -r requirements.txt
echo "✅ Packages installed successfully"

echo "🚀 Running migrations..."
python3 manage.py migrate
python3 manage.py collectstatic --no-input
