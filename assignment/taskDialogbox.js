let dialog = new frappe.ui.Dialog({
    title: "Create Task",
    fields: [
        {
            label: "Task Subject",
            fieldname: "task_subject",
            fieldtype: "Data",
            reqd: 1
        }
    ],
    primary_action_label: "Create Task",
    primary_action(values) {
        frappe.call({
            method: "assignment.TaskCreater.create_task",
            args: {
                task_subject: values.task_subject
            },
            callback(r) {
                if (r.message) {
                    dialog.hide();

                    frappe.msgprint({
                        title: "Success",
                        message: `Task <b>${r.message}</b> created successfully`,
                        indicator: "green"
                    });
                }
            }
        });
    }
});

dialog.show();
