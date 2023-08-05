from setuptools import find_packages, setup

from djangocms_scrape_google_photos_album import __version__


REQUIREMENTS = [
    "Django>=1.11",
    "django-cms>=3.5",
    "requests>=2.0",
]


CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Framework :: Django",
    "Framework :: Django :: 1.11",
    "Framework :: Django CMS",
    "Framework :: Django CMS :: 3.5",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
]


setup(
    name="djangocms-scrape-google-photos-album",
    version=__version__,
    author="Kevin Funk",
    url="https://github.com/k-funk/djangocms-scrape-google-photos-album",
    license="GPLv3+",
    description="django-cms plugin to scrape a Google Photos public album link for photo urls.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
)
