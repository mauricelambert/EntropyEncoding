from setuptools import setup, find_packages
import EntropyEncoding as package

setup(
    name="EntropyEncoding",
    version=package.__version__,
    py_modules=["EntropyEncoding"],
    packages=find_packages(include=[]),
    install_requires=[],
    scripts=[],
    author="Maurice Lambert",
    author_email="mauricelambert434@gmail.com",
    maintainer="Maurice Lambert",
    maintainer_email="mauricelambert434@gmail.com",
    description="This package implements an encoding to bypass entropy antivirus check.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mauricelambert/EntropyEncoding",
    project_urls={
        "Github": "https://github.com/mauricelambert/EntropyEncoding",
        "Documentation": "https://mauricelambert.github.io/info/python/security/EntropyEncoding.html",
    },
    include_package_data=True,
    classifiers=[
        "Topic :: System",
        "Topic :: Security",
        "Environment :: Console",
        "Topic :: System :: Shells",
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: System :: System Shells",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    keywords=[
        "entropy",
        "antivirus-bypass",
        "payload-encoding",
        "encoding",
        "malware",
    ],
    platforms=["Windows", "Linux", "MacOS"],
    license="GPL-3.0 License",
    python_requires=">=3.8",
)
