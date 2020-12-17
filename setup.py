from setuptools import setup, find_packages

setup(
    name="pypeeringmanager",
    description="Peering-Manager API client library",
    url="https://github.com/tucows/pypeeringmanager",
    author="Gordon Gidófalvy",
    author_email="ggidofalvy@tucows.com",
    license="Apache2",
    include_package_data=True,
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    install_requires=["pynetbox>=5.1.1", "requests>=2.20.0,<3.0"],
    zip_safe=False,
    keywords=["peering-manager", "peeringmanager"],
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
