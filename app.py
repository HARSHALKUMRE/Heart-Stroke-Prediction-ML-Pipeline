from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS, cross_origin
from heart_stroke.exception import HeartStrokeException
from heart_stroke.logger import logging
from heart_stroke.constant.application import APP_HOST, APP_PORT
from heart_stroke.pipeline.prediction_pipeline import HeartData, HeartStrokeClassifier
from heart_stroke.pipeline.training_pipeline import TrainingPipeline

application = Flask(__name__)
app = application

@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:

        heartstroke_data = HeartData(
            gender = request.form.get('gender'),
            age = int(request.form.get('age')),
            hypertension = int(request.form.get('hypertension')),
            heart_disease = int(request.form.get('heart_disease')),
            ever_married = request.form.get('ever_married'),
            work_type = request.form.get('work_type'),
            Residence_type = request.form.get('Residence_type'),
            avg_glucose_level = request.form.get('avg_glucose_level'),
            bmi = float(request.form.get('bmi')),
            smoking_status = request.form.get('smoking_status')
        )

        heartstroke_df = heartstroke_data.get_heart_stroke_input_data_frame()

        print(heartstroke_df)

        model_predictor = HeartStrokeClassifier()

        stroke_value = model_predictor.predict(dataframe=heartstroke_df)[0]

        if stroke_value == 1:
            results = "High chance of Heart stroke"
             
        else:
            results =  "Low chance of Heart stroke"

        return render_template('index.html', results=results, heartstroke_df=heartstroke_df)


@app.route("/train")
@cross_origin()
def trainRoute():
    try:
        pipeline = TrainingPipeline()

        pipeline.run_pipeline()
        
        return Respone("Training successful !!")

    except Exception as e:
        return Response(f"Error Occured ! {e}")

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)

