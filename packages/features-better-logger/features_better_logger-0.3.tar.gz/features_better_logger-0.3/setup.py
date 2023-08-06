from distutils.core import setup

setup(
    name="features_better_logger",
    packages=["features_better_logger"],
    version="0.3",
    license="MIT",
    description="Find Features Better Logging Package",
    author="Calum Webb",
    author_email="calumpeterwebb@icloud.com",
    url="https://github.com/findfeatures/better-logger",
    download_url="https://github.com/findfeatures/better-logger/archive/v0.3.tar.gz",
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)