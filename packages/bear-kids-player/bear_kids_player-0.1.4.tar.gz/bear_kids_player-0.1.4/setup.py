import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bear_kids_player", # Replace with your own username
    version="0.1.4",
    author="Shawn Wang",
    author_email="shawnyanwang@gmail.com",
    description="A player for kids",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shawnyanwang/bear_kids_player",
    packages=['bear_kids_player'],
    # scripts=['bear_kids_player.py','question_database_operation.py','config_processing.py'],
    include_package_data=True,
    package_data = {'bear_kids_player':['*.csv','*.ui']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['numpy','six','pytz',"pandas",'PyQt5','playsound','gtts']
)
