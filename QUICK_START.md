# ConstructMarket - Quick Start Guide

## 🚀 Your Application is Running!

### ✅ Current Status
- **Backend:** Running on http://localhost:8000
- **Frontend:** Running on http://localhost:3000
- **Database:** MongoDB running on port 27017
- **Test Users:** Created and ready to use

---

## 🌐 Access the Application

### Main Application
Open your browser and navigate to:
```
http://localhost:3000
```

### API Documentation
Interactive API documentation (Swagger UI):
```
http://localhost:8000/docs
```

---

## 🔑 Login with Test Accounts

### Builder Account
```
Email: builder@test.com
Password: Test123!
```
**Features:** Create tasks, review bids, award contracts, manage payments

### Provider Account
```
Email: provider@test.com
Password: Test123!
```
**Features:** Browse tasks, submit bids, manage work orders, submit invoices

### Admin Account
```
Email: admin@constructmarket.com
Password: Admin123!
```
**Features:** User management, company verification, system monitoring

---

## 📊 Server Information

### Backend Server
- **PID:** 88354
- **Port:** 8000
- **Logs:** `/tmp/backend.log`
- **View logs:** `tail -f /tmp/backend.log`

### Frontend Server
- **PID:** 88447
- **Port:** 3000
- **Logs:** `/tmp/frontend.log`
- **View logs:** `tail -f /tmp/frontend.log`

### MongoDB
- **Port:** 27017
- **Database:** constructmarket
- **Status:** `brew services list | grep mongodb`

---

## 🛑 Stop/Start Servers

### Stop All Services
```bash
# Stop backend
kill 88354

# Stop frontend
kill 88447

# Stop MongoDB
brew services stop mongodb-community
```

### Start All Services
```bash
# Start MongoDB
brew services start mongodb-community

# Start backend
/Users/karlambrosius/Documents/Construct-Market-main/start-backend.sh

# Start frontend (in a new terminal)
/Users/karlambrosius/Documents/Construct-Market-main/start-frontend.sh
```

---

## 📚 Documentation

- **DEPLOYMENT_STATUS.md** - Current deployment status and details
- **LOCALHOST_DEPLOYMENT.md** - Complete deployment guide
- **TEST_CREDENTIALS.md** - Test account details and usage
- **SWEEP.md** - Quick reference commands
- **README.md** - Project overview

---

## 🧪 Testing Workflow

1. **Open the app:** http://localhost:3000
2. **Login** with one of the test accounts
3. **Explore features** based on your role:
   - **Builder:** Create a task → Post to marketplace
   - **Provider:** Browse tasks → Submit a bid
   - **Admin:** View users → Verify companies

---

## 🔄 Reset Test Users

If you need to reset passwords or recreate test accounts:
```bash
python3 /Users/karlambrosius/Documents/Construct-Market-main/backend/create_test_users.py
```

---

## 🆘 Troubleshooting

### Application won't load
1. Check if servers are running: `lsof -i :8000 -i :3000`
2. Check backend logs: `tail -f /tmp/backend.log`
3. Check frontend logs: `tail -f /tmp/frontend.log`

### Cannot login
1. Verify MongoDB is running: `brew services list | grep mongodb`
2. Recreate test users: `python3 backend/create_test_users.py`
3. Check backend API: `curl http://localhost:8000/docs`

### Port already in use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

---

## 🎯 Next Steps

1. ✅ Login to http://localhost:3000
2. ✅ Test the application features
3. ✅ Explore the API at http://localhost:8000/docs
4. 📝 Configure Stripe/Resend API keys (optional)
5. 🚀 Start building!

---

**Happy Building! 🏗️**
