from fastapi import APIRouter

r = APIRouter()

r.get('/')
def home():
    spark_session = create_spark_session()
    time.sleep(10000)
    return spark_session

r.get('/dados')
def baixa_dados(url):
    #baixar dados da url
    #decomprimir na pasta data
    return "Finalizado"

