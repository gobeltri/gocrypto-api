load_fees_table();

/* AJAX request to get JSON content */
function load_fees_table() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("fees-section").innerHTML = this.responseText;
        }
    };
    xhttp.open('GET', '/api/v1', true);
    xhttp.send();
}