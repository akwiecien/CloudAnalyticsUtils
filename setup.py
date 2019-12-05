import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CloudAnalyticsUtils-kwiecien", # Replace with your own username
    version="1.0.0",
    description="Utils for help querying OLP",
    url="https://github.com/akwiecien/CloudAnalyticsUtils",
    author="Andrzej Kwiecien",
    author_email="andrzej.kwiecien@here.com",
    licence="MIT",
    packages=['CloudAnalyticsUtils'],
    zip_safe=False,
    python_requires='>=3.7',
)