import os
from pip._internal.utils.misc import get_installed_distributions

package_required_items = {}
package_required_items['pandas'] = ['pandas','numpy','six','pytz']
package_required_items['selenium'] = ['selenium']
package_required_items['pyqt5'] = ['pyqt5']
package_required_items['scipy'] = ['scipy','numpy']


def get_python_installed_packages_list():
    installed_packages = get_installed_distributions()
    res = {}
    for i in installed_packages:
        res[i.key]=i.version
    return res

def remove_packages_from_excluede_packages_list(installed_packages, include_packages):
    for include_package in include_packages:
        if include_package in package_required_items:
            for required_item in package_required_items[include_package]:
                print('remove '+required_item)
                installed_packages.pop(required_item,None)
    exclude_packages_list = sorted(["%s" % i for i in installed_packages])
    return exclude_packages_list

def get_excluded_packages_list(include_packages):
    installed_packages = get_python_installed_packages_list()
    exclude_packages_list = remove_packages_from_excluede_packages_list(installed_packages, include_packages)
    return exclude_packages_list

def compile_py_to_exe(included_packages_list, python_file):
    exclude_packages_list = get_excluded_packages_list(included_packages_list)
    text = ''
    for i in exclude_packages_list:
        text+="--exclude-module="+'\"'+i+'\"'+' '
    cmd = 'cd '+ os.getcwd()
    print(cmd)
    os.system(cmd)
    cmd = 'pyinstaller '+ text + '-F --noconsole '+ python_file
    print(cmd)
    os.system(cmd)

if __name__=='__main__':
    compile_py_to_exe(['pandas','pyqt5'],'bear_kids_player.py')
