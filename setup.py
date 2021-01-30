import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="movieverse",
    version="0.0.1",
    author="Koen Baak",
    #author_email="koen.baak@fake.email",
    description="A package for movie viewing analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KoenBaak/movieverse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
