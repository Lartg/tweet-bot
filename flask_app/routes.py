from flask import Flask, Blueprint, render_template
from text_to_list import text_to_list
from listogram import Listogram
main = Blueprint('main', __name__)

histogram = Listogram(text_to_list('text.txt'))

@main.route('/')
def home_page():
  word = histogram.sample()
  return render_template('base.html', word=word)