from setuptools import find_packages, setup

setup(
    name='pfluid',
    version='0.0.1',
    description='Thin wrapper that makes subprocess more fluid to work with',
    url='https://github.com/meyer1994/pfluid',
    download_url='https://github.com/meyer1994/pfluid/archive/v0.0.1.tar.gz',
    author='João Vicente Meyer',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools'
    ],
    keywords='subprocess run popen bash fluid',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    python_requires='>=3.6',
)
