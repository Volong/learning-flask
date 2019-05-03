#coding=utf8


from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_script import Manager
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):

	# StringField 类表示属性为 type="text" 的 <input> 元素
	# 可选参数 validators 指定一个由验证函数组成的列表,验证函数 Required() 确保提交的字段不为空
	name = StringField('what is your name?', validators=[Required()])
	# SubmitField 类表示属性为 type="submit" 的 <input> 元素
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()

	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name)

if __name__ == '__main__':
	manager.run()