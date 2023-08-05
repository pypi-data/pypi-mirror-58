from setuptools import setup

setup(name='modelevaluationammh',
      version='0.2',
      description='Model Evaluation tools',
      py_modules=['modelevaluationammh'],
      packages=['modelevaluationammh'],
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