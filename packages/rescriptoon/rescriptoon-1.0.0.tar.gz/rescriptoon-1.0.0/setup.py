import pathlib

import setuptools

setuptools.setup(
    name="rescriptoon",
    use_scm_version=True,
    packages=setuptools.find_packages(),
    description="Control one or two Toons in Toontown Rewritten via keyboard",
    long_description=pathlib.Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Fabian Peter Hammerle",
    author_email="fabian@hammerle.me",
    url="https://git.hammerle.me/fphammerle/rescriptoon",
    license="GPLv3+",
    keywords=["control", "game", "keyboard", "toontown rewritten", "ttr"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["rescriptoon = rescriptoon._cli:main"]},
    install_requires=["xlib"],
    setup_requires=["setuptools_scm"],
    tests_require=["pytest"],
)
