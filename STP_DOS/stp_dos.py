import flask
from flask_classful import route
from flask import request
from app_base import AppBase
from models.DBManager import DBManager
from utils import AppUtils


class STP_DOS(AppBase):
    @route("attaque", methods=["GET", "POST"])
    def attaque():
        content = request.json
        post_data = content
        result = DBManager.stp_dos.insert_one(post_data)
        print("One post: {0}".format(result.inserted_id))
        return flask.Response({"Attaque": "True"})

    @route("response", methods=["GET", "POST"])
    def response():
        content = request.json
        data_html = content["Response"]
        post_data = content
        result = DBManager.stp_dos.insert_one(post_data)
        data_html = str(data_html)
        id_rapport = result.inserted_id
        AppUtils.generateRapportPdf("STP_Dos.html", "STP_Dos", data_html, id_rapport)
        print("One post: {0}".format(result.inserted_id))
        return flask.Response({"Response": "True"})

    @route("list", methods=["GET", "POST"])
    def list():
        x = DBManager.stp_dos.find()
        return AppUtils.jsonEncode([todo for todo in x])