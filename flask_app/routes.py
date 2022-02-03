from flask import Flask, Blueprint, render_template
from sample import sample_word
from histogram import histogram
main = Blueprint('main', __name__)

@main.route('/')
def home_page():
  with open('text.txt', 'r') as c:
    corpus = c.read()
  hist_and_count = histogram(corpus)
  return render_template('base.html', word=sample_word(hist_and_count[0],hist_and_count[1]))