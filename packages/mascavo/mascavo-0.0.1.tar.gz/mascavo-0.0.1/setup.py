from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="mascavo",
    version="0.0.1",
    description="mascavo",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jonatasrenan/mascavo",
    author="Jônatas Renan Camilo Alves",
    author_email="jonatasrenan@gmail.com",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
    keywords="Mascavo library",
    packages=["mascavo"],
    install_requires=requirements,
    include_package_data=True,
    package_data={}
)
