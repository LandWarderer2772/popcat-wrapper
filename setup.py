from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pop-wrapper",
    version="1.0.0",
    author="land_lmao",
    author_email="mh3as81gb@mozmail.com",
    description="A comprehensive Python wrapper for the Popcat API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LandWarderer2772/pop-wrapper",
    project_urls={
        "Bug Tracker": "https://github.com/LandWarderer2772/pop-wrapper/issues",
        "Documentation": "https://popcat.readthedocs.io/",
        "Source Code": "https://github.com/LandWarderer2772/pop-wrapper",
        "Popcat API": "https://popcat.xyz/api"
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
        "Topic :: Games/Entertainment",
        "Topic :: Text Processing :: General",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "twine>=4.0.0",
            "build>=0.8.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "responses>=0.20.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "sphinx-autodoc-typehints>=1.17.0",
        ]
    },
    keywords=[
        "popcat", "api", "wrapper", "meme", "image", "manipulation", 
        "discord", "bot", "random", "joke", "weather", "github", 
        "text", "utilities", "entertainment", "social"
    ],
    include_package_data=True,
    zip_safe=False,
)