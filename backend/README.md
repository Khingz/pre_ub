# Instal posgres to your local machine

# Setup posgres, add username and password

# Create a database called upbeat

# Install packages by running the command
pip install -r requirements.txt

# Add the following to env to get the app started
export DB_USERNAME
export DB_PASSWORD
export DB_HOST
export FLASK_SECRET_KEY

# Create a virtualenv to containerize the app
virtualenv <venv>
 source <venv>/Scripts/activate    <!-- for windows -->
 source <venv>/bin/activate        <!-- for linux -->

# On the root director start app by running
python run.py