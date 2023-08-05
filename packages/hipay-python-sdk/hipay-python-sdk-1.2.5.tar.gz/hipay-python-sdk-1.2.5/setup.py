from distutils.core import setup
setup(
  name = 'hipay-python-sdk',         # How you named your package folder (MyLib)
  packages = ['hipay_python_sdk'],   # Chose the same as "name"
  version = '1.2.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python SDK for HiPay.com',   # Give a short description about your library
  author = 'Marco Mendao',                   # Type in your name
  author_email = 'mac.mendao@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Menda0',   # Provide either the link to your github or to your website
  keywords = ['HiPay', 'Payments', 'Gateway'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'zeep'
      ],
  classifiers=[
  ],
)
