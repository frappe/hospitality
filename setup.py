from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hospitality/__init__.py
from hospitality import __version__ as version

setup(
	name="hospitality",
	version=version,
	description="Hospitality",
	author="Frappe",
	author_email="pandikunta@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
