from setuptools import setup, find_packages

setup(
	name='stackcollector',
	version='1.0.0',
	packages=find_packages(),
	author='Jakob Schmutz',
	author_email='jakob@schmutz.co.uk',
	include_package_data=True,
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
	install_requires=[
		'requests>=2.4.3',
		'flask>=0.10.1',
		'click',
		'dateparser',
	],
)
