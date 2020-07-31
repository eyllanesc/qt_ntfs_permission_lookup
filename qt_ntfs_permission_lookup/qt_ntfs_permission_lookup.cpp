#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#ifdef Q_OS_WIN
QT_BEGIN_NAMESPACE
extern Q_CORE_EXPORT int qt_ntfs_permission_lookup;
QT_END_NAMESPACE
#endif

PYBIND11_MODULE(qt_ntfs_permission_lookup, m) {

    m.def("enable", [](){
#ifdef Q_OS_WIN
        qt_ntfs_permission_lookup = 1;
#endif
    });      
    m.def("disable", [](){
#ifdef Q_OS_WIN
        qt_ntfs_permission_lookup = 0;
#endif
    });      

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}