import os

DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://postgres:postgres@localhost/encryption-service')
