from flask import Flask, render_template, request,session,jsonify
from crypto_utils import encrypt_data,decrypt_data
import json
import os
from PIL import Image
import random
import hashlib
from datetime import datetime

app = Flask(__name__)
app.secret_key="secret123"

# Create users.json if not exists
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        f.write("{}")

# Load users
def load_users():
    with open("users.json") as f:
        return json.load(f)

# Save users
def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

# ================= HOME =================
@app.route('/')
def home():
    return render_template("login.html")

# ================= REGISTER =================
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        users = load_users()

        username = request.form['username'].strip()
        password = request.form['password']

        typing_data = json.loads(request.form['typingData'])
        mouse_data = int(request.form['mouseData'])

        image = request.files['bioimage']

        image_path = "static/" + image.filename

        image.save(image_path)

        img = Image.open(image_path)

        width, height = img.size

        points = []

        for i in range(5):

            x = random.randint(0, width - 1)

            y = random.randint(0, height - 1)

            points.append((x, y))

        print(points)

        combined_data = str(points)

        key = hashlib.sha256(combined_data.encode()).hexdigest()

        print("Generated Key:", key)

        users[username] = {

            "password": password,

            "typing": encrypt_data(typing_data),

            "mouse": encrypt_data(mouse_data),

            "key": key,
            "points": points
        }

        save_users(users)

        return "<h2>Registered Successfully ✅</h2><a href='/'>Go To Login</a>"

    return render_template("register.html")
# ================= LOGIN =================
@app.route('/login', methods=['POST'])
def login():

    users = load_users()

    username = request.form['username'].strip()
    password = request.form['password']

    # typing timings from browser
    typing_data = json.loads(request.form['typingData'])

    # mouse movement count
    mouse_data = int(request.form['mouseData'])
    image = request.files['bioimage']

    image_path = "static/" + image.filename

        
    points=users[username]["points"]

    print(points)
    
    new_key=users[username]["key"]

    print("Login Key:", new_key)

    # Check user exists
    if username not in users:
        return "<h2>User Not Found ❌</h2>"

    # Check password
    if users[username]["password"] != password:
        return "<h2>Wrong Password ❌</h2>"

    # ===== STORED DATA =====
    old_typing = decrypt_data(users[username]["typing"])
    old_mouse = decrypt_data(users[username]["mouse"])
    stored_key=users[username]["key"]

    # ===== CALCULATE AVERAGES =====
    old_avg = sum(old_typing) / len(old_typing)
    new_avg = sum(typing_data) / len(typing_data)

    # ===== DIFFERENCES =====
    typing_difference = abs(old_avg - new_avg)
    mouse_difference = abs(old_mouse - mouse_data)

    print("Typing Difference:", typing_difference)
    print("Mouse Difference:", mouse_difference)

    # ===== FINAL CHECK =====
    stored_key=users[username]["key"]
    new_key=users[username]["key"]
    if new_key==stored_key:
        session['user']=username
        return render_template("dashboard.html", user=username)

    else:
        with open("intruder_log.txt","a") as f:
            f.write(f"Intruder detected for user: {username} at {datetime.now()}\n")
        return "<h1 style='color:red'>Intruder Detected ❌</h1>"
# ================= RUN =================
@app.route('/monitor', methods=['POST'])
def monitor():

    if 'user' not in session:
        return jsonify({"status":"intruder"})

    username = session['user']

    users = load_users()

    data = request.get_json()

    current_mouse = data['mouse']
    current_typing = data['typing']

    old_mouse = decrypt_data(users[username]['mouse'])
    old_typing = decrypt_data(users[username]['typing'])

    # typing average
    if len(current_typing) == 0:
        current_avg = 0
    else:
        current_avg = sum(current_typing) / len(current_typing)

    old_avg = sum(old_typing) / len(old_typing)

    typing_difference = abs(old_avg - current_avg)

    mouse_difference = abs(old_mouse - current_mouse)

    print("Continuous Check")
    print("Typing Difference:", typing_difference)
    print("Mouse Difference:", mouse_difference)

    # ===== FINAL CHECK =====
    if typing_difference > 100 or mouse_difference > 500:

        session.clear()

        return jsonify({"status":"intruder"})

    return jsonify({"status":"ok"})
if __name__ == '__main__':
    app.run(debug=True)