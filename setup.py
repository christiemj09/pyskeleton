"""
Install pyskeleton.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Initialize a Python project skeleton.',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/pyskeleton.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'install_requires': [],
		'packages': ['pyskeleton'],
		'scripts': [
		    'bin/pyskeleton',
		],
		'entry_points': {
		    'console_scripts': [
		        'cat_setup_template=pyskeleton.cat_setup_template:main',
		    ],
		},
		'name': 'pyskeleton',
	}

	setup(**config)	

if __name__ == '__main__':
	main()
