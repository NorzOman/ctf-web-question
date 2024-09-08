from flask import Flask, render_template, send_from_directory, request, Response, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management, if needed

@app.route('/')
def index():
    # Check if there's an error message to display
    error_message = request.args.get('error')
    return render_template('index.html', error_message=error_message)

@app.route('/h1dden-page', methods=['GET', 'HEAD'])
def h1dden_page():
    if request.method == 'HEAD':
        response = Response('', status=200)
        response.headers['X-Custom-Header'] = 'Hmm this website is too much to maintain imma keep my first part of flag here "n0t_" , the rest? imma give it when admin contacts me on website'
        return response

    user_agent = request.headers.get('User-Agent')
    
    if user_agent == 'DJ-Browser':
        return render_template('cookie_in_return.html')
    
    flat_earth = request.cookies.get('flat-earth')
    if flat_earth == 'true':
        return render_template('error_ig.html')

    return render_template('access-denied_agent.html')

@app.route('/contactus', methods=['POST'])
def contactus():
    name = request.form.get('name')
    email = request.form.get('email')
    telephone = request.form.get('telephone')
    message = request.form.get('message')

    if name == 'admin' and email == 'ad1min7789@gmail.com':
        # Render response.txt if the admin credentials match
        return render_template('message-for-admin.html')

    if name == 'admin':
            return redirect(url_for('index', error='Oops! Wrong email for admin. Remember, our mail database was leaked. I announced it too') + '#contactus')
    # Redirect to index page with error message in query parameters
    return redirect(url_for('index', error='Due to website limitation we only accept feedback from admin') + '#contactus')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory('static', 'robots.txt')

if __name__ == '__main__':
    app.run(debug=True)
