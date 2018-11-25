import os

from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash

from Descriptor.miner import TextMiner
from Descriptor.descriptor import FoodDescriptor



UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """Check correctness of filename
    
    Arguments
        filename : str
            Name of uploaded image
        
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def mine_text(path_to_text_image):
    """"""
    image_text_miner = TextMiner()
    food_desc = FoodDescriptor()
    result = image_text_miner.get_text(path_to_image=path_to_text_image)
    description = food_desc.get_description(text=result['result'])
    return description


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('result', filename=filename))

    return render_template('index.html')


@app.route('/result')
def result(filename):
    # TODO: get path to text image
    # description = mine_text(path_to_text_image=filename)
    # TODO: put description into table from html
    return filename# render_template('result.html')




if __name__ == '__main__':
    app.run(debug=True)
