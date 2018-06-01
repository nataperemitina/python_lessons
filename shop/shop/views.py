from flask import (
    request, render_template,
    redirect, abort, url_for
)
from pony.orm import ObjectNotFound

from . import app
from .forms import CustomerForm
from .model import Customer


@app.route('/registration')
def registration():
    form = CustomerForm(request.form)

    if form.validate_on_submit():
        customer = Customer(email=form.email.data,
                            phone=form.phone.data,
                            name=form.name.data)
        return redirect(url_for('registration'))

    return render_template('registration.html', form=form)








