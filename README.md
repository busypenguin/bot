# Создание умного бота на основе сервиса Dialogflow


Проект создан с целью автоматизации ответов ботов на схожие вопросы.


### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```pip install -r requirements.txt```

### Переменные окружения

Создайте файл .env и запишите туда переменные окружения (TELEGRAM_BOT_TOKEN, TG_CHAT_ID, DVMN_API_TOKEN, GOOGLE_APPLICATION_CREDENTIALS, PROJECT_ID, VK_TOKEN) и их значения.


TELEGRAM_BOT_TOKEN вы получаете после создания телеграм-бота.
TG_CHAT_ID это путь к вашей группе в телеграме.
GOOGLE_APPLICATION_CREDENTIALS путь до места хранения файла ```application_default_credentials.json ```
PROJECT_ID - ID вашего Google проекта 
VK_TOKEN - токен вашей группы в ВК

Например:

```TELEGRAM_BOT_TOKEN = 087979801:A976578AqqKhDexAHU56781Hpaf3u879kijguPBKA```

### Запуск

Можете запустить код, написав в терминале:

```python3 tg_bot.py``` для запуска бота в телеграмме, или ```python3 vk_bot.py``` для запукска бота в ВК


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).










