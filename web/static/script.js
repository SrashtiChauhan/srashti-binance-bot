function toggleFields() {

    let type = document.getElementById("order_type").value;

    document.getElementById("limit_fields").style.display = "none";
    document.getElementById("stop_limit_fields").style.display = "none";
    document.getElementById("oco_fields").style.display = "none";
    document.getElementById("twap_fields").style.display = "none";

    if (type === "LIMIT") {
        document.getElementById("limit_fields").style.display = "block";
    }

    if (type === "STOP_LIMIT") {
        document.getElementById("stop_limit_fields").style.display = "block";
    }

    if (type === "OCO") {
        document.getElementById("oco_fields").style.display = "block";
    }

    if (type === "TWAP") {
        document.getElementById("twap_fields").style.display = "block";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    toggleFields();
});