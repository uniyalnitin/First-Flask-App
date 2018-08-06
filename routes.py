from app import app
from flask import jsonify, render_template, redirect, url_for
from app.scrapping import scrape
from app.forms import SearchForm


@app.route('/', methods=['Get','Post'])
def index():
	# form = SearchForm()
	# items=''
	jobs= scrape()
	l=[]
	form = SearchForm()
	if form.validate_on_submit():
		what = form.what.data
		where = form.where.data
		for job in jobs:
			if job["title"].lower()==what.lower() and where.lower() in job["location"].lower():
				l.append(job)
		return render_template('search.html',title='search',jobs=l, form=form)
	# return jobs
		# return render_template('search.html',title='Home',form=form, items=items)
	return render_template('search.html',title='Home',jobs=jobs, form=form)

# @app.route('/search')
# def search():

