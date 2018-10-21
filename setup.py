from setuptools import setup, find_packages


requirements = {
    "package": [x.strip() for x in open('requirements.txt').readlines()],
    "test": [
        "pytest",
        "pytest-cov",
        "pytest-flake8",
        "pytest-mock",
        "pytest-pudb",
        "pytest-xdist",
    ],
    "setup": [
        "pytest-runner",
    ],
}

requirements.update(all=sorted(set().union(*requirements.values())))

setup(
    name='instagagefluence',
    version='0.0.0',
    description='Python Instagram Engagement Influencer Bot',
    long_description=open('README.rst').read(),
    author='Kyle James Walker',
    author_email='KyleJamesWalker@gmail.com',
    url='https://github.com/KyleJamesWalker/instagagefluence',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requirements['package'],
    extras_require=requirements,
    setup_requires=requirements['setup'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'igf = instagagefluence.cli:main',
        ],
        'yamlsettings10': [
            'ext = instagagefluence.config:ConfigExtension',
        ],
    },
    test_suite='tests',
    tests_require=requirements['test'],
)
