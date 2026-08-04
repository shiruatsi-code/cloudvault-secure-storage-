# CloudVault

CloudVault is a secure cloud file storage platform that allows users to upload, organize, download, and share files through a modern web interface.

The project demonstrates full-stack software development, cloud storage integration, API security, role-based access control, encryption, automated testing, and continuous deployment.

## Project Status

CloudVault is currently under active development. Core features will be implemented incrementally through documented releases.

## Features

- Secure user registration and login
- JWT-based authentication
- Encrypted file uploads
- AWS S3 cloud storage
- Personal file dashboard
- Folder and file organization
- Private and shared file access
- Time-limited sharing links
- File download and deletion
- Upload size and file-type validation
- Audit logging
- User storage quotas
- Search and filtering
- Responsive user interface
- RESTful API
- Docker support
- Automated testing
- GitHub Actions CI/CD

## Technology Stack

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- JWT authentication

### Database

- PostgreSQL

### Cloud Storage

- Amazon S3

### DevOps

- Docker
- Docker Compose
- GitHub Actions

### Testing

- Pytest
- HTTPX
- React Testing Library

## Planned Architecture

```text
Browser
   |
React Frontend
   |
FastAPI REST API
   |
PostgreSQL Database
   |
Amazon S3 Storage
