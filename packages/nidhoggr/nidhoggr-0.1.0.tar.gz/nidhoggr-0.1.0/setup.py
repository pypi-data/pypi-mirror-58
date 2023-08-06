from pathlib import Path

from setuptools import setup, find_packages

requirements = Path('requirements.txt').read_text().splitlines()
setup_requirements = ['wheel']
test_requirements = Path('requirements_dev.txt').read_text().splitlines()

setup(
    name="nidhoggr",
    version="0.1.0",
    license="MIT",
    description="Yggdrasil protocol implementation",
    author="Andriy Kushnir (Orhideous)",
    author_email="me@orhideous.name",
    url="https://github.com/Orhideous/nidhoggr",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: No Input/Output (Daemon)",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Utilities",
    ],
    keywords=["Minecraft", "Yggdrasil", "Authentication", ],
    setup_requires=setup_requirements,
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='tests',
)
