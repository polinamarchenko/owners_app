from flask import Blueprint, redirect, render_template, request, url_for
#import our model Owner
from project.owners.models import Owner
from project.owners.forms import OwnerForm
from project.cars.models import Car

from project import db

owners_blueprint = Blueprint(
    'owners',
    __name__,
    template_folder='templates'
)

@owners_blueprint.route('/<int:id>/cars', methods=['GET', 'POST'])
def owner_cars(id):
    found_owner = Owner.query.get(id)
    return render_template('owners/cars.html', owner=found_owner)


@owners_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = OwnerForm(request.form)
        if form.validate():
            new_owner = Owner(request.form['first_name'], request.form['last_name'])
            db.session.add(new_owner)
            db.session.commit()
            return redirect(url_for('owners.index'))
        else:
            return render_template('owners/new.html', form=form)
    return render_template('owners/index.html', owners=Owner.query.all())

@owners_blueprint.route('/new')
def new():
    form = OwnerForm(request.form)
    return render_template('owners/new.html', form=form)

@owners_blueprint.route('/<int:id>/edit')
def edit(id):
    found_owner = Owner.query.get(id)
    form = OwnerForm(obj=found_owner)
    return render_template('owners/edit.html', form=form, owner=found_owner)

@owners_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    found_owner = Owner.query.get(id)
    if request.method == b'PATCH':
        form = OwnerForm(request.form)
        if form.validate():
            found_owner.first_name = request.form['first_name']
            found_owner.last_name = request.form['last_name']
            db.session.add(found_owner)
            db.session.commit()
            return redirect(url_for('owners.index'))
        else:
            return render_template('owners/edit.html', form=form, owner=found_owner)
    if request.method == b'DELETE':
        db.session.delete(found_owner)
        db.session.commit()
        return redirect(url_for('owners.index'))
    return render_template('owners/show.html', owner=found_owner)
