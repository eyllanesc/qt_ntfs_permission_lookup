import os
from PyQt5 import QtCore


def try_change_permissions():
    CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(CURRENT_DIRECTORY, "test.bin")

    file = QtCore.QFile(filename)
    if file.open(QtCore.QFile.WriteOnly):
        file.write(b"helloworld")
        file.close()

    file.setPermissions(file.permissions() & QtCore.QFileDevice.ReadUser)

    fi = QtCore.QFileInfo(filename)
    print(fi.isWritable())

    QtCore.QFile.remove(filename)


try_change_permissions()

try:
    import qt_ntfs_permission_lookup
except ImportError:
    pass
else:
    qt_ntfs_permission_lookup.enable()

try_change_permissions()
