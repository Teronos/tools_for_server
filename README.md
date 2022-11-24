# tools_for_server
That program creates as demon-process for linux,
which look at directories and removed olds files.

# Setup
_Nota bene:_ Default settings script you can find on `src/basic_struct.py`

##About parameters

The settings for the script should be located in the root folder of the project
on the file `./preference.json` and looks like this:

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

