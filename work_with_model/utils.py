from transformers import pipeline


def make_predictions(text):
    pipe = pipeline("text-classification", model="gordovaa/my_awesome_model")
    ans = pipe(text)[0]
    if ans['label'] == 'POSITIVE':
        print(ans['label'])
        star = round(ans['score'], 1)
        star *= 10
        star = int(star)
        print(star)
    else:
        print(ans['label'])
        star = round(1-ans['score'], 1)
        star *= 10
        if star == 0.0:
            star = 1.0
        star = int(star)
        print(star)


text = "There is a lot of ambiguity"

make_predictions(text)