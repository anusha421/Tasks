function validateForm() {
    let text = document.forms["create-form"]["create-body"].value;
    
    if (text == "") {
        alert("Task must be entered");
        return false;
    }
    else {
        alert("Task created");
    }
}

function validateEditForm() {
    let body = document.forms["edit-form"]["edit-body"].value;
    
    if (body == "") {
        alert("Task must be entered");
        return false;
    }
    else {
        alert("Task updated");
    }
}