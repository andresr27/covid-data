#!/usr/bin/python3
import ccy
from flask import Flask, render_template, abort, request
from momentjs import momentjs
app = Flask(__name__)
# Set jinja template global
app.jinja_env.globals['momentjs'] = momentjs

VISUALS = {
    '1': {
        'name': 'Name Visual 1',
        'category': 'Category 1',
        'value': 99,
    },
    '2': {
        'name': 'Name Visual 2',
        'category': 'Category 2',
        'value': 649,
    }
}


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', visuals=VISUALS)

@app.route('/visual/<key>')
def visual(key):
    visual = VISUALS.get(key)
    if not visual:
        abort(404)
    return render_template('visual.html', visual=visual)

@app.context_processor
def some_processor():
    def full_name(visual):
        return '{0} / {1}'.format(visual['category'], visual['name'])
    return {'full_name': full_name}

@app.template_filter('full_name')
def full_name_filter(visual):
    return '{0} / {1}'.format(visual['category'], visual['name'])

# @app.template_filter('format_currency')
# def format_currency_filter(amount):
#     currency_code = ccy.countryccy(request.accept_languages.best[-2:])
#     return '{0} {1}'.format(currency_code, amount)
