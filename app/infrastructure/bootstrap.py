# app/infrastructure/bootstrap.py

import importlib
import pkgutil
import app.application.handlers as handlers_path

def bootstrap_app():
    """به صورت خودکار تمام هندلرها را پیدا و لود می‌کند"""
    for _, name, is_pkg in pkgutil.walk_packages(handlers_path.__path__, handlers_path.__name__ + "."):
        if not is_pkg:
            importlib.import_module(name)
    
    print("🚀 All handlers registered successfully via Registry Pattern.")
