from setuptools import setup, find_packages

setup(
    name="handwritten_character_recognition",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tensorflow",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "jupyter"
    ],
)
