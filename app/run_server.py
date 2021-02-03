# USAGE
# Start the server:
# 	python run_front_server.py
# Submit a request via Python:
#	python simple_request.py

# import the necessary packages
import dill
import pandas as pd
import os
dill._dill._reverse_typemap['ClassType'] = type
#import cloudpickle
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

# initialize our Flask application and the model
app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_model(model_path):
	# load the pre-trained model
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)
	print(model)


modelpath = "/app/app/models/regressor_autoru_pipeline.dill"
load_model(modelpath)


@app.route("/", methods=["GET"])
def general():
	return """Welcome to fraudelent prediction process. Please use 'http://<address>/predict' to POST"""


@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}
	dt = strftime("[%Y-%b-%d %H:%M:%S]")
	# ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":

		privod = ''
		auto_class = ''
		price_segment = ''
		rul = ''
		vendor = ''
		ptc = ''
		seller_type = ''
		section = ''
		fuelType = ''
		numberOfDoors = ''
		vehicleTransmission = ''
		color = ''
		brand = ''
		model_name=''
		engineDisplacement=''
		enginePower=''
		mileage=''
		modelDate=''
		productionDate=''

		request_json = flask.request.get_json()
		if request_json["Привод"]:
			privod = request_json['Привод']
		if request_json["auto_class"]:
			auto_class = request_json['auto_class']
		if request_json["price_segment"]:
			price_segment = request_json['price_segment']

		if request_json["Руль"]:
			rul = request_json['Руль']
		if request_json["vendor"]:
			vendor = request_json['vendor']
		if request_json["ПТС"]:
			ptc = request_json['ПТС']
		if request_json["seller_type"]:
			seller_type = request_json['seller_type']
		if request_json["section"]:
			section = request_json['section']

		if request_json["fuelType"]:
			fuelType = request_json['fuelType']
		if request_json["numberOfDoors"]:
			numberOfDoors = request_json['numberOfDoors']
		if request_json["vehicleTransmission"]:
			vehicleTransmission = request_json['vehicleTransmission']
		if request_json["color"]:
			color = request_json['color']
		if request_json["brand"]:
			brand = request_json['brand']
		if request_json["model_name"]:
			model_name = request_json['model_name']

		if request_json["engineDisplacement"]:
			engineDisplacement = request_json['engineDisplacement']
		if request_json["enginePower"]:
			enginePower = request_json['enginePower']
		if request_json["mileage"]:
			mileage = request_json['mileage']
		if request_json["modelDate"]:
			modelDate = request_json['modelDate']
		if request_json["productionDate"]:
			productionDate = request_json['productionDate']

		logger.info(f'{dt} Data: Привод={privod}, auto_class={auto_class}, price_segment={price_segment}')

		try:
			preds = model.predict(pd.DataFrame({"Привод": [privod],
												"auto_class": [auto_class],
												"price_segment": [price_segment],
												"Руль": [rul],
												"vendor": [vendor],
												"ПТС": [ptc],
												"seller_type": [seller_type],
												"section": [section],
												"fuelType": [fuelType],
												"numberOfDoors": [numberOfDoors],
												"vehicleTransmission": [vehicleTransmission],
												"color": [color],
												"brand": [brand],
												"model_name": [model_name],
												"engineDisplacement": [engineDisplacement],
												"enginePower": [enginePower],
												"mileage": [mileage],
												"modelDate": [modelDate],
												"productionDate": [productionDate]
												}))
		except AttributeError as e:
			logger.warning(f'{dt} Exception: {str(e)}')
			data['predictions'] = str(e)
			data['success'] = False
			return flask.jsonify(data)

		data["predictions"] = preds[:, 1][0]
		# indicate that the request was a success
		data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server


if __name__ == "__main__":
	print(("* Loading the model and Flask starting server..."
		"please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8180))
	app.run(host='0.0.0.0', debug=True, port=port)
