import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="dotmvw",
	version="0.1.4",
	author="Yumitomo Onuma",
	author_email="yaonuma@umich.edu",
	description="For automating the complete HyperView session generation process.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/yaonuma/dotmvw",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 2.7",
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
	],
	install_requires=['anytree>=2.7.3'])