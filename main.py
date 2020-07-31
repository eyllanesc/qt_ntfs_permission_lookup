from PyQt5 import QtCore

fi = QtCore.QFileInfo("main.py")
print(fi.isWritable())

try:
	import qt_ntfs_permission_lookup
except ImportError:
	pass
else:
	print(fi.isWritable())
	qt_ntfs_permission_lookup.enable()
	print(fi.isWritable())