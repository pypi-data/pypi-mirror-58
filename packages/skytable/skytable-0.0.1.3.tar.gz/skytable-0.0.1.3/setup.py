from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(
    os.path.join(here, "skytable", "__version__.py"), mode="r", encoding="utf-8"
) as f:
    exec(f.read(), about)

with open(os.path.join(here, "README.md"), mode="r", encoding="utf-8") as f:
    readme = f.read()

with open(os.path.join(here, "HISTORY.md"), mode="r", encoding="utf-8") as f:
    history = f.read()

setup_requires = ["pytest-runner"]
install_requires = ["requests>=2", "six>=1.10", "pymongo>=3"]
tests_require = ["requests-mock", "requests"]

setup(
    name=about["__name__"],
    description=about["__description__"],
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__authoremail__"],
    url=about["__url__"],
    version=about["__version__"],
    packages=["skytable"],
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    keywords=["skytable", "mongodb"],
    license=about["__license__"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
