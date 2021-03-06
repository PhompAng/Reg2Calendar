from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadText, convert2calendar, get_time, create_csv_download

import csv

def index(request):
    if request.method == 'POST':
        form = UploadText(request.POST)
        if form.is_valid():
            data = convert2calendar(form.cleaned_data['regHtml'])
            open_day = form.cleaned_data['open_date_semester']
            end_day = form.cleaned_data['end_date_semester']

            content = create_csv_download(open_day, end_day, data)

            response = HttpResponse(content_type='text/ics')
            response['Content-Disposition'] = 'attachment; filename="export.ics"'
            response.write(content)
            return response

    else:
        form = UploadText()
    return render(request, 'genclass/index.html', {'form': form})