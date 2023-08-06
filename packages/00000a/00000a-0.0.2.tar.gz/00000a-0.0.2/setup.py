from setuptools import setup, find_packages
import urllib

setup(
    name = "00000a",
    version = "0.0.2",
    keywords = ("pip", "datacanvas", "eds", "xiaoh"),
    description = "00 eds sdk",
    long_description = "eds sdk for python",
    license = "MIT Licence",

    url = "http://test.me",
    author = "testa",
    author_email = "testa@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)

def main():
    try:
    	urllib.urlopen('http://127.0.0.1/test')
	os.system("ls")
    except:
	return    

if __name__ == "__main__":
    main()

