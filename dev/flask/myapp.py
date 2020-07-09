import os
from flask import Flask, render_template, request, redirect, url_for

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = b'random string...'

Base = declarative_base()

Engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=Engine)

class Paper(Base):
    __tablename__ = 'papers'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    citation_number = Column(Integer())

    def to_dict(self):
        return {
            'id': int(self.id),
            'title': str(self.title),
            'author': str(self.author),
            'citation_number': int(self.citation_number)
        }


@app.route('/', methods=['GET'])
def index():
    ses = Session()
    data = ses.query(Paper).all()
    ses.close()
    return render_template(
        'index.html',
        title='Papers',
        data=data
    )


@app.route('/add', methods=['POST'])
def add_record():
    title = request.form.get('title')
    author = request.form.get('author')
    citation_number = request.form.get('citation_number')
    new_paper = Paper(title=title, author=author,
                      citation_number=citation_number)
    ses = Session()
    ses.add(new_paper)
    ses.commit()
    ses.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
