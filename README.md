# tools_for_server
That program creates as demon-process for linux,
which look at directories and removed olds files.


_Nota bene:_ Default settings script you can find in `src/basic_struct.py`

__About parameters__

The settings for the script should be located in the root folder of the project
in the file `./preference.json` and looks like this:

```json
{
  "LIST_OF_PATH": ["./dir_1", "./dir_2"],
  "FREQUENCY_RUN": {
    "second": 0,
    "minuet": 0,
    "hour": 0,
    "day": 0,
    "week": 2,
    "month": 0,
    "year": 0
  },
  "LIFE_TIME": {
    "second": 0,
    "minuet": 0,
    "hour": 0,
    "day": 5,
    "week": 0,
    "month": 1,
    "year": 0
  }
}
```

**LIST_OF_PATH:** list of paths to all directories to tracking the status of files.

**FREQUENCY_RUN:** frequency of script running.

**LIFE_TIME:** amount time after which files are deleted from directories.

#Pre-setup

if pipenv is not installed, then you need to run the command

```bash
pip install pipenv
```
# Setup

Run the next commands in terminal
```bash
cd /opt/ && git clone https://github.com/Teronos/tools_for_server.git
cd tools_for_server && pipenv sync
```

Then create `./preference.json` so example in __About parameters__.

Now you have to create a configuration file for systemd.service

```bash
sudo nano /lib/systemd/system/deliter.service
```
 and use next configuration
```
[Unit]
Description=demon deliter setvice

[Service]
Type=idle
Restart=on-failure
User=root
ExecStart=/bin/bash -c 'cd /opt/tools_for_server/ && pipenv run python main.py'

[Install]
WantedBy=multi-user.target
```
and running command

```bash
sudo chmod 644 /lib/systemd/system/deliter.service
sudo systemctl daemon-reload
sudo systemctl enable deliter.service
```
In conclusion, now you're using  script as systemd.service.
