
SETUP_INFO = dict(
    name = 'infi.iscsiapi',
    version = '0.2.13',
    author = 'Arnon Yaari',
    author_email = 'arnony@infinidat.com',

    url = 'https://git.infinidat.com/host-opensource/infi.iscsiapi',
    license = 'BSD',
    description = """cross platfrom iSCSI opertions""",
    long_description = """iscsiapi provides a unified API for iSCSI operations to all supported platrforms""",

    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    install_requires = [
'infi.dtypes.hctl',
'infi.dtypes.iqn',
'infi.execute',
'infi.os_info',
'infi.pkgmgr',
'infi.win32service',
'infi.wmi',
'setuptools',
'six'
],
    namespace_packages = ['infi'],

    package_dir = {'': 'src'},
    package_data = {'': []},
    include_package_data = True,
    zip_safe = False,

    entry_points = dict(
        console_scripts = [],
        gui_scripts = [],
        ),
)

if SETUP_INFO['url'] is None:
    _ = SETUP_INFO.pop('url')

def setup():
    from setuptools import setup as _setup
    from setuptools import find_packages
    SETUP_INFO['packages'] = find_packages('src')
    _setup(**SETUP_INFO)

if __name__ == '__main__':
    setup()

