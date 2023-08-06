import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pelk_screen",
    version="0.0.5",
    author="PerfectELK",
    author_email="perfect-elk@perfect-elk.ru",
    description="Screenshot lib",
    long_description=long_description,
    url="https://github.com/PerfectELK/pelk_screen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)