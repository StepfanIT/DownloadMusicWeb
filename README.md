# 🎶 DownloadMusicWeb

**DownloadMusicWeb** — це Django-додаток, який дозволяє завантажувати музику з онлайн-ресурсів (YouTube та інші) через простий веб-інтерфейс.

## 🧰 Технології

- **Python 3.10+**
- **Django 4.x**
- **yt-dlp** — інструмент для завантаження аудіо/відео
- **HTML/CSS**
- **JavaScript** — для обробки подій на клієнтській стороні

## ⚙️ Встановлення

1. **Клонування репозиторію:**

    ```bash
    git clone https://github.com/StepfanIT/DownloadMusicWeb.git
    cd DownloadMusicWeb
    ```

2. **Створення та активація віртуального середовища:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. **Встановлення залежностей:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Запуск сервера:**

    ```bash
    python manage.py runserver
    ```

5. **Використання:**

    Відкрий у браузері [http://127.0.0.1:8000](http://127.0.0.1:8000) та встав URL треку для завантаження.

## 🔍 Можливості

- Завантаження музики з популярних онлайн-ресурсів
- Простий веб-інтерфейс
- Підтримка форматів: `.mp3`, `.m4a`, `.wav`