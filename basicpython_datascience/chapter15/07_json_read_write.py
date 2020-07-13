# JSON Read
# - JSON파일 구조 확인하고 -> 읽어온 후 -> Dict Type처럼 처리

# JSON data
# https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/json_example.json
#
# {"employees":[
#     {"firstName":"John", "lastName":"Doe"},
#     {"firstName":"Anna", "lastName":"Smith"},
#     {"firstName":"Peter", "lastName":"Jones"}
# ]}

import json

with open('json_example.json', 'r', encoding='utf8') as f1:
    json_data = json.loads(f1.read())
    print(json_data)
    print()
    print(json_data['employees'])
    print()
    print(json_data['employees'][0])
    print(json_data['employees'][1])
    print(json_data['employees'][2])
    print()
    print(json_data['employees'][0]['firstName'])
    print(json_data['employees'][1]['firstName'])
    print(json_data['employees'][2]['firstName'])
f1.close()


# JSON Write
# - Dict Type으로 데이터 저장 -> json module로 쓰기

dict_data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

with open('data.json', 'w') as f2:
    json.dump(dict_data, f2)
f2.close()


