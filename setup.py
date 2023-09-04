import setuptools

with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'RobustPIR',
    version = '2023.9.4.1',
    author = 'Juan Felipe Renza Chavarría',
    author_email= 'jfrenzac@gmail.com',
    description = 'Library that implements the PIR method modify with S_n and Q_m metrics',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/jfrenza/Robust_PIR',
    project_url = {
        "Bug_Tracker": "https://github.com/jfrenza/Robust_PIR/issues"
    },
    packages = ['Robust_PIR'],
    install_requires = []
)
