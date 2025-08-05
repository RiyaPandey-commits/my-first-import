FROM node:alpine

# Install http-server globally
RUN npm install -g http-server

# Set working directory
WORKDIR /app

# Copy HTML, CSS, images, etc.
COPY . .

# Expose default http-server port
EXPOSE 8080

# Run http-server
# CMD ["http-server", "-p", "8080"]
