# MongoDB Atlas Setup for Render Deployment

## Issue: SSL Handshake Failed

The Render deployment cannot connect to MongoDB Atlas due to IP whitelist restrictions.

## Solution

### Step 1: Add Render IP to MongoDB Atlas Network Access

1. Go to [MongoDB Atlas](https://cloud.mongodb.com)
2. Select your project
3. Go to **Network Access** (left sidebar)
4. Click **Add IP Address**
5. Click **Allow Access from Anywhere** (0.0.0.0/0) 
   - OR add Render's specific IP ranges
6. Click **Confirm**

### Step 2: Alternative - Use MongoDB Data API

If IP whitelisting doesn't work, you can use MongoDB's Data API:

1. In MongoDB Atlas, go to **Data API** (left sidebar)
2. Enable the Data API
3. Create an API key
4. Update the connection to use the Data API

## Current Connection String

```
mongodb+srv://kambros098_db_user:jr8CqzdzrZnm6znA@cluster0.vp0ienm.mongodb.net/constructmarket?retryWrites=true&w=majority
```

## Test Credentials

- **Admin Email**: admin@constructmarket.com
- **Admin Password**: Admin123!

Once the IP is whitelisted, the admin user will be created automatically on the next deployment.
