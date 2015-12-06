#-*-coding:utf-8
from flask import Flask, session, redirect, url_for, request, render_template

#server setting
app = Flask(__name__)
app.secret_key = 'adfjlksjfjsdjfkjskljfsd'

@app.route('/')
def main_page () :
	return render_template('main.html')


@app.route('/jing')
def show_jing_id() :
	return 'jing id'


@app.route('/ppu/<int:ppu_id>')
def show_ppu (ppu_id) :
	print (ppu_id)
	return render_template('naver_id.html', ppu_id=ppu_id)


@app.route('/user', methods=['GET'])
def get_user_form () :
	return render_template('user_form.html')


@app.route('/user', methods=['POST'])
def user_create () :
	user_name = 'none'
	if request.method == 'POST' :
		user_name = request.form['user-name']
	return show_user_name(user_name)


def show_user_name (user_name) :
	return render_template('Hello_world.html', user_name=user_name)

# server start
if __name__ == "__main__" :
	app.run(host='127.0.0.1', port=3000)