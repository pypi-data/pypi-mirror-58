from setuptools import setup

setup(name='classifier_yan_zabab',
      version='0.5',
      description='Example Package',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='intents',
      url='http://github.com/theKirill/GensimSample',
      author='Yanyushkin',
      author_email='k.a.yanushkin@gmail.com',
      license='MIT',
      packages=['classifier_yan_zabab'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['example-command=classifier_yan_zabab.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
