from setuptools import setup

setup (
    name="ct01-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "Caffeine Tracker modules",
    packages=['ct01_config','ct01_models'],
    python_requires=">=3.6",
    )