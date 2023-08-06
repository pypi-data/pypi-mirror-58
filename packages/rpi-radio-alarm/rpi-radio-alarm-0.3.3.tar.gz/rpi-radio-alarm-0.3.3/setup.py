from setuptools import setup


setup(
    name='rpi-radio-alarm',
    version='0.3.3',
    license='BSD-3',
    description='rpi-radio-alarm library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='bb4L',
    author_email='39266013+bb4L@users.noreply.github.com',
    url='https://github.com/bb4L/rpi-radio-alarm-pip',
    packages=['rpiradioalarm'],
    keywords=['Raspberry Pi', 'radio', 'alarm'],
    install_requires=[
        'aiohttp==3.5.4',
        'async-timeout==3.0.1',
        'attrs==19.3.0',
        'chardet==3.0.4',
        'discord==1.0.1',
        'discord.py==1.2.4',
        'idna==2.8',
        'multidict==4.5.2',
        'python-dotenv==0.10.3',
        'websockets==6.0',
        'yarl==1.3.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
)
# python setup.py sdist && twine upload dist/*