import json
from flask import Flask, request, Response

app = Flask(__name__)

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

    # Process the image to remove background
    # Replace this part with your actual background removal logic
    # For example, you can use rembg library as in your original code

if __name__ == '__main__':
    app.run(debug=True)
