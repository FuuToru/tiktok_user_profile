Để thực hiện các bước trên với Python phiên bản <= 3.10, bạn có thể làm theo các bước sau:

### 1. Tạo virtual environment (venv)
```bash
python3.10 -m venv venv
```

### 2. Kích hoạt venv
- **Linux/MacOS:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Cài đặt các gói từ `requirements.txt`
```bash
pip install -r requirements.txt
```

### 4. Chạy file `start.py`
```bash
python start.py
```

Nếu gặp lỗi liên quan đến phiên bản Python hoặc các gói, hãy kiểm tra và đảm bảo rằng bạn đang sử