from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import HomeForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from accounts.models import Post
import json
from http.client import HTTPConnection

def request_mediator(host, head):
    connection = HTTPConnection(host)
    request = connection.request("GET", "/", headers=head)
    response = connection.getresponse()
    connection.close()
    rhead, rdata = response.getheaders(), response.read()
    return rhead, rdata

class GenReqID:
    _ID = 0
    def next(self):
        GenReqID._ID += 1
        return GenReqID._ID

class Homeview(TemplateView):
    template_name='accounts/login.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['my_mathy_paragraph'] = my_mathy_paragraph
        return context

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            #here we are getting the list of the availiable tasks

            #rhead, rdata = request_mediator("127.0.0.1:25800", head={"request": "get_taskList", "reqID": GenReqID.next()})
            #rdata = b'[{"task_ID": "1", "des": "ololo1"}, {"task_ID": "5", "des": "ololo_strabacaba2"}]'
            #rdata = json.loads(rdata)
            tasklist = ''

            #for it in rdata:
            #    tasklist += it["task_ID"] + ':' + it["des"] + '||'

            #end of it



            text = form.cleaned_data['post']
            # here we are getting tasks
            text = text.split(' ')
            temp = ['', '', '', '', '']
            for it in text:
                # rhead, rdata = request_mediator("127.0.0.1:25800", head={"request": "get_task", "reqID": GenReqID.next(), "taskID": text[it})
                #temp[it] = str(rdata)

            text1 = temp[0]
            text2 = temp[1]
            text3 = temp[2]
            text4 = temp[3]
            text5 = temp[4]

            # end of it

            new = '''
            {
                "GlossSeeAlso": "1"
            }
            '''
            data = json.loads(new)
            data['GlossSeeAlso'] = text
            text= str(data['GlossSeeAlso'])
            form = HomeForm()
            #return redirect('/account')
        args = {'form': form, 'text': text, 'tasklist': tasklist, 'text1': text1, 'text2': text2, 'text3': text3, 'text4': text4, 'text5': text5}

        return render(request, self.template_name, args)
