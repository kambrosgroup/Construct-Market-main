# Vercel Deployment Guide

This guide will help you deploy the ConstructMarket application to Vercel.

## Prerequisites

1. [Vercel Account](https://vercel.com/signup)
2. [Vercel CLI](https://vercel.com/docs/cli) (optional but recommended)
3. MongoDB Atlas cluster (or other MongoDB provider)
4. Stripe account (for payments)
5. Resend account (for emails)

## Environment Variables

Set the following environment variables in your Vercel project dashboard:

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGO_URL` | MongoDB connection string | `mongodb+srv://user:pass@cluster.mongodb.net` |
| `DB_NAME` | Database name | `constructmarket` |
| `JWT_SECRET_KEY` | Secret key for JWT tokens | (generate a random string) |
| `CORS_ORIGINS` | Allowed CORS origins | `https://yourdomain.vercel.app` |

### Optional Variables

| Variable | Description |
|----------|-------------|
| `STRIPE_API_KEY` | Stripe API key for payments |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook secret |
| `RESEND_API_KEY` | Resend API key for emails |

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Fork/Clone this repository** to your GitHub account

2. **Create new project on Vercel:**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New Project"
   - Import your GitHub repository

3. **Configure Project:**
   - Framework Preset: `Create React App`
   - Build Command: `cd frontend && yarn install && yarn build`
   - Output Directory: `frontend/build`
   - Install Command: `pip install -r api/requirements.txt`

4. **Set Environment Variables:**
   - Add all required environment variables listed above

5. **Deploy:**
   - Click "Deploy"

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   vercel
   ```

4. **Set Environment Variables:**
   ```bash
   vercel env add MONGO_URL
   vercel env add JWT_SECRET_KEY
   # Add other variables...
   ```

5. **Redeploy:**
   ```bash
   vercel --prod
   ```

## Project Structure for Vercel

```
├── api/
│   ├── index.py          # Serverless function entry point
│   └── requirements.txt  # Python dependencies
├── backend/
│   └── server.py         # FastAPI application
├── frontend/
│   ├── public/
│   ├── src/
│   ├── build/            # Build output
│   └── package.json
├── vercel.json           # Vercel configuration
└── README.md
```

## Important Notes

### API Routes

- All API routes are prefixed with `/api/`
- The FastAPI application is served as a serverless function
- WebSocket support is limited in serverless environment

### File Uploads

- File uploads are stored temporarily in `/tmp` directory
- For production, consider using cloud storage (S3, Cloudinary, etc.)

### WebSocket Chat

WebSocket chat may not work in the serverless environment due to stateless nature. Consider:
- Using Pusher or similar service
- Implementing polling fallback
- Using Vercel's Edge Network (experimental)

### Database

- Use MongoDB Atlas or similar managed MongoDB service
- Ensure your MongoDB instance allows connections from Vercel's IP range

## Troubleshooting

### Build Errors

1. **Python dependencies failing:**
   - Check `api/requirements.txt` for compatibility
   - Some packages with C extensions may not work on Vercel

2. **Frontend build failing:**
   - Ensure Node.js version is compatible (18.x recommended)
   - Check for missing environment variables

### Runtime Errors

1. **API returning 404:**
   - Check `vercel.json` routes configuration
   - Ensure `api/index.py` exists and is properly formatted

2. **Database connection failing:**
   - Verify `MONGO_URL` environment variable
   - Check MongoDB Atlas network access settings

3. **CORS errors:**
   - Update `CORS_ORIGINS` environment variable
   - Check browser console for specific error messages

## Post-Deployment Checklist

- [ ] Health check endpoint works: `GET /api/health`
- [ ] API documentation available: `GET /api/docs` (if enabled)
- [ ] Frontend loads without errors
- [ ] User authentication works
- [ ] Database connections are stable
- [ ] File uploads work (or cloud storage configured)
- [ ] Stripe webhooks are configured (if using payments)

## Support

For issues specific to Vercel deployment, check:
- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/functions/runtimes/python)
- Project Issues on GitHub
