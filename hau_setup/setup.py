import os

os.system(f'pip install -r hau_setup\\requirements.txt')
os.system(f'pip install --upgrade --no-cache-dir gdown')

os.system('pyinstaller --onefile hau_setup\\run.py --name=App')

os.rename("dist\\App.exe", "App.exe")

