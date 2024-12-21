from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import subprocess

def install_requirements():
    if os.path.exists("requirements.txt"):
        subprocess.check_call([ "pip", "install", "--no-cache-dir", "-r", "requirements.txt" ])

# def fetch_models():
    # from huggingface_hub import login, hf_hub_download
    # login(token="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")
    # os.makedirs("/home/user/app/src/models", exist_ok=True)
    # hf_hub_download(repo_id="black-forest-labs/FLUX.1-dev", filename="ae.safetensors", local_dir="/data/models")
    # hf_hub_download(repo_id="comfyanonymous/flux_text_encoders", filename="t5xxl_fp8_e4m3fn.safetensors", local_dir="/data/models")
    # hf_hub_download(repo_id="comfyanonymous/flux_text_encoders", filename="clip_l.safetensors", local_dir="/data/models")
    # hf_hub_download(repo_id="Kijai/flux-fp8", filename="flux1-dev-fp8.safetensors", local_dir="/data/models")

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
        install_requirements()
        fetch_libraries()
        #fetch_models()
        install.run(self)

setup(
    name="flux-trainer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "huggingface_hub==0.26.5",
        "pip",
        "setuptools",
        "wheel",
    ],
    cmdclass={"install": ChainInstall},
)