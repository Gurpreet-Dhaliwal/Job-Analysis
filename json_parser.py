import json

"""
This method is used to parse json files
Arguments:
    filename: Name of the json file
"""
def parser(filename):
    with open(filename, 'r') as f:
        return json.load(f)

"""
if __name__ == "__main__":
    # Testing the parser function
    data = parser('./roles.json')
    print(data)
    data = parser('./technologies.json')
    print(data)
"""