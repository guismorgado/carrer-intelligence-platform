@echo off
echo Setting up Career Intelligence Platform backend...

python -m venv venv
call venv\Scripts\activate

pip install -r requirements.txt

echo.
echo Setup complete! To start the server:
echo   call venv\Scripts\activate
echo   uvicorn app:app --reload
echo.
echo API docs will be at: http://localhost:8000/docs
