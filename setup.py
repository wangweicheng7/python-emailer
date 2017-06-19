# coding: utf-8

# by wangweicheng

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DOC = \
"""
Features:
    Python SMTP 发送带附件电子邮件
    $ sudo pip install pyapns
    Author: weicheng wang
    Note:   Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
    
    支持 easy_install::
    
        $ sudo pip install pyapns
    
    
    <https://github.com/wangweicheng7/python-emailer>`.
"""

setup(
  name = "pyemailer",
  version = "0.1.0",
  description = "Python SMTP 发送带附件电子邮件",
  long_description = DOC,
  author = "wangweicheng",
  author_email="809405366@qq.com",
  license="MIT",
  url="http://github.com/samuraisam/pyapns/tree/master",
  download_url="https://github.com/wangweicheng7/python-emailer",
  classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MAC OS',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules :: email'],
  packages=['pyapns'],
  package_data={},
  install_requires=[]
)
