from fastapi import FastAPI

from router import router as all_router

import uvicorn

app = FastAPI()

app.include_router(all_router)

if __name__ == '__main__':  
  uvicorn.run(
    'app:app',
    host = "localhost",
    port = 9001,
    reload = True,
    log_level = "info"
  )
