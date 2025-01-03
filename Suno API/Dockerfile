# Use an ARM-compatible base image
FROM node:lts-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files to the container
COPY . .

# Set environment variable for SUNO_COOKIE (you'll need to supply this)
ENV SUNO_COOKIE=""

# Build the app
RUN npm run build

# Expose port
EXPOSE 3000

# Run the app
CMD ["npm", "run", "start"]

