import MySQLdb
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import shoppingtrends
import openai
from langchain.prompts import ChatPromptTemplate
from langchain.utilities import SQLDatabase


# Create your views here.

db_user = "root"
db_pass = "root"
db_host = "127.0.0.1"
db_name = "datafy_db"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}")

openai_api_key='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'
openai.api_key = openai_api_key

def home(request):
    return render(request, "index.html")


def ask_openai(message):
    response = openai.chat.completions.create(
        model = "gpt-4",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

def chat(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message,'response':response})
    return render(request, 'chat.html')


def readdb():
    all_entrys = shoppingtrends.objects.all
    info=[ all_entrys ]


def get_schema(_):
   return db.get_table_info()
