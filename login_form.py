from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <html>
    <head>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .login-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(15px);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                color: white;
                width: 320px;
                text-align: center;
            }
            .login-card h2 {
                margin-bottom: 20px;
            }
            .login-card input[type="text"], 
            .login-card input[type="password"] {
                width: 100%;
                padding: 12px;
                margin-bottom: 15px;
                border: none;
                border-radius: 10px;
                outline: none;
                font-size: 16px;
                background: rgba(255, 255, 255, 0.2);
                color: #fff;
            }
            .login-card input[type="submit"] {
                width: 100%;
                padding: 12px;
                border: none;
                border-radius: 10px;
                background-color: #ffffff;
                color: #764ba2;
                font-weight: bold;
                cursor: pointer;
                font-size: 16px;
                transition: background-color 0.3s ease;
            }
            .login-card input[type="submit"]:hover {
                background-color: #e0e0e0;
            }
            ::placeholder {
                color: #e0e0e0;
            }
        </style>
    </head>
    <body>
        <div class="login-card">
            <h2>Welcome Back</h2>
            <form method="post" action="/login">
                <input type="text" name="username" placeholder="Username"><br>
                <input type="password" name="password" placeholder="Password"><br>
                <input type="submit" value="Login">
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'Chandrakant' and password == 'chand123':
        return '''
        <html>
        <head>
            <style>
                body {
                    background: linear-gradient(135deg, #56ab2f, #a8e063);
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    color: white;
                }
                .result-box {
                    text-align: center;
                    background: rgba(255, 255, 255, 0.1);
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
                    backdrop-filter: blur(10px);
                }
                .icon {
                    font-size: 60px;
                    margin-bottom: 20px;
                    animation: pop 0.5s ease;
                }
                @keyframes pop {
                    0% { transform: scale(0); }
                    100% { transform: scale(1); }
                }
                h1 {
                    margin: 0;
                    font-size: 28px;
                }
            </style>
        </head>
        <body>
            <div class="result-box">
                <div class="icon">!!!!</div>
                <h1>Login Successful</h1>
                <p>Welcome, Chandrakant! You have successfully logged in.</p>
            </div>
        </body>
        </html>
        '''
    else:
        return '''
        <html>
        <head>
            <style>
                body {
                    background: linear-gradient(135deg, #ff4e50, #f9d423);
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    color: white;
                }
                .result-box {
                    text-align: center;
                    background: rgba(255, 255, 255, 0.1);
                    padding: 40px;
                    border-radius: 20px;
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
                    backdrop-filter: blur(10px);
                }
                .icon {
                    font-size: 60px;
                    margin-bottom: 20px;
                    animation: pop 0.5s ease;
                }
                @keyframes pop {
                    0% { transform: scale(0); }
                    100% { transform: scale(1); }
                }
                h1 {
                    margin: 0;
                    font-size: 28px;
                }
            </style>
        </head>
        <body>
            <div class="result-box">
                <div class="icon"></div>
                <h1>Login Failed</h1>
                <p>Invalid username or password. Please try again.</p>
            </div>
        </body>
        </html>
        ''', 401

if __name__ == '__main__':
    app.run(debug=True, port=8080)
