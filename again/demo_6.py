from plotly.graph_objs import Bar
from plotly import  offline
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

response_dict =r.json()

#print(response_dict.keys())
repo_dicts=response_dict['items']
item_list = []
item_name_list, item_stars_list,item_url_list = [],[],[]
for item in repo_dicts:
    new_item={}
    new_item['name'] = item['name']
    new_item['html_url'] = item['html_url']
    new_item['stars'] = item['stargazers_count']
    item_list.append(new_item)
#print(item_list)
#print(len(item_list))
link_list = []
for item in item_list:
    item_name_list.append(item['name']) 
    item_stars_list.append(item['stars']) 
    item_url_list.append(item['html_url'])  
    link = f"<a href='{item['html_url']}>{item['name']}</a>"
    link_list.append(link)
data = [{
    'type' : 'bar',
    'x' : link_list,
    'y' : item_stars_list, 
    'marker': {
        'color' : 'rgb(60, 100 ,150)',
        'line' : {'width':1.5, 'color': 'rgb(25,25,25)'}    
    },
    'opacity' : 0.6,
}]

my_layout = {
    'title' : "github python项目stars统计",
    "xaxis" : {'title' : 'Repository'},
    "yaxis" : {'title' : 'Stars'}
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='python_repo.html')