import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-francislabounty", # Replace with your own username
    version="0.0.1",
    author="Francis LaBounty",
    author_email="labounty3d@gmail.com",
    description="Lambda DS22 Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/francislabountyjr/lambdata-francislabounty",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)