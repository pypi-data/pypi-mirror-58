# Convolut-Tensorboard
```shell script
pip install convolut-tensorboard
```
![convolut](https://raw.githubusercontent.com/convolut/convolut-tensorboard/master/docs/img/logo.png)

# What you get
![what you get](https://raw.githubusercontent.com/convolut/convolut-tensorboard/master/docs/img/log_example.png)

# Usage
## Basic
```python
# ...
from convolut import Runner
from convolut_tensorboard import TensorboardLogger

# ...

(Runner(loaders=[train_loader, valid_loader], epochs=epochs)
    # ...
    .add(TensorboardLogger(folder="YOUR_FOLDER_FOR_TENSORBOARD_LOGS"))
    .start()
)
```

## Environment variables
* Telegram logger uses these envs for initialization

```.env
CONVOLUT_LOGGER_TENSORBOARD_FOLDER=logs/tensorboard # default
CONVOLUT_LOGGER_TENSORBOARD_MODE=basic # default
```

* Now you can use it that way:
```python
# ...
from convolut import Runner
from convolut_tensorboard import TensorboardLogger

# ...

(Runner(loaders=[train_loader, valid_loader], epochs=epochs)
    # ...
    .add(TensorboardLogger())
    .start()
)
```

## Tensorboard Server
```shell script
tensorboard --logdir=YOUR_FOLDER_FOR_TENSORBOARD_LOGS
```
