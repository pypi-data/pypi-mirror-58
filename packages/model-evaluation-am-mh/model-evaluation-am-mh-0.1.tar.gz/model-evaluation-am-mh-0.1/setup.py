from setuptools import setup

setup(name='model-evaluation-am-mh',
      version='0.1',
      description='Model Evaluation tools',
      packages=['model-evaluation-am-mh'],
      license='MIT',
      author = 'Alder Martinez & Michael Howard',
      author_email = 'aldermartinez@gmail.com',
      install_requires=[
          'sklearn',
          'pandas',
          'numpy',
          'matplotlib'
      ],
      zip_safe=False)