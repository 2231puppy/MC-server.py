import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="test-package",
    version="0.0.1",
    author="2231puppy",
    author_email="micha@2231puppy.tech",
    packages=["mc-server.py"],
    description="A utility to create a Minecraft server from a config file.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/2231puppy/MC-server.py",
    license="AGPL-3.0-only",
    python_requires=">=3.8",
    install_requires=[],
)
