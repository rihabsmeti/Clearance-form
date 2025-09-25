from flask import Flask, request, redirect, render_template
import pandas as pd

app = Flask(__name__)

# Load Excel file
df = pd.read_excel("Database.xlsx")


@app.route("/")
def home():
    # Show the login page first
    return render_template("Login_page.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email").strip().lower()

    # Look up email in Excel
    user = df[df["Email"].str.lower() == email]

    if not user.empty:
        role = user.iloc[0]["Role"].strip().lower()

        # Redirect to correct page based on role
        if role == "students":
            return render_template("Students.html")
        elif role == "staff":
            return render_template("Staff.html")
        elif role == "security":
            return render_template("Security.html")
        elif role == "bill":
            return render_template("Bill.html")
        else:
            return f"Role '{role}' not recognized"
    else:
        return "Email not found. Please try again."


if __name__ == "__main__":
    app.run(debug=True)
