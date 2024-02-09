from flask import Flask, render_template, request
import codecs
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<filename>')

def display_file(filename='file1.txt'):
    start_line = request.args.get('start')
    end_line = request.args.get('end')

    try:
        with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.read()
            if start_line and end_line:
                lines = lines[int(start_line)-1:int(end_line)]
            content = ''.join(lines)
            return render_template('display.html', content=content, filename=filename)
    except FileNotFoundError:
        return render_template('error.html', error='File not found.')
    except Exception as e:
        return render_template('error.html', error=str(e))
    
if __name__ == '__main__':
    app.run(debug=True)