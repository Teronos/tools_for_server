import time
import os

from src.basic_struct import Preference


def check_directory(path: str):
    def filter_elder(path_to_file: str) -> bool:
        return time.time() - os.stat(path_to_file).st_mtime > config.LIFE_TIME

    def rm_files(path_file) -> int:
        try:
            os.remove(path_file)
            return 1
        except FileNotFoundError:
            print(f"No such file or directory: {path}")

    paths_files_from_directory = list(map(lambda x: f"{path}/{x}", os.listdir(path)))
    count = sum(list(map(rm_files, list(filter(filter_elder, paths_files_from_directory)))))
    print(f"remove {count} files")


def run():
    while True:
        list(map(check_directory, config.LIST_OF_PATH))
        time.sleep(config.FREQUENCY_RUN)


if __name__ == '__main__':
    global config
    config = Preference.load_preference_from()
    if config.LIST_OF_PATH != ['not_exist_directory'] and len(config.LIST_OF_PATH) != 0:
        run()
    raise FileNotFoundError(f'you need included directories on {Preference.PATH_WITH_PREFERENCE}')
