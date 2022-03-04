from flask import Flask, Blueprint, render_template, request, redirect
import twitter
main = Blueprint('main', __name__)
from even_better_markov_chain import generate_tweet

@main.route('/')
def home_page():
  tweet = generate_tweet()
  return render_template('base.html', tweet=tweet)

@main.route('/tweet', methods=['POST'])
def tweet():
  new_tweet = request.form['tweet']
  print(new_tweet)
  twitter.tweet(new_tweet)
  return redirect('/')