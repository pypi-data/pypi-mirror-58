# Convolut-Telegram
```shell script
pip install convolut-telegram
```
![convolut](https://raw.githubusercontent.com/convolut/convolut-telegram/master/docs/img/logo.png)

# What you get
![what you get](https://raw.githubusercontent.com/convolut/convolut-telegram/master/docs/img/log_example.png)

# Usage
## Basic
```python
# ...
from convolut import Runner
from convolut_telegram import TelegramLogger

# ...

(Runner(loaders=[train_loader, valid_loader], epochs=epochs)
    # ...
    .add(TelegramLogger(token="YOUR_BOT_TOKEN_HERE", chat_id="YOUR_CHAT_ID_HERE"))
    .start()
)
```

## Environment variables
* Telegram logger uses these envs for initialization

```.env
CONVOLUT_LOGGER_TELEGRAM_TOKEN=YOUR_BOT_TOKEN_HERE
CONVOLUT_LOGGER_TELEGRAM_CHAT_ID=YOUR_CHAT_ID_HERE
CONVOLUT_LOGGER_TELEGRAM_MODE=basic # default value
CONVOLUT_LOGGER_TELEGRAM_PROXY=https://api.telegram.org # default value
```

* Now you can use it that way:
```python
# ...
from convolut import Runner
from convolut_telegram import TelegramLogger

# ...

(Runner(loaders=[train_loader, valid_loader], epochs=epochs)
    # ...
    .add(TelegramLogger())
    .start()
)
```

