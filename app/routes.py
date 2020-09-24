from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import AddMachineForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/add_machine', methods=['GET', 'POST'])
def add_machine():
    form = AddMachineForm()
    if form.validate_on_submit():
        flash('Machine added')
        return redirect(url_for('index'))
    return render_template('add_machine.html', title='Add Machine', form=form)