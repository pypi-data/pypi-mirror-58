from setuptools import setup

NAME = "intents_classifier"
DESCRIPTION = "package for classifiying users requests"
AUTHOR = "Kirill Yanyushkin, Ekaterina Zababurina"
AUTHOR_EMAIL = "ea.zababurina@gmail.com, k.a.yanushkin@gmail.com"
setup(name=NAME,
      version='0.6',
      description=DESCRIPTION,
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='intents, intent, classifier of intents, requests classifier',
      url='http://github.com/theKirill/GensimSample',
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license='MIT',
      install_requires=[
	  'typing',
          'pymorphy2',
	  'nltk',
	  'gensim',
	  'keras',
	  'sklearn',
	  'numpy',
      ],
      packages=[NAME],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False)
