from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for posts
posts = []

# Homepage with career options and search bar
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Route to handle search
@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    filtered_posts = [post for post in posts if query in post['content'].lower()]
    return render_template('index.html', posts=filtered_posts, query=query)

# Route to handle posting
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            posts.append({'content': content})
        return redirect(url_for('index'))
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)