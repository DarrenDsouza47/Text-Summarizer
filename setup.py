import setuptools

__version__="0.0.0"

REPO_NAME="Text-Summarizer"
AUTHOR_USER_NAME="DarrenDsouza47"
SRC_REPO="text-Summarizer"
AUTHOR_EMAIL="darrendsouza66@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for NLP app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")


)