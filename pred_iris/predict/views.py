from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
from sklearn.datasets import load_iris, load_breast_cancer
import pickle
from .forms import PredForms

# Create your views here.

def predict(request):
    if request.method == "POST":
        form = PredForms(request.POST)
        if form.is_valid():
            sl = form.cleaned_data.get('sepal_length')
            pl = form.cleaned_data.get('petal_length')
            sw = form.cleaned_data.get('sepal_width')
            pw = form.cleaned_data.get('petal_width')

            iris = load_iris()
            df = pd.DataFrame(iris.data, columns=iris.feature_names)
            X = df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
            y = iris.target
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

            model = SVC()

            model.fit(X_train, y_train)
            predict = model.predict(X_test)
            filename = "pred.sav"

            pickle.dump(model, open(filename, 'wb'))

            load_model = pickle.load(open(filename, 'rb'))

            target_names = iris.target_names

            result = load_model.predict([[sl, sw, pl, pw]])

            answer = target_names[result[0]]

            accu = load_model.score(X_test,y_test)

            accuracy = accu * 100





            return render(request,'answer.html', {'sl':answer, 'accu':accuracy})
        else:
            form = PredForms()
            return render(request, 'predict.html', {'form': form})

    form = PredForms()
    return render(request, 'predict.html', {'form':form})

