from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Set your OpenAI API key securely
client = OpenAI(api_key="")  # Replace with your actual OpenAI API key

# Dictionary to store blogs, with the author's name as the key and their blogs as a multidimensional array
blogs = {
    "Virat Kohli": [["The Journey of Virat Kohli: From a Young Talent to Cricket Legend", """Hey everyone,

I’m Virat Kohli, and today I want to take you on a journey through my life and career in cricket. Born on November 5, 1988, in Delhi, I grew up with a bat in hand and a dream in my heart. Cricket has always been my passion, and I knew from a young age that I wanted to make it my life.

I still remember captaining the Indian team to victory in the Under-19 World Cup in 2008. That moment was surreal; it marked the beginning of my journey with the national team. I made my debut against Sri Lanka later that year, and I felt a mix of excitement and nerves. Playing for India was a dream come true.

Throughout my career, I’ve had the privilege of representing India in countless matches. There have been highs and lows, but my determination to push boundaries has always driven me. I’ve always believed in chasing targets and never backing down. I take immense pride in being the fastest player to score 10,000 runs in ODIs and leading the team to our historic series win in Australia in 2018-2019.

Leadership has been an incredible journey for me. I strive to inspire my teammates to give their best and play with passion. Seeing my team perform at their peak and achieving our goals together is what I cherish the most.

I’ve always tried to be consistent, and my records—like having the most centuries in ODIs—reflect my hard work and dedication. But it’s not just about personal achievements; it’s about how we can come together as a team and make our fans proud.

Thank you all for being part of this journey with me. Your support means the world, and I promise to keep striving for excellence, both on and off the field.

Cheers,
Virat Kohli
"""]]
}
# Route to serve the homepage
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/atheletes')
def atheletes():
    return render_template('atheletes.html')

# Route to serve the ChatGPT page
@app.route('/ask', methods=['GET'])
def ask_page():
    return render_template('ask.html')

@app.route('/blog', methods=['GET'])
def blog_page():
    return render_template('blog.html')

# Route to get all blogs (for displaying on the frontend)
@app.route('/get_blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs)




# Route to submit a new blog (author, title, and content)
@app.route('/blog', methods=['POST'])
def submit_blog():
    data = request.json
    author = data.get('author')
    title = data.get('title')
    hashtag = data.get('hashtags')
    content = data.get('content')
    

    if author and title and content:
        # Add blog to the dictionary
        if author in blogs:
            blogs[author].append([title, content])  # Append if the author has already written blogs
        else:
            blogs[author] = [[title, content]]  # Create a new entry for the author
        print(blogs)
        return jsonify({"message": "Blog added successfully!"}), 200
    else:
        return jsonify({"error": "Author, title, and content are required!"}), 400

# Route to handle questions using ChatGPT API
@app.route('/ask_blog', methods=['POST'])
def ask_blog():
    data = request.json
    author = data.get('author')
    title = data.get('title')  # Get the title as well
    question = data.get('question')

    if author and title and question:
        # Create a prompt based on the author's blogs and question
        if author in blogs:
            # Filter blogs by title
            filtered_blogs = [content for t, content in blogs[author] if t == title]
            if filtered_blogs:
                blog_content = " ".join(filtered_blogs)  # Use only the specific blog content
                prompt = f"The user is asking a question about the blog titled '{title}' written by {author}: {blog_content}. The question is: {question}"
            else:
                prompt = f"The user is asking a question about the title '{title}' but no such blog exists by {author}. The question is: {question}"
        else:
            prompt = f"The user is asking a question: {question}"

        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on blog content."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the answer from the response
        answer = response.choices[0].message.content
        return jsonify({"answer": answer}), 200

    else:
        return jsonify({"error": "Author, title, and question are required!"}), 400
@app.route('/explore', methods=['GET'])
def explore_page():
    return render_template('explore.html', blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)
