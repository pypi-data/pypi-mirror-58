#include "pyaction.h"
#include "module.h"

using namespace std;

PyAction::PyAction()
    : callback_on_create(NULL),
      callback_on_created(NULL),
      callback_on_update(NULL),
      callback_on_updated(NULL)
{
    if (py_sync == NULL || py_store == NULL) {
        throw Dinemic::DException("Dinemic is not initialized. Call pydinemic.launch first");
    }
}

void PyAction::py_apply(const string &filter) {
    py_sync->add_on_create_listener(filter, this);
    py_sync->add_on_created_listener(filter, this);
    py_sync->add_on_update_listener(filter, this);
    py_sync->add_on_updated_listener(filter, this);
}

void PyAction::py_revoke(const string &filter) {
    py_sync->remove_on_create_listener(filter, this);
    py_sync->remove_on_created_listener(filter, this);
    py_sync->remove_on_update_listener(filter, this);
    py_sync->remove_on_updated_listener(filter, this);
}

// CREATE
void PyAction::set_callback_on_create(PyObject *cb) {
    callback_on_create = cb;
}
void PyAction::on_create(Dinemic::DActionContext &context, const std::string &key) {
    if (callback_on_create != NULL)
        boost::python::call<string, string>(callback_on_create, context.get_object_id(), key);
}

void PyAction::set_callback_on_created(PyObject *cb) {
    callback_on_created = cb;
}
void PyAction::on_created(Dinemic::DActionContext &context, const std::string &key) {
    if (callback_on_created != NULL)
        boost::python::call<string, string>(callback_on_created, context.get_object_id(), key);
}

void PyAction::set_callback_on_owned_created(PyObject *cb) {
    callback_on_owned_created = cb;
}
void PyAction::on_owned_created(Dinemic::DActionContext &context, const std::string &key) {
    if (callback_on_owned_created != NULL)
        boost::python::call<string, string>(callback_on_owned_created, context.get_object_id(), key);
}


// UPDATE
void PyAction::set_callback_on_update(PyObject *cb) {
    callback_on_update = cb;
}
void PyAction::on_update(Dinemic::DActionContext &context, const string &key, const string &old_value, const string &new_value) {
    if (callback_on_update != NULL)
        boost::python::call<string, string, string, string>(callback_on_update, context.get_object_id(), key, old_value, new_value);
}

void PyAction::set_callback_on_authorized_update(PyObject *cb) {
    callback_on_authorized_update = cb;
}
void PyAction::on_authorized_update(Dinemic::DActionContext &context, const string &key, const string &old_value, const string &new_value) {
    if (callback_on_authorized_update != NULL)
        boost::python::call<string, string, string, string>(callback_on_authorized_update, context.get_object_id(), key, old_value, new_value);
}

void PyAction::set_callback_on_owned_update(PyObject *cb) {
    callback_on_owned_update = cb;
}
void PyAction::on_owned_update(Dinemic::DActionContext &context, const string &key, const string &old_value, const string &new_value) {
    if (callback_on_owned_update != NULL)
        boost::python::call<string, string, string, string>(callback_on_owned_update, context.get_object_id(), key, old_value, new_value);
}


// UPDATED
void PyAction::set_callback_on_updated(PyObject *cb) {
    callback_on_updated = cb;
}
void PyAction::on_updated(Dinemic::DActionContext &context, const string &key, const string &old_value, const string &new_value) {
    if (callback_on_updated != NULL)
        boost::python::call<string, string, string, string>(callback_on_updated, context.get_object_id(), key, old_value, new_value);
}

void PyAction::set_callback_on_authorized_updated(PyObject *cb) {
    callback_on_authorized_updated = cb;
}
void PyAction::on_authorized_updated(Dinemic::DActionContext &context, const string &key, const string &old_value, const string &new_value) {
    if (callback_on_authorized_updated != NULL)
        boost::python::call<string, string, string, string>(callback_on_authorized_updated, context.get_object_id(), key, old_value, new_value);
}

void PyAction::set_callback_on_owned_updated(PyObject *cb) {
    callback_on_owned_updated = cb;
}
void PyAction::on_owned_updated(Dinemic::DActionContext &context, const string &key, const string &old_value, const string &new_value) {
    if (callback_on_owned_updated != NULL)
        boost::python::call<string, string, string, string>(callback_on_owned_updated, context.get_object_id(), key, old_value, new_value);
}

