TITLE Nova manga botu kurulumu

goto check

:check
where python.exe
if errorlevel 1 goto python_not_found
if errorlevel 0 goto python_found

:python_not_found
echo "Python bulunamadı."
echo "Python kurulumu gerkiyor. Lütfen 'add to PATH seçeneğini açıp kurulumu başlatın.'"
start python/python-3.10.5-amd64.exe
goto check

:python_found
echo "Python bulundu."
pip install discord
pip install bs4
pip install requests
pip install feedparser
pip install python-dotenv
echo "Kurulum başarılı. Lütfen 'bot.py' dosyasını çalıştırın."

