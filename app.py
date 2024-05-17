import json
from flask import Flask, request, Response
import requests
from rembg import remove
import os

app = Flask(__name__)

# Get the port from the PORT environment variable or use 8080 as default
port = int(os.environ.get('PORT', 8080))

# Health check route
@app.route('/', methods=['GET'])
def health_check():
    return Response(json.dumps({'status': 'OK'}), status=200, mimetype='application/json')

# Background removal route
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
    # Run the app with binding to the port specified by the PORT environment variable or 8080 as default
    app.run(debug=True, host='0.0.0.0', port=port)
