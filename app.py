# from flask import Flask, render_template
# from newsapi import NewsApiClient

# app = Flask (__name__)

# @app.route('/')
# def index():
#     newsapi = NewsApiClient(api_key="7b0bfb570f184d4ab16beb3de1276ba6")
#     topheadlines = newsapi.get_top_headlines(sources="bbc-news - BBC News")
    
#     articles = topheadlines['articles']
    
#     desc = []
#     news = []
#     img = []
    
#     for i in range (len(articles)):
#         myarticles= articles[i]
        
#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
        
#     Listsaya = zip(news, desc, img)

#     return render_template('index.html', context = Listsaya)      

# if __name__ == "__main__":
#     app.run()
        
             
from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="7b0bfb570f184d4ab16beb3de1276ba6")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    
    if topheadlines.get('status') != 'ok':
        return "Error fetching news", 500

    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []
    
    for i in range(len(articles)):
        myarticles = articles[i]
        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        
    Listsaya = zip(news, desc, img)

    return render_template('index.html', context=Listsaya)      

if __name__ == "__main__":
    app.run(debug=True)        