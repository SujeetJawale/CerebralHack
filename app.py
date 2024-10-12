from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to store blogs, with the author's name as the key and their blogs as the value
blogs = {}

# Route to serve the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to get all blogs (for displaying on the frontend)
@app.route('/get_blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs)

# Route to submit a new blog (author and content)
@app.route('/submit_blog', methods=['POST'])
def submit_blog():
    data = request.json
    author = data.get('author')
    content = data.get('content')
    
    if author and content:
        # Add blog to the dictionary
        if author in blogs:
            blogs[author].append(content)  # Append if the author has already written blogs
            print("Current blogs stored: ", blogs)
        else:
            blogs[author] = [content]  # Create a new entry for the author
            print("Current blogs stored: ", blogs)
        return jsonify({"message": "Blog added successfully!"}), 200
    else:
        return jsonify({"error": "Author and content are required!"}), 400
if __name__ == '__main__':
    app.run(debug=True)
