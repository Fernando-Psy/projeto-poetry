#!/bin/bash

# Deploy script for bookstore application
set -e

# Configuration
APP_NAME="bookstore"
DOCKER_IMAGE="${DOCKER_USERNAME}/${APP_NAME}:${GITHUB_SHA}"
CONTAINER_NAME="${APP_NAME}_web"
NETWORK_NAME="${APP_NAME}_network"

echo "🚀 Starting deployment process..."

# Pull latest image
echo "📦 Pulling Docker image: ${DOCKER_IMAGE}"
docker pull ${DOCKER_IMAGE}

# Stop and remove existing container
echo "🛑 Stopping existing container..."
docker stop ${CONTAINER_NAME} || true
docker rm ${CONTAINER_NAME} || true

# Create network if it doesn't exist
docker network create ${NETWORK_NAME} || true

# Run database migrations
echo "🗄️ Running database migrations..."
docker run --rm \
    --network ${NETWORK_NAME} \
    -e DATABASE_URL=${DATABASE_URL} \
    -e SECRET_KEY=${SECRET_KEY} \
    ${DOCKER_IMAGE} \
    python manage.py migrate

# Collect static files
echo "📂 Collecting static files..."
docker run --rm \
    --network ${NETWORK_NAME} \
    -e DATABASE_URL=${DATABASE_URL} \
    -e SECRET_KEY=${SECRET_KEY} \
    -v ${APP_NAME}_static:/app/staticfiles \
    ${DOCKER_IMAGE} \
    python manage.py collectstatic --noinput

# Start new container
echo "🔥 Starting new container..."
docker run -d \
    --name ${CONTAINER_NAME} \
    --network ${NETWORK_NAME} \
    --restart unless-stopped \
    -p 8000:8000 \
    -e DATABASE_URL=${DATABASE_URL} \
    -e SECRET_KEY=${SECRET_KEY} \
    -e DEBUG=False \
    -v ${APP_NAME}_static:/app/staticfiles \
    ${DOCKER_IMAGE}

# Health check
echo "🏥 Performing health check..."
sleep 10

if curl -f http://localhost:8000/admin/ > /dev/null 2>&1; then
    echo "✅ Deployment successful!"
else
    echo "❌ Health check failed!"
    docker logs ${CONTAINER_NAME}
    exit 1
fi

# Clean up old images
echo "🧹 Cleaning up old images..."
docker image prune -f

echo "🎉 Deployment completed successfully!"