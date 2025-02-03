from typing import List

from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

def cors_middleware (app: FastAPI):
  allowOriginList: List[str] = (
    # dev
    'http://localhost:8081',
    'http://localhost:8080',
    
    # test

    # prod
  )
  
  app.add_middleware(
    CORSMiddleware,
    allow_origins = allowOriginList,
    allow_credentials = True,
    allow_methods = ('GET', 'POST'),
    allow_headers = ('Content-Type', 'Authorization', 'Cookie', 'Origin', 'Console-Type'),
  )