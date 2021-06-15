from flask import Flask, render_template
from dotenv import load_dotenv
from flask_restful import Api
from flask_cors import CORS
from threading import Thread
from main import create_app
