    python -m venv venv
    venv\Scripts\activate.bat
    
    python.exe -m pip install --upgrade pip

    pip install fastapi
    pip install "uvicorn[standard]"
    pip install jinja2
    pip install python-multipart

    pip install sqlalchemy
    pip install databases[aiosqlite]

    uvicorn main:app --reload