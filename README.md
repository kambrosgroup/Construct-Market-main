# ConstructMarket

[![CI - Build & Test](https://github.com/kambrosgroup/Construct-Market-main/actions/workflows/ci.yml/badge.svg)](https://github.com/kambrosgroup/Construct-Market-main/actions/workflows/ci.yml)
[![CD - Deploy to Vercel](https://github.com/kambrosgroup/Construct-Market-main/actions/workflows/cd-vercel.yml/badge.svg)](https://github.com/kambrosgroup/Construct-Market-main/actions/workflows/cd-vercel.yml)
[![Code Quality](https://github.com/kambrosgroup/Construct-Market-main/actions/workflows/code-quality.yml/badge.svg)](https://github.com/kambrosgroup/Construct-Market-main/actions/workflows/code-quality.yml)

A full-stack construction marketplace platform connecting builders with trade providers.

## Features

- 🔐 **Authentication**: JWT + Google OAuth
- 👥 **Role-based Access**: Builder, Provider, Admin dashboards
- 📋 **Task Management**: Create, post, and manage construction tasks
- 💰 **Bidding System**: Providers can bid on tasks
- 📄 **Contract Generation**: Automated contract creation with e-signatures
- 💳 **Payment Processing**: Stripe integration for secure payments
- 💬 **Real-time Chat**: WebSocket-based messaging
- 📱 **Responsive Design**: Mobile-friendly UI with Tailwind CSS

## Tech Stack

### Frontend
- React 19
- Tailwind CSS 3.4
- shadcn/ui components
- React Router 7
- Axios for API calls

### Backend
- FastAPI 0.110
- MongoDB (Motor/PyMongo)
- JWT Authentication
- WebSocket support

### Infrastructure
- Vercel (Frontend + Serverless API)
- MongoDB Atlas
- GitHub Actions CI/CD

## Quick Start

### Prerequisites
- Node.js 20+
- Python 3.12+
- MongoDB (local or Atlas)

### Installation

```bash
# Clone the repository
git clone https://github.com/kambrosgroup/Construct-Market-main.git
cd Construct-Market-main

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend
npm install --legacy-peer-deps
```

### Environment Variables

Create `.env` files:

**backend/.env:**
```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=constructmarket
JWT_SECRET_KEY=your-secret-key
CORS_ORIGINS=http://localhost:3000
STRIPE_API_KEY=sk_test_...
RESEND_API_KEY=re_...
```

**frontend/.env:**
```env
REACT_APP_BACKEND_URL=http://localhost:8000
```

### Running Locally

```bash
# Start backend (from backend/)
uvicorn server:app --reload --port 8000

# Start frontend (from frontend/)
npm start
```

## Deployment

See [DEPLOYMENT_VERCEL.md](DEPLOYMENT_VERCEL.md) for detailed deployment instructions.

## GitHub Actions Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| CI - Build & Test | Push/PR to main/develop | Runs backend tests and frontend build |
| CD - Deploy to Vercel | Push to main | Deploys production to Vercel |
| Code Quality | Push/PR to main/develop | Runs linting and security scans |

### Required Secrets

Configure these in your GitHub repository settings:

- `VERCEL_TOKEN` - Vercel API token
- `VERCEL_ORG_ID` - Vercel organization ID
- `VERCEL_PROJECT_ID` - Vercel project ID
- `MONGO_URL` - MongoDB connection string
- `JWT_SECRET_KEY` - JWT signing key
- `CORS_ORIGINS` - Allowed CORS origins

## License

[MIT](LICENSE)

