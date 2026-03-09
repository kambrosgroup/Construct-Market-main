# ConstructMarket - Localhost Deployment Guide

## Prerequisites Installed ✅
- ✅ Python 3.13.5
- ✅ Node.js v25.6.1
- ✅ npm 11.9.0
- ✅ FastAPI
- ✅ uvicorn

## ⚠️ MongoDB Required
MongoDB is **NOT** currently installed on your system. You have three options:

### Option 1: Install MongoDB Locally (Recommended for Development)
```bash
# macOS with Homebrew
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

### Option 2: Use MongoDB Atlas (Cloud - Free Tier Available)
1. Sign up at https://www.mongodb.com/cloud/atlas
2. Create a free cluster
3. Get your connection string
4. Update `backend/.env` with your Atlas connection string:
   ```
   MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/
   ```

### Option 3: Use Docker
```bash
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

## Environment Files Created ✅
The following environment files have been created:

### Backend (.env)
Location: `/Users/karlambrosius/Documents/Construct-Market-main/backend/.env`
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=constructmarket
JWT_SECRET_KEY=your-local-dev-secret-key-change-in-production
CORS_ORIGINS=http://localhost:3000
STRIPE_API_KEY=sk_test_your_stripe_key_here
RESEND_API_KEY=re_your_resend_key_here
```

### Frontend (.env)
Location: `/Users/karlambrosius/Documents/Construct-Market-main/frontend/.env`
```env
REACT_APP_BACKEND_URL=http://localhost:8000
```

## Quick Start - Deploy on Localhost

### Step 1: Install Frontend Dependencies (if needed)
```bash
cd /Users/karlambrosius/Documents/Construct-Market-main/frontend
npm install --legacy-peer-deps
```

### Step 2: Start Backend Server
Open a new terminal window and run:
```bash
/Users/karlambrosius/Documents/Construct-Market-main/start-backend.sh
```
Or manually:
```bash
cd /Users/karlambrosius/Documents/Construct-Market-main/backend
uvicorn server:app --reload --port 8000
```

The backend will be available at:
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Interactive API**: http://localhost:8000/redoc

### Step 3: Start Frontend Server
Open another terminal window and run:
```bash
/Users/karlambrosius/Documents/Construct-Market-main/start-frontend.sh
```
Or manually:
```bash
cd /Users/karlambrosius/Documents/Construct-Market-main/frontend
npm start
```

The frontend will be available at:
- **Application**: http://localhost:3000

## Troubleshooting

### Backend won't start - MongoDB connection error
**Error**: `pymongo.errors.ServerSelectionTimeoutError`

**Solution**: Install and start MongoDB (see options above)

### Frontend won't start - Dependencies missing
**Error**: Module not found errors

**Solution**:
```bash
cd /Users/karlambrosius/Documents/Construct-Market-main/frontend
npm install --legacy-peer-deps
```

### Port already in use
**Error**: `Address already in use`

**Solution**:
```bash
# Find and kill process on port 8000 (backend)
lsof -ti:8000 | xargs kill -9

# Find and kill process on port 3000 (frontend)
lsof -ti:3000 | xargs kill -9
```

## Development Workflow

1. **Backend Development**:
   - Edit files in `/backend/`
   - Server auto-reloads with `--reload` flag
   - Test API at http://localhost:8000/docs

2. **Frontend Development**:
   - Edit files in `/frontend/src/`
   - Browser auto-refreshes on save
   - View app at http://localhost:3000

3. **Database**:
   - MongoDB running on port 27017
   - Database name: `constructmarket`
   - Use MongoDB Compass for GUI: mongodb://localhost:27017

## Next Steps

1. ✅ Environment files created
2. ⚠️ Install MongoDB (choose one option above)
3. 📦 Ensure frontend dependencies are installed
4. 🚀 Start backend server
5. 🚀 Start frontend server
6. 🌐 Open http://localhost:3000 in your browser

## Additional Configuration

### Update API Keys (Optional for basic testing)
- **Stripe**: Get test keys from https://dashboard.stripe.com/test/apikeys
- **Resend**: Get API key from https://resend.com/api-keys
- **JWT Secret**: Generate a secure random string for production

### Production Deployment
For production deployment to Vercel, see [DEPLOYMENT_VERCEL.md](DEPLOYMENT_VERCEL.md)
