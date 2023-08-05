import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyPIDTuneMethods",
    version="0.3.5",
    author="ElBar",
    author_email="eleftherios.barbas@gmail.com",
    description="A PID controller design and tuning application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sourceforge.net/projects/pypidtunemethods/",
    packages=setuptools.find_packages(),
	include_package_data=False,
	package_data={
		'pyPIDTuneMethods': ['PIDTuning.xls', 'PIDTune.png', 'ui/*.*', 'ui/icons/*.*'],
		},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)