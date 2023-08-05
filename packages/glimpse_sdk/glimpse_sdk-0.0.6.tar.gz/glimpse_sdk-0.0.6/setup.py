import distutils.core

try:
    import setuptools
except ImportError:
    pass

packages = ['pycryptodome', 'requests']

distutils.core.setup(
    name='glimpse_sdk',
    version='0.0.6',
    packages=['glimpse_sdk', 'glimpse_sdk/crypto'],

    author='murphy',
    author_email='murphy@nilinside.com',
    install_requires=packages,
)
