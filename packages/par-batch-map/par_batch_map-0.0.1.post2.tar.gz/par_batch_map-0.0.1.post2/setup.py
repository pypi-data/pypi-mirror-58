import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

setuptools.setup(
    name="par_batch_map", # Replace with your own username
    version="0.0.1post2",
    author="Krzysztof Rutkowski",
    author_email="krutk@icm.edu.pl",
    description="Package for parallel batch processing of iterators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.icm.edu.pl/krutk/parallel_batch",
    packages=setuptools.find_packages(),
    install_requires=load_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.8',
)
