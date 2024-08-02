import requests
import json
from bs4 import BeautifulSoup

# URL do Trustindex onde as avaliações estão disponíveis
url = "https://www.trustindex.io/reviews/consultanacional.org"

# Fazendo uma solicitação HTTP GET para obter o conteúdo da página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extraindo avaliações (aqui você precisaria ajustar os seletores de acordo com a estrutura do HTML do Trustindex)
reviews_elements = soup.select(".review-element-class")  # ajuste o seletor conforme necessário

reviews = []
for element in reviews_elements:
    author = element.select_one(".author-class").text.strip()
    date_published = element.select_one(".date-class").text.strip()
    review_body = element.select_one(".review-body-class").text.strip()
    rating_value = element.select_one(".rating-value-class").text.strip()
    
    review = {
        "@type": "Review",
        "author": {
            "@type": "Person",
            "name": author
        },
        "datePublished": date_published,
        "reviewBody": review_body,
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": rating_value
        }
    }
    reviews.append(review)

# Estrutura JSON completa
schema = {
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Consulta Nacional",
  "image": "URL_da_Imagem_da_Sua_Empresa",
  "@id": "https://www.consultanacional.org",
  "url": "https://www.consultanacional.org",
  "telephone": "+55-47-1234-5678",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua Exemplo, 123",
    "addressLocality": "Cidade Exemplo",
    "addressRegion": "SC",
    "postalCode": "12345-678",
    "addressCountry": "BR"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",  # Você pode calcular a média das avaliações reais
    "reviewCount": str(len(reviews))
  },
  "review": reviews
}

# Converter para JSON e salvar em um arquivo
with open('schema.json', 'w', encoding='utf-8') as f:
    json.dump(schema, f, ensure_ascii=False, indent=2)

print("JSON-LD gerado com sucesso!")
