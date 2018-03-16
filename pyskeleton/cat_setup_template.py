"""
Print out the setup.py template.
"""

# Help from https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package

import pkg_resources


def main():
    resource_package = 'pyskeleton'
    resource_path = '/'.join(['setup_template.txt'])
    template = pkg_resources.resource_string(resource_package, resource_path)
    print(template.decode('utf-8'))  # bytes to string


if __name__ == '__main__':
    main()

