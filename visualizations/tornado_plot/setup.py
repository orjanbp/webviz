from setuptools import setup, find_packages

setup(
    name='webviz_tornado_plot',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    package_dir={"": "."},
    package_data={
        'webviz_tornado_plot': []},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz', 'webviz_plotly', 'pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'TornadoPlot = webviz_tornado_plot:TornadoPlot'
        ]
    },
    zip_safe=False
)
