#!/bin/bash

# Script de démarrage pour le projet Mokpokpo
# Ce script démarre le backend et le frontend

echo "?? Démarrage du projet Mokpokpo..."
echo ""

# Vérifier si Python est installé
if ! command -v python &> /dev/null; then
    echo "? Python n'est pas installé. Veuillez installer Python 3.8+"
    exit 1
fi

# Vérifier si Node.js est installé
if ! command -v node &> /dev/null; then
    echo "? Node.js n'est pas installé. Veuillez installer Node.js 18+"
    exit 1
fi

# Fonction pour démarrer le backend
start_backend() {
    echo "?? Démarrage du backend..."
    cd Backend
    
    # Vérifier si les dépendances sont installées
    if [ ! -d "venv" ]; then
        echo "?? Création de l'environnement virtuel..."
        python -m venv venv
    fi
    
    # Activer l'environnement virtuel
    source venv/bin/activate
    
    # Installer les dépendances
    pip install -r requirements.txt > /dev/null 2>&1
    
    # Démarrer le serveur
    echo "? Backend démarré sur http://localhost:8000"
    python -m uvicorn main:app --reload --port 8000 &
    BACKEND_PID=$!
    
    cd ..
}

# Fonction pour démarrer le frontend
start_frontend() {
    echo "?? Démarrage du frontend..."
    cd Frontend
    
    # Vérifier si les dépendances sont installées
    if [ ! -d "node_modules" ]; then
        echo "?? Installation des dépendances..."
        npm install
    fi
    
    # Démarrer le serveur de développement
    echo "? Frontend démarré sur http://localhost:3000"
    npm run dev &
    FRONTEND_PID=$!
    
    cd ..
}

# Fonction de nettoyage
cleanup() {
    echo ""
    echo "?? Arrêt des serveurs..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null
    fi
    if [ ! -z "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null
    fi
    echo "?? Au revoir!"
    exit 0
}

# Intercepter Ctrl+C
trap cleanup SIGINT SIGTERM

# Démarrer les serveurs
start_backend
sleep 3
start_frontend

echo ""
echo "======================================"
echo "? Projet Mokpokpo démarré avec succès!"
echo "======================================"
echo ""
echo "?? Backend API: http://localhost:8000"
echo "?? Documentation: http://localhost:8000/docs"
echo "?? Frontend: http://localhost:3000"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter les serveurs"
echo ""

# Attendre que les processus se terminent
wait
