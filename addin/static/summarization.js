(function () {

    Office.initialize = function (reason) {
        $(document).ready(function () {

            $('#getOOXMLData').click(function () { getOOXML_newAPI(); });

        });
    };

    var currentOOXML = "";

    function postData(input) {

        $.ajax({
            type: "POST",
            url: "http://localhost:55555/summarization1",
            data: { param: input },
            async: false,
            success: function (data) {
                $("#demo").html(data);
            }
        });
    }

    function getOOXML_newAPI() {

        var report = document.getElementById("status");

        while (report.hasChildNodes()) {
            report.removeChild(report.lastChild);
        }


        Word.run(function (context) {

            var body = context.document.body;

            var bodyOOXML = body.getOoxml();

            return context.sync().then(function () {
                currentOOXML = bodyOOXML.value;
                if (window.DOMParser) {
                    parser = new DOMParser();
                    xmlDoc = parser.parseFromString(currentOOXML, "application/xml");
                }
                else {
                    xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
                    xmlDoc.async = false;
                    xmlDoc.loadXML(currentOOXML);
                }
                var x, i, txt;
                txt = "";
                x = xmlDoc.getElementsByTagName("w:t");
                for (i = 0; i < x.length; i++) {
                    txt += x[i].childNodes[0].nodeValue;
                }
                document.getElementById("demo").innerHTML = txt;
                postData(txt);
            });
        })
        .catch(function (error) {

            currentOOXML = "";
            report.innerText = error.message;

            console.log("Error: " + JSON.stringify(error));
            if (error instanceof OfficeExtension.Error) {
                console.log("Debug info: " + JSON.stringify(error.debugInfo));
            }
        });
    }
})();



 