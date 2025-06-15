from setuptools import setup, find_packages

setup(
    name='easycvdraw',
    version='0.1',
    description='Beginner-friendly OpenCV drawing utility',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    python_requires='>=3.6',
)
