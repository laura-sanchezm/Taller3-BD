from fastapi import FASTAPI;
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from datetime import datetime
import os

app = FASTAPI()
app.add_middleware(
    CORSMiddleware, 
     allow_origins=["*"], 
     allow_methods=["*"], 
     allow_headers=["*"])

client = MongoClient(os.environ("MONGO_URI"))

client = MongoClient(os.environ("MONGO_URI"))
