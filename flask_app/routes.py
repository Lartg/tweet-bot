from flask import Flask, Blueprint, render_template
main = Blueprint('main', __name__)
from even_better_markov_chain import generate_tweet

@main.route('/')
def home_page():
  tweet = generate_tweet()
  return render_template('base.html', tweet=tweet)