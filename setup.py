from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import subprocess

def fetch_libraries():
    os.makedirs("/home/user/app/src/", exist_ok=True)
    os.chdir("/home/user/app/src")
    git_download = ["git", "clone", "https://github.com/kohya-ss/sd-scripts.git", "-b", "sd3"]
    subprocess.run(git_download)
    os.chdir("sd-scripts")    
    pip_install = ["pip", "install", "--no-cache-dir", "-r", "./requirements.txt"]
    subprocess.run(pip_install)
    os.chdir("/home/user/app")

class ChainInstall(install):
    def run(self):
        fetch_libraries()
        install.run(self)

setup(
    name="flux-trainer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pip",
        "setuptools",
        "wheel",
    ],
    cmdclass={"install": ChainInstall},
)