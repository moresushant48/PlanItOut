pyinstaller -n PlanItOut --onefile main.py --add-data Symbola.ttf;ttkbootstrap --add-data themes.json;ttkbootstrap --clean --uac-admin  
:: --noconsole
pyinstaller -n runner --onefile .\runner.py
:: --noconsole