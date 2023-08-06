import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iwebrepl",
    version="0.2.0",
    author="Vlatko Kosturjak",
    author_email="vlatko.kosturjak@gmail.com",
    description="Client to handle micropython web_repl interactively",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kost/iwebrepl-python",
    packages=setuptools.find_packages(),
    install_requires=[
        "websocket-client",
        "prompt_toolkit",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'scripts/iwebrepl'
    ]
)
