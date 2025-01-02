# Utiliser une image de base officielle de Python
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application va s'exécuter
EXPOSE 8000

# Définir la commande pour exécuter l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]