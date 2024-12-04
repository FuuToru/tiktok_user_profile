from api.main import Host_IP, Host_Port
import uvicorn

if __name__ == '__main__':
    uvicorn.run('api.main:app', host=Host_IP, port=Host_Port, reload=True, log_level="info")
