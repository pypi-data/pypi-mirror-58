import os

PYTHONS = ["3.7", "3.6", "3.5", "2.7"]

for python in PYTHONS:
    print("conda build -c conda-forge -c  conda_recipe/ -c nostrumbiodiscovery --python={}".format(python))
    os.system("conda build -c conda-forge conda_recipe/ -c nostrumbiodiscovery --python={}".format(python))
