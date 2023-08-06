import setuptools
from pathlib import Path
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="sslcommerz-lib",
    version=1.0,
    description="SSLCOMERZ PAYMENT GATEWAY",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="SSLCOMMERZ Developers",
    url="https://github.com/sajanPoddar/sslcommerz-lib-py",
    author_email="sajan.sslwireless@gmail.com",
    keywords=["sslcommerz", "payment", "1.0"],
    packages=setuptools.find_packages(exclude=["tests", "data"]),
    install_requires=[
        "requests",
    ],
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
