#!/usr/bin/env python3
"""
Startup script to initialize the database with admin user
"""
import asyncio
import bcrypt
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from pathlib import Path
from datetime import datetime, timezone

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
db_name = os.environ.get('DB_NAME', 'constructmarket')

async def create_admin_user():
    """Create admin user if it doesn't exist"""
    
    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]
    
    admin_email = "admin@constructmarket.com"
    admin_password = "Admin123!"
    
    # Check if admin already exists
    existing_admin = await db.users.find_one({"email": admin_email})
    
    if existing_admin:
        print(f"⚠️  Admin user {admin_email} already exists.")
        # Update password to ensure it's correct
        hashed_password = bcrypt.hashpw(admin_password.encode('utf-8'), bcrypt.gensalt())
        await db.users.update_one(
            {"email": admin_email},
            {"$set": {
                "password_hash": hashed_password.decode('utf-8'),
                "role": "admin",
                "is_verified": True,
                "is_active": True,
                "updated_at": datetime.now(timezone.utc)
            }}
        )
        print(f"✅ Updated admin user: {admin_email}")
    else:
        # Create new admin user
        hashed_password = bcrypt.hashpw(admin_password.encode('utf-8'), bcrypt.gensalt())
        
        admin_doc = {
            "user_id": f"admin_{int(datetime.now(timezone.utc).timestamp())}",
            "email": admin_email,
            "password_hash": hashed_password.decode('utf-8'),
            "first_name": "Admin",
            "last_name": "User",
            "role": "admin",
            "phone": "+1234567890",
            "is_verified": True,
            "is_active": True,
            "profile_picture": None,
            "company_id": None,
            "two_factor_enabled": False,
            "two_factor_secret": None,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        }
        
        await db.users.insert_one(admin_doc)
        print(f"✅ Created admin user: {admin_email}")
    
    client.close()
    print("\n" + "="*60)
    print("ADMIN LOGIN CREDENTIALS:")
    print("="*60)
    print(f"Email:    {admin_email}")
    print(f"Password: {admin_password}")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(create_admin_user())
