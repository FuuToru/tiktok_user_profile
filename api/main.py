
# FastAPI APP
import uvicorn
from fastapi import FastAPI
from api.router import router as api_router

# OS
import os

# YAML
import yaml

# Load Config

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)


Host_IP = config['API']['Host_IP']
Host_Port = config['API']['Host_Port']


version = config['API']['Version']
update_time = config['API']['Update_Time']
environment = config['API']['Environment']

docs_url = config['API']['Docs_URL']

app = FastAPI(
    title="TikTok Core Search API",
    description="TikTok Core Search API",
    version=version,
    docs_url=docs_url, 
)

# API router
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(app, host=Host_IP, port=Host_Port)
