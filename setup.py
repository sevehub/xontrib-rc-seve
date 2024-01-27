#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-rc-seve',
    version='0.14.0.1',
    license='MIT',
    author='anki-code',
    author_email='no@no.no',
    description="Awesome snippets of code for xonshrc in xonsh shell.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=[
        'xonsh[full]', # The awesome shell.
        'xontrib-prompt-bar', # The bar prompt for xonsh shell with customizable sections and Starship support. 
        'xontrib-zoxide', # Return to the most recently used directory when starting the xonsh shell. 
        'xontrib-argcomplete', # Argcomplete support to tab completion of python and xonsh scripts in xonsh shell. 
        'xontrib-clp', # Copy output to clipboard. URL: https://github.com/anki-code/xontrib-clp
        
        # Get more xontribs:
        #  * https://github.com/topics/xontrib
        #  * https://github.com/xonsh/awesome-xontribs
        #  * https://xon.sh/api/_autosummary/xontribs/xontrib.html
    ],
    extras_require={
        "xxh": [
            "xxh-xxh" # Using xonsh wherever you go through the ssh.
        ],
    },
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.py', '*.xsh']},    
    platforms='any',
)
