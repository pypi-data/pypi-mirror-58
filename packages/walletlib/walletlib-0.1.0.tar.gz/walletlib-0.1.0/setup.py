from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="walletlib",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/jimtje/walletlib",
    license="Unlicense",
    author="jim zhou",
    author_email="jimtje@gmail.com",
    description="Library for accessing cryptocurrency wallet files",
    requires_python=">=3.6.0",
    install_requires=requirements,
    entry_points={
        "console_scripts": ["dumpwallet = walletlib.scripts.dumpwallet:main"]
    },
)
