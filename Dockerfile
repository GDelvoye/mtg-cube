# Utilisation d'une image Python légère
FROM python:3.11-slim

# Définition du répertoire de travail à /app/back
WORKDIR /app/back

# Copier le backend tel quel (y compris requirements.txt)
COPY back/ /app/back/

# Copier le dossier data
COPY data/ /app/data/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask
EXPOSE 5000

# Lancer Gunicorn en considérant /app/back comme racine
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

