#import os
from crypt import methods
from curses.ascii import isalpha
from flask import Flask, render_template
#from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
#from flask_session import Session
#from tempfile import mkdtemp
#from werkzeug.security import check_password_hash, generate_password_hash
#import datetime
from key_generator import WithoutRepeat
from encryption import encryption
import tkinter
from tkinter import messagebox
import string
import random


str(gen_key) = WithoutRepeat(26)

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route('/')
def index():
     return render_template("index.html")


@app.route("/encrypt", methods = ["GET", "POST"])
def encrypt_page():
    if request.method == "GET":
       return render_template("encryption.html")
    else:
        text_autogen = request.form.get("text_autogen")
        if not text_autogen.isalpha()
            root = tkinter.Tk()
            root.withdraw()

            # Message Box
            messagebox.showinfo("Alert", "Only characters acceptiable")

        gen_key = WithoutRepeat(26)
        
        return render_template("encryption.html", generated_key=gen_key)

@app.route("/decrypt")
def decrypt_page():
    return render_template("decryption.html")

@app.route("/login_register")
def login_register_page():
    return render_template("login_register.html")ß

#@app.route("/logout")
#def logout():
#    session.clear()
#    return redirect("/")