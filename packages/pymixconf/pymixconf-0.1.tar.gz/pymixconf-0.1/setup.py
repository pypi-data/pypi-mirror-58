from setuptools import setup, find_packages
setup(
    name="pymixconf",
    version="0.1",
    packages=find_packages(),
    install_requires=['pyaml'],
    author="Hannah Ward",
    author_email="hannah@coffee-and-dreams.uk",
    description="Load environment-specific configuration like elixir's mix",
    keywords="configuration",
    project_urls={
        "Source Code": "https://github.com/floatingghost/pymixconf",
    },
    license="MIT"
)
