import joblib
import os 

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

from wtforms import FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8hUljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    alcool                   = FloatField('Álcool:', validators=[DataRequired()])
    acido_malico             = FloatField('Ácido málico:', validators=[DataRequired()])
    cinza                    = FloatField('Cinza:', validators=[DataRequired()])
    alcalinidade_das_cinzas  = FloatField('Alcalinidade das cinzas:', validators=[DataRequired()])
    magnesio                 = FloatField('Magnésio:', validators=[DataRequired()])
    flavanoides_totais       = FloatField('Flavanóides Totais:', validators=[DataRequired()])
    flavanoides              = FloatField('Flavanóides:', validators=[DataRequired()])    
    fenois_nao_flavanoides   = FloatField('Fenóis não flavanoides:', validators=[DataRequired()])
    proantocianinas          = FloatField('Proantocianinas:', validators=[DataRequired()])
    intensidade_da_cor       = FloatField('Intensidade da cor:', validators=[DataRequired()])
    Matiz                    = FloatField('Matiz:', validators=[DataRequired()])
    OD280_OD315              = FloatField('OD280/OD315:', validators=[DataRequired()])
    Proline                  = FloatField('Proline:', validators=[DataRequired()])
    
@app.route('/', methods=['GET', 'POST'])
def index():
    form   = InputForm(request.form)
    classe = 'no-image'
    if form.validate_on_submit():
       x = [[form.alcool.data, 
             form.acido_malico.data,
             form.cinza.data, 
             form.alcalinidade_das_cinzas.data,
             form.magnesio.data,
             form.flavanoides_totais.data,
             form.flavanoides.data,
             form.fenois_nao_flavanoides.data,
             form.proantocianinas.data,
             form.intensidade_da_cor.data,
             form.Matiz.data,
             form.OD280_OD315.data,
             form.Proline.data]]
       classe = make_prediction(x)
           
    return render_template('index.html', form=form, classe=classe)

def make_prediction(x):
    filename = os.path.join('model', 'finalized_model.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]

if __name__ == '__main__':
    app.run()






