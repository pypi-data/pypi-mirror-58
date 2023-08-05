# AutomaticBehaviorAnalysis

## Установка
### pip
Клиент (в режиме работы с кеша)
Для работы с кеша нужно разместить видео и файл кэша в одну папку

Установка пакета:

`pip install --user automatic-behavior-analysis`

Обновление пакета:

`pip install --upgrade --user automatic-behavior-analysis`

Запуск клиента:

`aba-client`

Перед первым запуском после установки надо перейти в папку
`~/.local/lib/python3.7/site-packages/client2/`
 И создать копию файла config.1.json с именем config.json

ВНИМАНИЕ!
Для корректной работы в пути к пакетам не должно содержаться кирилических символов .

## Требования

* Python 3
* TensorFlow
* [Tensorflow Object Detection API](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)
* Keras
* numpy
* PIL
* tkinter
* appdirs
* openCV
* websocket

### Client2

* Python 3
* openCV
* appdirs

## Сборка контейнера с сервером

### Контейнер для разработки

В контейнере для разработки отсутствуют файлы и модели с целью минификации образа и повышения удобства работы.

Контейнер собирается следующей командой:

```bash
# Для контейнера с поддержкой GPU
docker build -t registry.gitlab.com/digiratory/automatic-behavior-analysis/dev-gpu .
# Для контейнера с поддержкой только CPU
docker build  -f Dockerfile.dev.cpu -t registry.gitlab.com/digiratory/automatic-behavior-analysis/dev-cpu .
```

Для работы нет необходимости пересобирать контейнер и можно забрать собранный с репозитория с помощью следующих команд:

```bash
docker login registry.gitlab.com
# Для запуска контейнера с поддержкой GPU
docker run --runtime=nvidia -it -v <workspace>:/home/user/ -p 1217:1217 registry.gitlab.com/digiratory/automatic-behavior-analysis/dev-gpu:latest

# Для запуска контейнера с поддержкой CPU
docker run -it -v <workspace>:/home/user/ -p 1217:1217 registry.gitlab.com/digiratory/automatic-behavior-analysis/dev-cpu:latest
```

Для CPU-only:

```bash
docker login registry.gitlab.com
docker run -it -v <workspace>:/home/user/ -p 1217:1217 registry.gitlab.com/digiratory/automatic-behavior-analysis/dev-cpu:latest
```

Если на машине отсутствует gpu, то ключ `--runtime=nvidia` указывать не надо.

ВНИМАНИЕ! Контейнер для разработки не включает в свой состав исходный код, модели и прочее.

## Запуск приложений

Порядок запуска:

1. Серверная часть
2. Клиентская часть

Порядок выключения:

1. Клиентская часть
2. Серверная часть

### Сервер

Для запуска серверной части необходимо выполнить ./server.py

```bash
python3 ./server.py
```

Аргументы команды:
[ip= ] — Ip адрес для прослушки (По умолчанию 172.0.0.1 )
[port= ] — Порт сервера (По умолчанию 1217)

### Клиентская часть (GUI)

Для запуска серверной части необходимо выполнить ./client_gui.py

```bash
python3 ./client_gui.py
```

Аргументы команды:
[ip= ] — Ip адрес сервера (По умолчанию 172.0.0.1 )
[port= ] — Порт сервера (По умолчанию 1217)
