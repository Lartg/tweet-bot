from flask import Flask, Blueprint, render_template
from sample import sample_word
from histogram import histogram
main = Blueprint('main', __name__)

@main.route('/')
def home_page():
  corpus = None
  with open('text.txt', 'r') as c:
    corpus = c.read()
  
  
  return render_template('base.html', word=sample_word(histogram(corpus)[0]))