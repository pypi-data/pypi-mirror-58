import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pimodules", # Replace with your own username
    version='0.1',
    author='Mike Ray',
    author_email='mike.ray@btinternet.com',
    description="A package which contains code to support PiModules products of various kinds.",
    long_description_content_type="text/markdown",
    url='http://pimodules.com',
    packages=['pimodules'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=2.7',
)
