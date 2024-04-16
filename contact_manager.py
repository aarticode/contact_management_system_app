# contact_manager.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Global variable to store contacts
contacts = [
    {"name": "johndoe", "phone": "123-456-7890", "email": "john@example.com"},
    {"name": "Jane Smith", "phone": "987-654-3210", "email": "jane@example.com"}
]


# Function to add a new contact
def add_contact(name, phone, email):
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)

# Function to delete a contact
def delete_contact(name):
    global contacts
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)

# Function to search for a contact
def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

# Function to display all contacts
def display_contacts():
    return contacts

# Main route
@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

# Add contact route
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    add_contact(name, phone, email)
    return redirect('/')

# Delete contact route
@app.route('/delete/<name>')
def delete(name):
    delete_contact(name)
    return redirect('/')

# Search contact route
@app.route('/search', methods=['POST'])
def search():
    name = request.form['name']
    contact = search_contact(name)
    return render_template('search.html', contact=contact)

if __name__ == '__main__':
    app.run(debug=True)

