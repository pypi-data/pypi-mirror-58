# Copyright 2019 Portmod Authors
# Distributed under the terms of the GNU General Public License v3

import os
import tempfile
import configparser
import getpass
import git
from appdirs import AppDirs


class Env:
    DEBUG = False

    APP_NAME = "portmod"
    DIRS = AppDirs(APP_NAME)

    TMP_DIR = os.path.join(tempfile.gettempdir(), "portmod")

    PORTMOD_CONFIG_DIR = DIRS.user_config_dir
    SET_DIR = os.path.join(PORTMOD_CONFIG_DIR, "sets")
    PORTMOD_CONFIG = os.path.join(PORTMOD_CONFIG_DIR, "portmod.conf")

    PORTMOD_LOCAL_DIR = DIRS.user_data_dir
    MOD_DIR = os.path.join(PORTMOD_LOCAL_DIR, "mods")
    CACHE_DIR = DIRS.user_cache_dir
    DOWNLOAD_DIR = os.path.join(CACHE_DIR, "downloads")

    INSTALLED_DB = os.path.join(PORTMOD_LOCAL_DIR, "db")
    PORTMOD_MIRRORS_DEFAULT = "https://gitlab.com/portmod/mirror/raw/master/"

    ALLOW_LOAD_ERROR = True

    REPO = "https://gitlab.com/portmod/openmw-mods.git"
    REPOS_FILE = os.path.join(PORTMOD_CONFIG_DIR, "repos.cfg")

    REPOS = []

    INTERACTIVE = True


env = Env()


if not env.REPOS:
    import portmod.repos

    env.REPOS = portmod.repos.get_repos()


# Ensure that INSTALLED_DB exists
if not os.path.exists(env.INSTALLED_DB):
    # Initialize as git repo
    os.makedirs(env.INSTALLED_DB)
    gitrepo = git.Repo.init(env.INSTALLED_DB)
    # This repository is for local purposes only.
    # We don't want to worry about prompts for the user's gpg key password
    globalconfig = git.config.GitConfigParser()
    localconfig = gitrepo.config_writer()
    localconfig.set_value("commit", "gpgsign", False)
    USER = getpass.getuser()

    # Set the user name and email if they aren't in a global config
    try:
        globalconfig.get_value("user", "name")
    except (configparser.NoOptionError, configparser.NoSectionError):
        localconfig.set_value("user", "name", f"{USER}")

    try:
        globalconfig.get_value("user", "email")
    except (configparser.NoOptionError, configparser.NoSectionError):
        localconfig.set_value("user", "email", f"{USER}@example.com")

    localconfig.release()
