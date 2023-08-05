from setuptools import setup, find_packages


with open("README.rst") as f:
    long_description = f.read()

setup(
    name="django-polaris",
    version="0.9.11",
    description="A SEP-24-compliant Django anchor server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://django-polaris.readthedocs.io/en/stable",
    author="Jake Urban",
    author_email="jake@stellar.org",
    license="Apache license 2.0",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=["stellar", "sdf", "anchor", "server", "polaris", "sep-24", "sep24"],
    include_package_data=True,
    package_dir={"": "polaris"},
    packages=find_packages("polaris"),
    install_requires=[
        "aiohttp==4.0.0a1",
        "aiohttp-sse-client==0.1.6",
        "async-timeout==3.0.1",
        "attrs==19.3.0",
        "certifi==2019.11.28",
        "cffi==1.13.2",
        "chardet==3.0.4",
        "crc16==0.1.1",
        "django==2.2.8",
        "django-cors-headers==3.2.0",
        "django-environ==0.4.5",
        "django-model-utils==4.0.0",
        "django-sslserver==0.22",
        "djangorestframework==3.11.0",
        "idna==2.8",
        "mnemonic==0.19",
        "multidict==4.7.1",
        "psycopg2-binary==2.8.4",
        "pycparser==2.19",
        "pyjwt==1.7.1",
        "pynacl==1.3.0",
        "pytz==2019.3",
        "requests==2.22.0",
        "six==1.13.0",
        "sqlparse==0.3.0",
        "stellar-base-sseclient==0.0.21",
        "stellar-sdk==2.0.0",
        "toml==0.10.0",
        "typing-extensions==3.7.4.1",
        "urllib3==1.25.7",
        "whitenoise==5.0.1",
        "yarl==1.4.2",
    ],
    python_requires=">=3.7",
)
