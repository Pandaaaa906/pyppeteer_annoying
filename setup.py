from setuptools import setup

setup(
    name='pyppeteer_annoying',
    version='0.0.1',
    packages=['pyppeteer_annoying'],
    url='https://github.com/Pandaaaa906/pyppeteer_annoying',
    license='GNU General Public License v3.0',
    author='Pandaaaa906',
    author_email='ye.pandaaaa906@gmail.com',
    description='Some shortcuts for pyppeteer',
    include_package_data=True,
    package_data={
        'pyppeteer_annoying': ['js/preload.js', ],
    },
    install_requires=['pyppeteer'],
)
