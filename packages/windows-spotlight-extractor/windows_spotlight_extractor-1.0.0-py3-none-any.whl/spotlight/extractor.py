import logging
import os
import shutil
from configparser import ConfigParser
from pathlib import Path

from PIL import Image


class ConfigRepository:
    CONFIG_HOME: Path = Path(f"{os.environ['localappdata']}/w10-spotlight-extractor")

    def __init__(self):
        os.makedirs(str(ConfigRepository.CONFIG_HOME), exist_ok=True)
        self.config = ConfigParser()
        self._read_config()

    def get_wallpapers_path(self):
        try:
            return Path(self.config["PATHS"]["wallpapers"])
        except KeyError as ke:
            logging.error("PATHS.wallpapers doesn't exist, using default")
            self._set_config("PATHS", "wallpapers", Path(os.environ["userprofile"] + "/OneDrive/Pictures/Spotlight"))
            return self.get_wallpapers_path()

    def get_spotlight_path(self):
        try:
            return Path(self.config["PATHS"]["spotlight_assets"])
        except KeyError as ke:
            logging.error("PATHS.spotlight_assets doesn't exist, using default")
            self._set_config("PATHS", "spotlight_assets", Path(os.environ[
                                                                   "localappdata"] + "/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"))
            return self.get_spotlight_path()

    def get_logging_level(self):
        try:
            return self.config["LOGGING"]["level"]
        except KeyError as ke:
            self._set_config("LOGGING", "level", "INFO")
            return self.get_logging_level()

    def get_logging_file(self):
        try:
            return Path(self.config["LOGGING"]["file"])
        except KeyError as ke:
            return None

    def _set_config(self, section, cfg, value):
        if not self.config.has_section(section):
            self.config.add_section(section)

        self.config.set(str(section), str(cfg), str(value))
        self._save_config()

    def _save_config(self):
        with open(f"{ConfigRepository.CONFIG_HOME}/settings.ini", 'w') as cfg_f:
            self.config.write(cfg_f)
        self._read_config()

    def _read_config(self):
        self.config.read(f"{ConfigRepository.CONFIG_HOME}/settings.ini")


def is_wallpaper_image(filepath) -> bool:
    im = Image.open(filepath)
    width, height = im.size
    return (width >= 1920) and (height >= 1080)


def copy_if_wallpaper(src: Path, dest: Path) -> bool:
    if is_wallpaper_image(src):
        try:
            shutil.copyfile(src, dest)
            return True
        except Exception as e:
            logging.error(f"Failed to Copy File from {src} to {dest}", e)

    return False


def main():
    config_repository = ConfigRepository()

    logging.basicConfig(format="[%(asctime)s] [%(name)s] [%(name)s] - %(message)s",
                        filename=config_repository.get_logging_file(),
                        level={
                            "DEBUG": logging.DEBUG,
                            "INFO": logging.INFO,
                            "WARN": logging.WARN,
                            "ERROR": logging.ERROR
                        }[config_repository.get_logging_level()])
    wallpapers = config_repository.get_wallpapers_path()
    spotlight_assets = config_repository.get_spotlight_path()
    logging.info(f"Copying Windows Spotlight Images Into {wallpapers}")
    for _, _, files in os.walk(spotlight_assets):
        logging.debug(f"Scanning {spotlight_assets}")
        copied = 0
        for file in files:
            logging.debug(f"Checking {file}")
            src = Path(f"{spotlight_assets}/{file}")
            dest = Path(f"{wallpapers}/{file}.jpg")
            if copy_if_wallpaper(src, dest):
                copied += 1
        logging.info(f"Successfully Copied {copied} files")


if __name__ == '__main__':
    main()
