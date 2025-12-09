#!/usr/bin/env python
'''
This module contains the main function that runs getTestString.
'''

import {{ cookiecutter.package_name }}.core as pscore

def main():
    '''Prints the result of getTestString function.
    :returns: NoneType
    '''
    print(pscore.getTestString())

if __name__ == "__main__":
    main()
