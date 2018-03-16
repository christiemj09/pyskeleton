"""
Print out the setup.py template.
"""

# Help from https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package

import pkg_resources


def main():
    resource_package = 'pyskeleton'
    resource_path = '/'.join(['files', 'setup_template.py'])
    print(pkg_resources.resource_stream(resource_package, resource_path))


if __name__ == '__main__':
    main()

