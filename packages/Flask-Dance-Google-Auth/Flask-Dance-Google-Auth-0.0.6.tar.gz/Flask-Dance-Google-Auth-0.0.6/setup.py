import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask-Dance-Google-Auth",
    version="0.0.6",
    author="spyc",
    author_email="unknown@gmail.com",
    description="A personal package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=['flask_dance_google_auth'],
    license='MIT',
    install_requires=['Flask', 'Flask-Dance'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
