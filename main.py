import uvicorn
from fastapi import FastAPI
from routers import payment_router
from settings.secrets import Secret

app = FastAPI()

app.include_router(payment_router)
host = Secret().host_creds()


if __name__ == "__main__":
    uvicorn.run(app, host=host.get("host"), port=int(host.get("port")))
