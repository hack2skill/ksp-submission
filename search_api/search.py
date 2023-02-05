import json
import requests



def search_text(query, no_of_results):
    """
    Args:
        query (str): text to search
        no_of_results (int): How many results do you want

    Returns:
        result (list({'title': str, 'url': str, 'text': str})): list of search results
    """
    url = f"https://customsearch.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx="

    results = []
    for i in range(((no_of_results-1)//10) + 1):
        if i != 0:
            url = f"{url}&start={i*10 + 1}"
        response = requests.get(url)
        result = json.loads(response.text)
        for item in result['items']:
            results.append({
                'title': item['title'],
                'url': item['link'],
                'text': item['snippet']
            })
    return results[:no_of_results]


def search_image(query, no_of_results):
    """
    Args:
        query (str): text to search
        no_of_results (int): How many results do you want

    Returns:
        result (list({'url': str, 'text': str})): list of image search results
    """
    url = f"https://customsearch.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx="
    url = f"{url}&searchType=image"

    results = []
    for i in range(((no_of_results-1)//10) + 1):
        if i != 0:
            url = f"{url}&start={i*10 + 1}"
        response = requests.get(url)
        result = json.loads(response.text)
        for item in result['items']:
            results.append({
                'url': item['link'],
                'text': item['snippet']
            })
    return results[:no_of_results]        

if __name__ == '__main__':
    x = search_text("Raghav Maheshwari", no_of_results=10)
    print(x)
        
