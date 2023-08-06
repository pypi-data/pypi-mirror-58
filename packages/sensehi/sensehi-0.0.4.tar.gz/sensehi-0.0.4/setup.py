import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="sensehi",
    version="0.0.4",
    author='yyx',
    py_modules=['sensehi.__init__', 'sensehi.niimaskplot', 'sensehi.hello', 'sensehi.lib'],
    author_email="954053501@qq.com",
    description="demo",
    long_description=long_description,
    url="https://github.com/...",
    classifier=[
        "Programming language :: Python :: 3"
    ]
)
