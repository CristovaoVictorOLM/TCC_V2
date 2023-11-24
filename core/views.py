import MySQLdb
import csv
import openai
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import shoppingtrends
from .forms import UploadCSVForm

from langchain.prompts import ChatPromptTemplate
from langchain.utilities import SQLDatabase
from io import TextIOWrapper,StringIO



# Create your views here.

db_user = "root"
db_pass = "root"
db_host = "127.0.0.1"
db_name = "datafy_db"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}")

openai_api_key=''
openai.api_key = openai_api_key

def home(request):
    return render(request, "index.html")

def processar_csv(request):
    if request.method == 'POST':
        print(request.POST)
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                # Crie uma instância do modelo e salve os dados do CSV
                if len(row) >= 18:
                    try:
                        shopping_instance = shoppingtrends.objects.create(
                            Customer_ID=row['Customer_ID'],
                            Age=row['Age'],
                            Gender=row['Gender'],
                            Item_Purchased=row['Item_Purchased'],
                            Category=row['Category'],
                            Purchase_Amount_USD=row['Purchase_Amount_USD'],
                            Location=row['Location'],
                            Size=row['Size'],
                            Color=row['Color'],
                            Season=row['Season'],
                            Review_Rating=row['Review_Rating'],
                            Subscription_Status=row['Subscription_Status'],
                            Shipping_Type=row['Shipping_Type'],
                            Discount_Applied=row['Discount_Applied'],
                            Promo_Code_Used=row['Promo_Code_Used'],
                            Previous_Purchases=row['Previous_Purchases'],
                            Payment_Method=row['Payment_Method'],
                            Frequency_of_Purchases=row['Frequency_of_Purchases'],
                        )
                        print(f'Dados inseridos com sucesso para Customer_ID={row["Customer_ID"]}')
                    except Exception as e:
                        print(f'Erro ao inserir dados para Customer_ID={row["Customer_ID"]}: {type(e).__name__} - {e}')
                        print(f'Dados da linha do CSV: {row}')
                else:
                    # Adicionar tratamento para linhas que não têm dados suficientes
                    print(f'A linha não contém dados suficientes: {row}')

            messages.success(request, 'Dados inseridos com sucesso no banco de dados.')
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados e tente novamente.')
    else:
        form = UploadCSVForm()
    print(form.errors)
    return render(request, 'chat.html', {'form': form})