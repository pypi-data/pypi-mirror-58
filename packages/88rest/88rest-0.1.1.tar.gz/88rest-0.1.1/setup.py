import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="88rest",
    version="0.1.1",
    author="Rimba Prayoga",
    author_email="rimba47prayoga@gmail.com",
    description="88 Rest Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://pypi.python.org/pypi/88rest/",
    packages=["rest88"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "Django >= 2.2.8, < 3",
        "django-rest-framework",
        "requests",
        "orm88"
    ]
)
