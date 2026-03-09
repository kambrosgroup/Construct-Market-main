#!/usr/bin/env python3
"""
Script to create test user credentials in MongoDB
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
db_name = os.environ['DB_NAME']

async def create_test_users():
    """Create test users with predefined credentials"""

    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]

    # Test user credentials
    test_users = [
        {
            "email": "builder@test.com",
            "password": "Test123!",
            "first_name": "Test",
            "last_name": "Builder",
            "role": "builder",
            "phone": "+1234567890"
        },
        {
            "email": "provider@test.com",
            "password": "Test123!",
            "first_name": "Test",
            "last_name": "Provider",
            "role": "provider",
            "phone": "+1234567891"
        },
        {
            "email": "admin@constructmarket.com",
            "password": "Admin123!",
            "first_name": "Admin",
            "last_name": "User",
            "role": "admin",
            "phone": "+1234567892"
        }
    ]

    print("Creating test users in MongoDB...")
    print(f"Database: {db_name}")
    print(f"MongoDB URL: {mongo_url}")
    print("-" * 60)

    for user_data in test_users:
        email = user_data["email"]

        # Check if user already exists
        existing_user = await db.users.find_one({"email": email})

        if existing_user:
            print(f"⚠️  User {email} already exists. Updating password...")
            # Update existing user's password
            hashed_password = bcrypt.hashpw(user_data["password"].encode('utf-8'), bcrypt.gensalt())
            await db.users.update_one(
                {"email": email},
                {"$set": {
                    "password_hash": hashed_password.decode('utf-8'),
                    "updated_at": datetime.now(timezone.utc)
                }}
            )
            print(f"✅ Updated password for {email}")
        else:
            # Create new user
            hashed_password = bcrypt.hashpw(user_data["password"].encode('utf-8'), bcrypt.gensalt())

            user_doc = {
                "user_id": f"user_{email.split('@')[0]}_{int(datetime.now(timezone.utc).timestamp())}",
                "email": email,
                "password_hash": hashed_password.decode('utf-8'),
                "first_name": user_data["first_name"],
                "last_name": user_data["last_name"],
                "role": user_data["role"],
                "phone": user_data.get("phone"),
                "is_verified": True,  # Pre-verify test accounts
                "is_active": True,
                "profile_picture": None,
                "company_id": None,
                "two_factor_enabled": False,
                "two_factor_secret": None,
                "created_at": datetime.now(timezone.utc),
                "updated_at": datetime.now(timezone.utc)
            }

            await db.users.insert_one(user_doc)
            print(f"✅ Created new user: {email} (Role: {user_data['role']})")

    print("-" * 60)
    print("✅ Test users created successfully!")
    print("\nTest Credentials:")
    print("-" * 60)
    print("Builder Account:")
    print("  Email: builder@test.com")
    print("  Password: Test123!")
    print()
    print("Provider Account:")
    print("  Email: provider@test.com")
    print("  Password: Test123!")
    print()
    print("Admin Account:")
    print("  Email: admin@constructmarket.com")
    print("  Password: Admin123!")
    print("-" * 60)

    # Close connection
    client.close()

if __name__ == "__main__":
    asyncio.run(create_test_users())
