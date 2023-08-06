#include "pydmodel.h"

using namespace boost::python;
using namespace std;

PyDModel::PyDModel(string db_id)
    : obj(db_id, py_store, py_sync),
      caller(NULL)
{
    if (py_sync == NULL || py_store == NULL) {
        throw Dinemic::DException("Dinemic is not initialized. Call pydinemic.launch first");
    }
}

PyDModel::PyDModel(string db_id, string caller_id)
    : obj(db_id, py_store, py_sync),
      caller(NULL)
{
    if (py_sync == NULL || py_store == NULL) {
        throw Dinemic::DException("Dinemic is not initialized. Call pydinemic.launch first");
    }
    if (caller_id != "") {
        caller = new Dinemic::DModel(caller_id, py_store, py_sync);
    }
}

PyDModel::PyDModel(string model_name, boost::python::list authorized_objects)
    : obj(model_name, py_store, py_sync, std::vector<string>(boost::python::stl_input_iterator<string>(authorized_objects), boost::python::stl_input_iterator<string>() )),
      caller(NULL)
{
    if (py_sync == NULL || py_store == NULL) {
        throw Dinemic::DException("Dinemic is not initialized. Call pydinemic.launch first");
    }
}

PyDModel::PyDModel(const PyDModel &o)
    : obj(o.obj)
{
}

string PyDModel::get_id() {
    return obj.get_id();
}

string PyDModel::get_db_id() {
    return obj.get_db_id();
}

string PyDModel::get_model() {
    return obj.get_model();
}

vector<string> PyDModel::object_list(string filter) {
    return obj.object_list(filter);
}

vector<string> PyDModel::object_list_owned(string filter) {
    return obj.object_list_owned(filter);
}

void PyDModel::set(string key, string value) {
    obj.set(key, value);
}

string PyDModel::get(string key, string default_value) {
    return obj.get(key, default_value);
}

void PyDModel::del(string key) {
    obj.del(key);
}
