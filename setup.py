from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()
setup(
    name='read-only-attributes',         # How you named your package folder (MyLib)
    packages=['roa'],   # Chose the same as "name"
    version='2.0.0',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Makes read only attributes for a Python class',   # Give a short description about your library
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='tek.shinobi',                   # Type in your name
    author_email='tek.shinobi.ninja@gmail.com',      # Type in your E-Mail
    url='https://github.com/tek-shinobi/read-only-attributes',   # Provide either the link to your github or to your website
    keywords=['read', 'only', 'attributes', 'property'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
    ],
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ]
)
