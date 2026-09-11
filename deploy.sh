#!/usr/bin/env bash
REMOTE_USER="u283966854"
REMOTE_HOST="77.37.91.204"
REMOTE_PORT="65002"
REMOTE_DIR="/home/u283966854/domains/stephaniayyilmar.com.mx/public_html/"

# Sincronizar hacia Hostinger excluyendo entornos locales/IDE
rsync -avz --delete \
  --exclude '.git/' \
  --exclude '.gitignore' \
  --exclude '.obsidian/' \
  --exclude '.claude/' \
  --exclude '.agents/' \
  --exclude '.opencode/' \
  --exclude '.copilot/' \
  --exclude 'nbproject/' \
  --exclude 'deploy.sh' \
  -e "ssh -p $REMOTE_PORT" ./ "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DIR"

echo "Despliegue completado con éxito: $(date)"
