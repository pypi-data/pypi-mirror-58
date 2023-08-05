import setuptools

with open("README.md", "r") as fh:
    long_description_txt = fh.read()

setuptools.setup(
    name='quantastor-qsclient',
    version='5.5.0',
    scripts=['quantastor/qs_client.py'],
    author="OSNEXUS Corporation",
    author_email="support@osnexus.com",
    description="QuantaStor REST API python library",
    long_description=long_description_txt,
    long_description_content_type="text/markdown",
    url="https://github.com/OSNEXUS/QSPyClient",
    packages=setuptools.find_packages(),
    install_requires=['urllib3','requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ],

 )

# User: OSNEXUS
# Password: rPTF!J^BL:YL98%{
