# ConstructMarket - Test Credentials

## 🔑 Test User Accounts

The following test accounts are available for development and testing:

---

### 👷 Builder Account
**Use this account to test builder/client features:**

- **Email:** `builder@test.com`
- **Password:** `Test123!`
- **Role:** Builder
- **Features:**
  - Create and post construction tasks
  - Review bids from providers
  - Award contracts
  - Manage work orders
  - Process payments
  - Rate providers

---

### 🔧 Provider Account
**Use this account to test provider/contractor features:**

- **Email:** `provider@test.com`
- **Password:** `Test123!`
- **Role:** Provider
- **Features:**
  - Browse marketplace tasks
  - Submit bids on tasks
  - Manage awarded contracts
  - Update work order progress
  - Submit invoices
  - View ratings and reviews

---

### 👨‍💼 Admin Account
**Use this account to test administrative features:**

- **Email:** `admin@constructmarket.com`
- **Password:** `Admin123!`
- **Role:** Admin
- **Features:**
  - User management
  - Company verification
  - System monitoring
  - Dispute resolution
  - Platform analytics
  - Configuration management

---

## 🔄 Reset/Recreate Test Users

If you need to reset the test user passwords or recreate the accounts, run:

```bash
python3 /Users/karlambrosius/Documents/Construct-Market-main/backend/create_test_users.py
```

This script will:
- Create new test users if they don't exist
- Update passwords if users already exist
- Ensure all test accounts are verified and active

---

## 🧪 Testing Workflow

### 1. Test Builder Flow
1. Login as `builder@test.com`
2. Create a new construction task
3. Post the task to marketplace
4. Wait for bids (or switch to provider account)
5. Review and award a bid
6. Monitor work progress
7. Release payment
8. Rate the provider

### 2. Test Provider Flow
1. Login as `provider@test.com`
2. Browse available tasks in marketplace
3. Submit a bid on a task
4. Wait for award (or switch to builder account)
5. Update work order status
6. Submit invoice
7. Receive payment
8. View rating received

### 3. Test Admin Flow
1. Login as `admin@constructmarket.com`
2. View all users and companies
3. Verify company registrations
4. Monitor platform activity
5. Handle disputes if any
6. View analytics and reports

---

## 🔐 Security Notes

**⚠️ IMPORTANT:**
- These are **TEST CREDENTIALS ONLY**
- Never use these credentials in production
- Change all passwords before deploying to production
- Test accounts have `is_verified: true` for convenience
- In production, users must verify their email addresses

---

## 📝 Additional Test Data

To fully test the application, you may want to create:
- Test companies for builder and provider
- Sample construction tasks
- Test bids and contracts
- Mock payment transactions
- Sample invoices and work orders

You can create these through the UI or by extending the `create_test_users.py` script.

---

## 🆘 Troubleshooting

### Cannot Login
- Verify MongoDB is running: `brew services list | grep mongodb`
- Check backend server is running: `curl http://localhost:8000/docs`
- Recreate test users: `python3 backend/create_test_users.py`

### Password Not Working
- Passwords are case-sensitive
- Ensure no extra spaces when copying
- Try recreating the users with the script

### User Not Found
- Run the create test users script
- Check MongoDB connection in backend logs: `tail -f /tmp/backend.log`

---

**Last Updated:** March 8, 2026
**Script Location:** `/Users/karlambrosius/Documents/Construct-Market-main/backend/create_test_users.py`
