import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mrobot',
    version='1.0',
    url="https://johnnes-smarts.ch",
    license='License :: OSI Approved :: MIT License',
    author='David Johnnes',
    author_email='david.johnnes@gmail.com',
    description='Framework for web automation and testing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='DevOps, Audit Automation, Audit Orchestration, Vendor-Neutral configurations Audit',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
