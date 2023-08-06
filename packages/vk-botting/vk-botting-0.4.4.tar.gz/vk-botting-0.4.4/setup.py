import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vk-botting",
    version="0.4.4",
    author="MrDandycorn",
    author_email="ypsen@yandex.ru",
    description="A basic package for building async VK bots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrdandycorn/vk-botting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
