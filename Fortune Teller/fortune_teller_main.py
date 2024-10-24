import json
import random
import os

def lambda_handler():
    # TODO implement

    file_path = os.path.join(os.path.dirname(__file__),'index.html')

    print(f"The file path is {file_path}")

    try:
        with open(file_path, 'r') as file:
            html_content = file.read()
            print(f"The content is {html_content}")
    except FileNotFoundError:
        return {
            'statusCode' : 404,
            'body': json.dumps({"error" : "File Not Found"})
        }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_content
    }

if __name__ == "__main__":
    lambda_handler()

