import os
import zipfile
from .driver_packager import zip_dir, add_version_file_to_zip


class ShellPackager(object):

    def create_shell_package(self, package_name):

        print("Packaging {0}.zip".format(package_name))

        zip_file = zipfile.ZipFile(package_name + ".zip", 'w')

        package_full_name = self.get_package_dir_name(package_name)
        zip_dir(package_full_name, zip_file, False, True)

        zip_file.close()

    @staticmethod
    def get_package_dir_name(package_name):
        package_name += "Package"
        if not os.path.exists(package_name):
            raise Exception('package folder "{0}" not found'.format(package_name))
        return package_name





