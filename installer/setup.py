from setuptools import setup

setup(
    name="Openpdfsign Configurator",
    version="1.0.0",
    description="This installs open-pdf-sign as server and signs all your PDFs served with Nginx with your SSL certificate",
    packages=["opsinstaller"],
    install_requires=["pyparsing"],
    entry_points={
        "console_scripts": [
            "opsconfigurator = opsinstaller.installer:main"
        ]
    }
)
