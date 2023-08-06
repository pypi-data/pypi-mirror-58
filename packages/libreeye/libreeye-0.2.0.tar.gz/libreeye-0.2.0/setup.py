import os
import setuptools


# Call setup method
setuptools.setup(
    name='libreeye',
    version='0.2.0',
    description='WIP',
    url='https://chponte.github.io/libreeye',
    author='Christian Ponte',
    author_email='chrponte@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='libreeye',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.7',
    install_requires=[
        'boto3',
        'botocore',
        'docker',
        'ffmpeg-python',
        'numpy',
        'python-daemon'
    ],
    entry_points={
        'console_scripts': [
            'lectl=libreeye.daemon.control:main'
        ],
    },
    package_data={'libreeye': [os.path.join(*r.split(os.path.sep)[2:], f) 
        for r, _, fs in os.walk('src/libreeye/package_data') for f in fs]},
    project_urls={
        'Bug Reports': 'https://github.com/chponte/libreeye/issues',
        'Funding': 'https://chponte.github.io/donate/',
        'Source': 'https://github.com/chponte/libreeye/',
        'Docker hub': 'https://hub.docker.com/repository/docker/chponte/libreeye/',
    },
)
