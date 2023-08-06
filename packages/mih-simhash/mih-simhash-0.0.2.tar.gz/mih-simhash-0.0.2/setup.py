#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'mih-simhash',
        version = '0.0.2',
        description = '',
        long_description = '',
        author = 'MIH',
        author_email = '',
        license = '',
        url = '',
        scripts = [],
        packages = [],
        namespace_packages = [],
        py_modules = [
            '__init__',
            'simhash',
            'redis'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'aioredis==1.3.1',
            'asn1crypto==0.24.0',
            'async-timeout==3.0.1',
            'backcall==0.1.0',
            'bleach==3.1.0',
            'boto==2.49.0',
            'boto3==1.10.23',
            'botocore==1.13.23',
            'certifi==2019.6.16',
            'cffi==1.12.3',
            'chardet==3.0.4',
            'cmarkgfm==0.4.2',
            'cryptography==2.7',
            'cycler==0.10.0',
            'decorator==4.4.0',
            'docutils==0.15.2',
            'future==0.17.1',
            'gensim==3.8.1',
            'hiredis==1.0.1',
            'idna==2.8',
            'ipython==7.8.0',
            'ipython-genutils==0.2.0',
            'jedi==0.15.1',
            'jieba==0.39',
            'jmespath==0.9.4',
            'joblib==0.13.2',
            'JPype1==0.7.0',
            'kiwisolver==1.1.0',
            'matplotlib==3.1.1',
            'mih-similarity==0.0.5',
            'mkl-fft==1.0.14',
            'mkl-random==1.0.2',
            'mkl-service==2.3.0',
            'nltk==3.4.5',
            'numpy==1.16.5',
            'pandas==0.25.1',
            'parso==0.5.1',
            'patsy==0.5.1',
            'pexpect==4.7.0',
            'pickleshare==0.7.5',
            'pkginfo==1.5.0.1',
            'progressbar2==3.47.0',
            'prompt-toolkit==2.0.9',
            'ptyprocess==0.6.0',
            'pybuilder==0.11.17',
            'pycparser==2.19',
            'Pygments==2.4.2',
            'pyhanlp==0.1.49',
            'pymongo==3.9.0',
            'pyOpenSSL==19.0.0',
            'pypandoc==1.3.3',
            'pyparsing==2.4.2',
            'PySocks==1.7.0',
            'python-dateutil==2.8.0',
            'python-utils==2.3.0',
            'pytz==2019.2',
            'readme-renderer==24.0',
            'requests==2.22.0',
            'requests-toolbelt==0.9.1',
            's3transfer==0.2.1',
            'scikit-learn==0.21.2',
            'scipy==1.3.1',
            'seaborn==0.9.0',
            'six==1.12.0',
            'smart-open==1.9.0',
            'statsmodels==0.10.1',
            'tailer==0.4.1',
            'tblib==1.4.0',
            'tornado==6.0.3',
            'tqdm==4.32.1',
            'traitlets==4.3.2',
            'twine==1.13.0',
            'unittest-xml-reporting==2.5.1',
            'urllib3==1.24.2',
            'wcwidth==0.1.7',
            'webencodings==0.5.1'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
