import httpx

url1 = "https://caelum-online-public.s3.amazonaws.com/2273-introducao-spark/01/empresas.zip"
url2 = "https://caelum-online-public.s3.amazonaws.com/2273-introducao-spark/01/estabelecimentos.zip"
url3 = "https://caelum-online-public.s3.amazonaws.com/2273-introducao-spark/01/socios.zip"

lista_url_dados = [url1, url2, url3]
dominio = "http://localhost:7777"

httpx.get(f"{dominio}/dados", param=url1)