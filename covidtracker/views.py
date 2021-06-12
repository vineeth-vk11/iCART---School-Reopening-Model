from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.apps import apps
from .forms import inputform
from .school_reopening_model_new import *
import matplotlib.pyplot as plt
import pandas as pd
import urllib
import base64
import io
from keyring.backends import null


def home(request):
    form = inputform(request.POST)
    if request.method == 'POST':
        form = inputform(request.POST)
        if form.is_valid():
            student_no = int(form['student_no'].value())
            student_age_limit = form['student_age_limit'].value().split(";")
            student_age_lower_limit = int(student_age_limit[0])
            student_age_upper_limit = int(student_age_limit[1])
            teacher_no = int(form['teacher_no'].value())
            teacher_age_limit = form['teacher_age_limit'].value().split(";")
            teacher_age_lower_limit = int(student_age_limit[0])
            teacher_age_upper_limit = int(student_age_limit[1])
            non_teacher_no = int(form['non_teacher_no'].value())
            non_teacher_age_limit = form['non_teacher_age_limit'].value().split(
                ";")
            non_teacher_age_lower_limit = int(student_age_limit[0])
            non_teacher_age_upper_limit = int(student_age_limit[1])
            batch_size = int(form['batch_size'].value())
            infection = float(form['infection'].value())
            sensitivity = float(form['sensitivity'].value())
            specificity = float(form['specificity'].value())

            print(student_no, teacher_no, non_teacher_no, student_age_lower_limit,
                  student_age_upper_limit, batch_size, teacher_age_lower_limit, teacher_age_upper_limit, non_teacher_age_lower_limit,
                  non_teacher_age_upper_limit, infection, sensitivity, specificity)

            t, S, E, I, R = generateOutput(student_no, teacher_no, non_teacher_no, student_age_lower_limit,
                                           student_age_upper_limit, batch_size, teacher_age_lower_limit, teacher_age_upper_limit, non_teacher_age_lower_limit,
                                           non_teacher_age_upper_limit, infection, sensitivity, specificity)

            plt.semilogy(t, S, label='Susceptible')
            plt.semilogy(t, E, label='Exposed')
            plt.semilogy(t, I, label='Infected')
            plt.semilogy(t, R, label='Recovered')
            plt.legend()
            # sim.display(time=1)
            fig = plt.gcf()
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)
            return render(request, 'home.html', {'form': form, 'data': uri})
    return render(request, 'home.html', {'form': form})
