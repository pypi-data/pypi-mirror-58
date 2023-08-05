"""core.py
"""
import os
import platform


OS = platform.system()


def _minknow_path():
    return {
        "Darwin": os.path.join(os.sep, "Applications", "MinKNOW.app", "Contents", "Resources"),
        "Linux": os.path.join(os.sep, "opt", "ONT", "MinKNOW"),
        "Windows": os.path.join(os.sep, "Program Files", "OxfordNanopore", "MinKNOW"),
    }.get(OS, None)


def _python_path():
    return {
        "Darwin": os.path.join("ont-python", "bin", "python"),
        "Linux": os.path.join("ont-python", "bin", "python"),
        "Windows": os.path.join("ont-python", "python.exe"),
    }.get(OS, None)


def ont_python_path():
    return os.path.join(_minknow_path(), _python_path())


def conf_path():
    conf = os.path.join(
        "conf", "package", "sequencing"
    )
    return os.path.join(_minknow_path(), conf)


def binaries_path():
    return os.path.join(_minknow_path(), "bin")


def full_config_path(filename):
    return os.path.join(conf_path(), filename)


def full_binaries_path(filename):
    return os.path.join(binaries_path(), filename)


def minknow_config_path(filename):
    return os.path.join(_minknow_path(), "conf", filename)


def restart_minknow():
    return {
        "Linux": "Run:\n  sudo systemctl restart minknow",
        "Darwin": "Kill the MinKNOW process:\n  sudo pkill mk_manager_svc\nRestart MinKNOW:\n  sudo /Applications/MinKNOW.app/Contents/Resources/bin/mk_manager_svc --config_dir /Applications/MinKNOW.app/Contents/Resources/conf &",
        "Windows": "Restart your computer",
    }.get(OS, None)


class sudoedit:
    def __init__(self, path, octal=0o777):
        self.path = path
        self.new_oct = octal
        self.old_oct = os.stat(self.path).st_mode & 0o777

    def __enter__(self):
        self.mod_perm(self.new_oct)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mod_perm(self.old_oct)
        return True

    def mod_perm(self, perms):
        os.chmod(self.path, perms)
