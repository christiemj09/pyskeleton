"""
Install {package}.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': '{description}',
		'author': '{author}',
		'download_url': '{download_url}',
		'author_email': '{author_email}',
		'version': '{version}',
		'install_requires': [],
		'packages': ['{package}'],
		'scripts': [],
		'entry_points': {
		    'console_scripts': [],
		},
		'name': '{package}',
	}

	setup(**config)	

if __name__ == '__main__':
	main()
