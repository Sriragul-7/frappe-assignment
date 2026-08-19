import frappe
from frappe.query_builder import DocType


@frappe.whitelist()
def training_demo():

    TrainingProgram = DocType("Training Program")
    TrainingEnrollment = DocType("Training Enrollment")
    
    query = (
        frappe.qb.from_(TrainingProgram)
        .inner_join(TrainingEnrollment)
        .on(TrainingProgram.name == TrainingEnrollment.program)
        .select(
            TrainingProgram.name.as_("program"),
            TrainingProgram.program_name,
            TrainingEnrollment.name.as_("enrollment"),
            TrainingEnrollment.student_name,
            TrainingEnrollment.enrollment_status,
            TrainingEnrollment.total_amount
        )
    )

    results = query.run(as_dict=True)

    if not results:
        return {
            "message": "No training enrollments found."
        }

    program_name = results[0]["program"]

    program = frappe.get_doc("Training Program", program_name)

    program.description = (
        (program.description or "")
        + "\n\nUpdated using Document API."
    )

    program.save()
    
    for row in results:
        frappe.db.set_value(
            "Training Enrollment",
            {
                "program": row["program"],
                "student_name": row["student_name"]
            },
            "enrollment_status",
            "Approved"
        )
      
    return {
        "success": True,
        "records_found": len(results),
        "updated_program": program_name,
        "data": results
    }
    


@frappe.whitelist()
def get_recent_todos():
    todos = frappe.get_list(
        "ToDo",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit_page_length=5,
    )

    for todo in todos:
        todo["email"] = frappe.db.get_value(
            "User",
            todo["owner"],
            "email",
        )

    return {
        "timestamp": frappe.utils.now(),
        "records": todos,
    }
    


@frappe.whitelist()
def create_task(task_subject):
    task = frappe.new_doc("Task")
    task.subject = task_subject
    task.save()
    return task.name

