from setuptools import setup, find_packages

setup(
    name='zeit.content.gallery',
    version='2.6.12.dev0',
    author='gocept',
    author_email='mail@gocept.com',
    url='https://svn.gocept.com/repos/gocept-int/zeit.cms',
    description="ZEIT portraitbox",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='gocept proprietary',
    namespace_packages=['zeit', 'zeit.content'],
    install_requires=[
        'cssselect',
        'Pillow',
        'gocept.form',
        'setuptools',
        'zeit.cms>=2.25.0.dev0',
        'zeit.connector>=2.3.1.dev0',
        'zeit.imp>=0.15.0.dev0',
        'zeit.content.image',
        'zeit.push>=1.7.0.dev0',
        'zeit.wysiwyg',
        'zope.app.appsetup',
        'zope.app.testing',
        'zope.component',
        'zope.formlib',
        'zope.interface',
        'zope.publisher',
        'zope.security',
        'zope.testing',
    ],
    entry_points={
        'fanstatic.libraries': [
            'zeit_content_gallery=zeit.content.gallery.browser.resources:lib',
        ],
    },
)
