from setuptools import setup

setup(
    name="songscribe",
    version="0.1.0",
    description="A lyrics utility tool that fetches the lyrics and automatically writes to ID3 tag.",
    # long_description=README,
    # long_description_content_type="text/markdown",
    url="https://github.com/bluemberg/songscribe",
    author="bluemberg",
    # author_email="",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GPL-3.0 License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["songscribe"],
    include_package_data=True,
    install_requires=[
        "python-dotenv", "lyricsgenius", "music-tag"
    ],
    entry_points={"console_scripts": ["songscribe=songscribe.__main__:main"]},
)