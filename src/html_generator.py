def generate_html(data): #Only as basic for testing
    html_content = ""
    # Gathering data:
    test = data.get("test", 1) #Makes the default a Hello world box, the basic url http://localhost:5000/embed? is therefore a hello world test
    match test:
        case 1:
            return """<div style="border: 2px solid red; padding: 10px; display:inline-block;">
                    Hello World
                    </div>"""

    return html_content
