import json
from flask import Flask, request, Response
import requests
from rembg import remove

app = Flask(__name__)

@app.route('/remove_background', methods=['GET'])
def remove_background():
    # Extract the URL parameter from the query string
    url = request.args.get('url')
    
    if not url:
        return Response(json.dumps({'error': 'Missing URL parameter'}), status=400, mimetype='application/json')

    # Download the image from the URL
    response = requests.get(url)
    input_data = response.content

    # Process the image to remove background
    output_data = remove(input_data)

    # Return the background removed image
    return Response(output_data, status=200, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
