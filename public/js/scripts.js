// Make an AJAX request and add a table with results on a given section.
load_api_table('GET', '/api/v1', 'fees-section', ['ticker', 'binance_fee_usd', 'bittrex_fee_usd', 'poloniex_fee_usd']);


/* Fill a table from an AJAX request on a JSON API
   @method: 'GET'
   @api_url: URL from API to call
   @section_id: Section ID in target DOM
   @keys: List of dictionary keys to print in table

*/
function load_api_table(method, api_url, section_id, keys) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var html = jsonlist2table(this.responseText, keys);
            document.getElementById(section_id).innerHTML = html;
        }
    };
    xhttp.open(method, api_url, true);
    xhttp.send();
}


/* Converts a JSON-formatted list to a table with given keys */
function jsonlist2table (list, keys) {

    var myObj = JSON.parse(list);
    var html = '<table>';
    
    // Keys
    html += '<tr>';
    for (var i in keys) {
        html += '<th>' + keys[i] + '</th>';
    }
    html += '</tr>';

    // Values
    for (var i in myObj) {
        html += '<tr>';
        for (var j in keys) {
            var key = keys[j];
            html += '<td>' + myObj[i][key] + '</td>';
        }
        html += '</tr>';
    }
    
    html += "</table>";

    return html;
}