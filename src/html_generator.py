import json

def generate_html(data): #Only as basic for testing
    html_content = ""
    # Gathering data:
    # We're expecting the data to be in the form: {"test": number, "type": text, "options:" {...}, "data": {...}}
    test = data.get("test", 1) #Makes the default a Hello world box, the basic url http://localhost:5000/embed? is therefore a hello world test
    graph_type = data.get("type", "bar")
    graph_options = json.dumps(data.get("options", {}))
    graph_data = json.dumps(data.get("data", {}))
    # Test matching
    match test:
        case 1: #Hello world
            return """<div style="border: 2px solid red; padding: 10px; display:inline-block;">
                    Hello World
                    </div>"""
        case 2: # Scatter graph
            pass
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markg Chart</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <canvas id="Chart" width="400" height="400"></canvas>
    <script>
        var ctx = document.getElementById('Chart').getContext('2d');
        var Chart = new Chart(ctx, {{
            type: '{graph_type}',
            data: {graph_data},
            options: {graph_options}
        }});
    </script>
</body>
</html>
"""

    return html_content


