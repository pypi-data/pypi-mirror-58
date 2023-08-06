import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-sso-ui",
    version="0.1.1",
    description="A simple SSO UI CAS wrapper for Flask",
    author="Made Wira Dhanar Santika",
    author_email="dhanar.santika@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DhanarSantika/flask-sso-ui",
    license="MIT",
    packages=["flask_sso_ui"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
    install_requires=["python-cas", "flask", "requests"]
)