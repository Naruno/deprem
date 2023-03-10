from pythonforandroid.recipe import PythonRecipe


class DecentraNetworkGuiRecipe(PythonRecipe):
    version = '0.43.0'
    url = 'https://files.pythonhosted.org/packages/7a/92/bcde51e167642cdc22d80def8dd9ea2c632201ffefc864e1b942f9f4097d/decentra_network_gui-0.43.0.tar.gz'

    #call_hostpython_via_targetpython = True
    '''If True, tries to install the module using the hostpython binary
    copied to the target (normally arm) python build dir. However, this
    will fail if the module tries to import e.g. _io.so. Set this to False
    to call hostpython from its own build dir, installing the module in
    the right place via arguments to setup.py. However, this may not set
    the environment correctly and so False is not the default.'''

    #install_in_hostpython = False
    '''If True, additionally installs the module in the hostpython build
    dir. This will make it available to other recipes if
    call_hostpython_via_targetpython is False.
    '''

    #install_in_targetpython = True
    '''If True, installs the module in the targetpython installation dir.
    This is almost always what you want to do.'''

    # depends = []
    depends = ["setuptools", "Kivy", "kivymd", "qrcode", "kivymd_extensions.sweetalert", "plyer", "pillow"]

    call_hostpython_via_targetpython = False
    install_in_hostpython = True

recipe = DecentraNetworkGuiRecipe()
