import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robotframework-jiraissueopener",
    version="0.0.2.5",
    author="Andrea Gubellini",
    author_email="agubellini@yahoo.com",
    description="An automatic Jira issue opener for Robotframework",
    long_description=[],
    long_description_content_type="text/markdown",
    url="https://github.com/andreagubellini/robotframework-jiraissueopener",
    packages=['jiraissueopener'],
    install_requires=['robotframework>=3.0', 'requests>=2.20.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])    