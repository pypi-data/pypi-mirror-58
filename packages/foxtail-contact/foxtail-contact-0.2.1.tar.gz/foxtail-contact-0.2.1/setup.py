import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("./foxtail_contact/version.py") as fp:
    exec(fp.read(), version)

install_requires = [
    'django>=2.2',
    'django-mail-templated-simple',
    'django-crispy-forms',
    'django-recaptcha',
    'django-csp-helpers>=0.3'
]

setuptools.setup(
    name="foxtail-contact",
    version=version['__version__'],
    author="Luke Rogers",
    author_email="lukeroge@gmail.com",
    description="A contact form.",
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmptrluke/foxtail-contact",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
