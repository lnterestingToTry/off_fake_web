from flask import Flask, render_template, request, jsonify, url_for, redirect
from loguru import logger
import db_init
from handlers import get_answer


app = Flask(__name__)


@app.route("/start")
def start():
    return redirect(url_for('query'))


@app.route("/query", methods=['GET', 'POST'])
async def query():
    if request.method == 'POST':
        query = request.form.get('query')

        answer = await get_answer(query)
        logger.info(answer)

        answer = f"{answer}"

        if answer != None:
            return render_template("query.html", query=query, answer=answer)
    return render_template("query.html")