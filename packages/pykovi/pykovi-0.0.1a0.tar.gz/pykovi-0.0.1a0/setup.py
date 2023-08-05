import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pykovi",
    packages=setuptools.find_packages(),
    version="0.0.1-alpha",
    description="A python library that wraps AWS Wrangler allowing mocked clients and a specialized glue job publisher.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Johni Michels",
    author_email="johni.michels@gmail.com",
    url="https://github.com/kovihq/pykovi",
    entry_points="""
        [console_scripts]
        pykovi=pykovi:cli.publish_jobs
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
    install_requires=[
        "awswrangler==0.0.11",
        "click",
        "list_imports"
    ],
    python_requires=">=3.6",
)
