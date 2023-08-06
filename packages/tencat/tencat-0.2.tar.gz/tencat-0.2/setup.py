"""Setup for tencat package."""

import setuptools

with open('README.rst') as f:
	README = f.read()

setuptools.setup(
	author="Nicholas Meyer, Agniezka Rozniak, Pia Ruttner",
	author_email="meyernic@student.ethz.ch, rozniaka@student.ethz.ch, ruttnerp@student.ethz.ch",
	name='tencat',
	license="MIT",
	description='tencat is a python package that offers functionality to slice sparse tensors',
	version='v0.2',
	long_description=README,
	url='https://github.com/NixtonM/TenCat',
	packages=setuptools.find_packages(),
	python_requires=">=3.6",
	install_requires=['numpy'],
	classifiers=[ 
		'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
