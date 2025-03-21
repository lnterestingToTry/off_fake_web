from flask import Flask, render_template, request, jsonify, url_for, redirect
from loguru import logger
import db_init
from handlers import get_answer


app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        query = request.form.get('query')

        logger.info(query)
        
        answer = get_answer(query)
        logger.info(answer)

        kwargs =    {  
                    'query': query,
                    'answer': answer
                    }

        if answer != None:
            return render_template(template_name_or_list="index.html", **kwargs)

    query = request.form.get('query')
    
    
    answer = {}
    
    
    kwargs =    {  
        'query': query,
        'answer': answer
        }
    
    return render_template(template_name_or_list="index.html", **kwargs)