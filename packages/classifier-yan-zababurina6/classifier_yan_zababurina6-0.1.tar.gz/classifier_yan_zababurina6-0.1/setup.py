from setuptools import setup

DESCRIPTION = "package for classifiying users requests"
AUTHOR = "Kirill Yanyushkin, Ekaterina Zababurina"
AUTHOR_EMAIL = "ea.zababurina@gmail.com, k.a.yanushkin@gmail.com"
setup(name='classifier_yan_zababurina6',
      version='0.1',
      description=DESCRIPTION,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='intents, intent, classifier of intents',
      url='http://github.com/theKirill/GensimSample',
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license='MIT',
      packages=['classifier_yan_zababurina6'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False)
