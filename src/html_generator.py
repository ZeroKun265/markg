def generate_html(data): #Only as basic for testing
    # Extract data
    style = data.get('style', 'box')
    color = data.get('color', 'red')
    content = data.get('content', 'This is a box')

    # Generate the HTML based on the data
    return f'''
    <div style="border: 2px solid {color}; padding: 10px; display:inline-block;">
        {content}
    </div>
    '''
