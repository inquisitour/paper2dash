import json

def load_paper_data():
    try:
        with open('data/paper_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except UnicodeDecodeError:
        # If UTF-8 fails, try with 'iso-8859-1' encoding
        with open('data/paper_data.json', 'r', encoding='iso-8859-1') as f:
            return json.load(f)

def get_content(pathname):
    data = load_paper_data()
    page = pathname.strip('/') or 'overview'
    return data.get(page, None)

def get_complexity_data():
    try:
        data = load_paper_data()
        return data['complexity']['chart_data']
    except KeyError:
        print("Error: 'complexity' or 'chart_data' key not found in paper_data.json")
        return []
    except Exception as e:
        print(f"An error occurred while getting complexity data: {str(e)}")
        return []

def get_complexity_content():
    data = load_paper_data()
    return data.get('complexity', {
        'title': 'Complexity Analysis',
        'sections': []
    })

def get_all_sections():
    data = load_paper_data()
    return list(data.keys())

def get_references():
    data = load_paper_data()
    return data['references']['content']

def search_references(query):
    references = get_references()
    return [ref for ref in references if query.lower() in ref['title'].lower() or 
            query.lower() in ref['authors'].lower() or 
            query.lower() in ref['publication'].lower()]

def format_reference(ref):
    return f"{ref['authors']} ({ref['year']}). {ref['title']}. {ref['publication']}. {ref.get('details', '')}"