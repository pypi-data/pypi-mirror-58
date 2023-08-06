from setuptools import setup
from threaded_task_executor import __version__

def readme():
    with open('README.md', 'r') as fo:
        return fo.read()

setup(name='threaded-task-executor',
        version=__version__,
        python_requires='>=3.5',
        description='Spawn a thread that executes tasks in order',
        long_description=readme(),
        long_description_content_type="text/markdown",
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Utilities'
        ],
        keywords='threading tasks order queue',
        url='http://github.com/enchant97/python-threadedtaskexecutor',
        author='enchant97',
        author_email='contact@enchantedcode.co.uk',
        license='mit',
        packages=['threaded_task_executor'],
        include_package_data=True,
        zip_safe=False)
