# SWEEP.md - Project Commands & Configuration

## Build & Deployment Commands

### Localhost Deployment

#### Backend (FastAPI)
```bash
# Start backend server on localhost:8000
cd /Users/karlambrosius/Documents/Construct-Market-main/backend
uvicorn server:app --reload --port 8000

# Or use the helper script:
/Users/karlambrosius/Documents/Construct-Market-main/start-backend.sh
```

#### Frontend (React)
```bash
# Start frontend dev server on localhost:3000
cd /Users/karlambrosius/Documents/Construct-Market-main/frontend
npm start

# Or use the helper script:
/Users/karlambrosius/Documents/Construct-Market-main/start-frontend.sh
```

#### Build Frontend for Production
```bash
cd /Users/karlambrosius/Documents/Construct-Market-main/frontend
npm run build
```

### Prerequisites
- Python 3.12+ (Currently: 3.13.5)
- Node.js 20+ (Currently: v25.6.1)
- MongoDB (local or Atlas)

### Environment Files
- Backend: `/Users/karlambrosius/Documents/Construct-Market-main/backend/.env`
- Frontend: `/Users/karlambrosius/Documents/Construct-Market-main/frontend/.env`

## Testing

### Create Test Users
```bash
# Create/reset test user accounts in MongoDB
python3 /Users/karlambrosius/Documents/Construct-Market-main/backend/create_test_users.py
```

**Test Credentials:**
- Builder: builder@test.com / Test123!
- Provider: provider@test.com / Test123!
- Admin: admin@constructmarket.com / Admin123!

### Backend Tests
```bash
cd /Users/karlambrosius/Documents/Construct-Market-main/backend
pytest
```

### Frontend Tests
```bash
cd /Users/karlambrosius/Documents/Construct-Market-main/frontend
npm test
```

### Linting
```bash
# Frontend linting
cd /Users/karlambrosius/Documents/Construct-Market-main/frontend
npm run lint
```

## MongoDB Setup

### Option 1: Local MongoDB (macOS)
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

### Option 2: Docker
```bash
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

### Option 3: MongoDB Atlas
Update `backend/.env` with Atlas connection string:
```
MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
```

## Project Structure
- `/backend` - FastAPI backend server
- `/frontend` - React frontend application
- `/api` - Serverless API functions for Vercel
- `/tests` - Test files
- `/memory` - Project memory/context files

## Tech Stack
- **Backend**: FastAPI 0.110, MongoDB (Motor/PyMongo), JWT Auth
- **Frontend**: React 19, Tailwind CSS 3.4, shadcn/ui, React Router 7
- **Infrastructure**: Vercel (Frontend + Serverless API), MongoDB Atlas

## Deployment
- **Localhost**: See LOCALHOST_DEPLOYMENT.md
- **Production (Vercel)**: See DEPLOYMENT_VERCEL.md

## Code Style
- Backend: Python with type hints, FastAPI conventions
- Frontend: React functional components with hooks
- CSS: Tailwind CSS utility classes
