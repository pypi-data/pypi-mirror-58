from setuptools import setup, find_packages
setup(
    name='GeneralNewsExtractor',
    packages=find_packages(exclude=[]),
    install_requires=['lxml', 'numpy'],
    version='0.1.0',
    description='General extractor of news pages.',
    author='Kingname',
    author_email='contact@kingname.info',
    url='https://github.com/kingname/GeneralNewsExtractor',
    keywords=['python', 'webcrawler', 'webspider'],
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
    ]
)
