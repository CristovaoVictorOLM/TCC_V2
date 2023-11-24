import MySQLdb
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import shoppingtrends
import openai
from langchain.prompts import ChatPromptTemplate
from langchain.utilities import SQLDatabase
from dotenv import load_dotenv,find_dotenv
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from pymysql import connect
from sqlalchemy import create_engine





# Create your views here.

"""db_user = "root"
db_pass = "root"
db_host = "127.0.0.1"
db_name = "datafy_db"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}")"""

openai_api_key='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'
openai.api_key = openai_api_key

"""data_base = connect(host= '127.0.0.1',
                    user= 'root',
                    passwd= 'admin',)

cur = data_base.cursor()

query = 'show databases'

cur.execute(query)

data_base = cur.fetchall()"""






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
    data_base = connect(host = '127.0.0.1',
                    user = 'root',
                    passwd= 'admin',
                    database= 'datafy_db',)
    
    engine = create_engine(f"mysql+pymysql://root:admin@127.0.0.1/datafy_db")

    cur = data_base.cursor()
    query2='show tables'
    cur.execute(query2)

    tables = cur.fetchall()

    query3 = 'SELECT * from core_shoppingtrends'
    load_dotenv(find_dotenv())

    df=pd.read_sql(query3,engine)

    chat_02 = ChatOpenAI(model_name="gpt-4", temperature=0.0, openai_api_key = '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')
    agent = create_pandas_dataframe_agent(chat_02, df, verbose=True)
    
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_openai(message)
        definitve_response = agent.run(response)
        return JsonResponse({'message':message,'response':definitve_response})
    return render(request, 'chat.html')



def readdb():
    all_entrys = shoppingtrends.objects.all
    info=[ all_entrys ]


"""def get_schema(_):
   return db.get_table_info()"""




