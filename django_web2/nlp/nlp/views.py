from django.shortcuts import render
from transformers import pipeline
from pathlib import Path


def index(request):
    return render(request, "base.html", {"prediction": "None"})


def prediction(request):
    '''
    BASE_DIR = Path(__file__).resolve().parent.parent
    premus = joblib.load(BASE_DIR / "premus/premus.joblib")
    gender, age = request.POST["gender"], request.POST["age"]
    prediction = premus.predict([[age, gender]])
    settings = {"gender": gender, "age": age}
    return render(request, "base.html", {"prediction": prediction[0], "settings": settings})'''

    text = request.POST["feedback"]
    pipe = pipeline("text-classification", model="gordovaa/my_awesome_model")
    ans = pipe(text)[0]
    if ans['label'] == 'POSITIVE':
        #print(ans['label'])
        w = 'положительный'
        star = round(ans['score'], 1)
        star *= 10
        star = int(star)
        #print(star)
    else:
        #print(ans['label'])
        w = 'отрицательный'
        star = round(1 - ans['score'], 1)
        star *= 10
        if star == 0.0:
            star = 1.0
        star = int(star)
        #print(star)
    l_star = '1'*star
    g_star = '1'*(10-star)
    settings = {"category": w, "star": star, "your_feedback": text, "l_star" : l_star, "g_star" : g_star}
    return render(request, "base.html", {"settings": settings})

