import time
import os

from src.basic_struct import Preference


def check_directory(path: str):
    def filter_elder(path_to_file: str) -> bool:
        return time.time() - os.stat(path_to_file).st_mtime > config.life_time

    def rm_files(path_file) -> int:
        if os.path.isfile(path_file):
            os.remove(path_file)
            return 1
        return 0
    try:
        paths_files_from_directory = list(map(lambda x: f"{path}/{x}", os.listdir(path)))
        count = sum(list(map(rm_files, list(filter(filter_elder, paths_files_from_directory)))))
        print(f"remove {count} files")
    except FileNotFoundError:
        print(f"No such file or directory: {path}")


def run():
    while True:
        list(map(check_directory, config.LIST_OF_PATH))
        time.sleep(config.FREQUENCY_RUN)


if __name__ == '__main__':
    config = Preference.load_preference_from()
    if config.LIST_OF_PATH != ['not_exist_directory'] and len(config.LIST_OF_PATH) != 0:
        run()
    raise FileNotFoundError(f'you need included directories on {Preference.PATH_WITH_PREFERENCE}')

