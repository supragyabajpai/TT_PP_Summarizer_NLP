import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPONAME = "TT_PP_Summarizer_NLP"
AUTHOR_USERNAME = "supragyabajpai"
SRC_REPO = "TT_PP_Summarizer_NLP"
AUUTHOR_EMAIL = "supragya.vajpai@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUUTHOR_EMAIL,
    description="T&C_PP_summarizer",
    long_description=long_description,
    long_description_content_type=" we will add this later",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPONAME}/issues",
    },
    package_dir= {"": "src"},
    packages =setuptools.find_packages(where="src")
)


