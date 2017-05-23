from flask import Blueprint, redirect, render_template, request, url_for
#import our model Owner
from project.cars.models import Car
from project.cars.forms import CarForm
from project import db

cars_blueprint = Blueprint(
    'cars',
    __name__,
    template_folder='templates'
)

@cars_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = CarForm(request.form)
        if form.validate():
            new_car = Car(request.form['model'], request.form['owner_id'])
            db.session.add(new_car)
            db.session.commit()
            return redirect(url_for('cars.index'))
        else:
            return render_template('cars/new.html', form=form)
    return render_template('cars/index.html', cars = Car.query.all())

@cars_blueprint.route('/new')
def new():
    form = CarForm(request.form)
    return render_template('cars/new.html', form=form)

@cars_blueprint.route('/<int:id>/edit')
def edit(id):
    found_car = Car.query.get(id)
    form = CarForm(obj=found_car)
    return render_template('cars/edit.html', form=form, car=found_car)

@cars_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    found_car = Car.query.get(id)
    if request.method == b'PATCH':
        form = CarForm(request.form)
        if form.validate():
            found_car.model = request.form['model']
            found_car.owner_id = request.form['owner_id']
            db.session.add(found_car)
            db.session.commit()
            return redirect(url_for('cars.index'))
        else:
            return render_template('cars/edit.html', form=form, car=found_car)
    if request.method == b'DELETE':
        db.session.delete(found_car)
        db.session.commit()
        return redirect(url_for('cars.index'))
    return render_template('cars/show.html', car=found_car)
