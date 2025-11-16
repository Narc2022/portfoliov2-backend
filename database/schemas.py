def individual_data(todo):
    return {
        "id": str(todo["_id"]), #as mongodb store data in object so here we typcaste id to string
        "title": todo["name"],
        "description": todo["description"],
        "status": todo["is_completed"]
    }
    
#create list of dictionary
def all_tasks(todos):
    return [individual_data(todo) for todo in todos]