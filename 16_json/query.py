from db_init import Session, Json1


session = Session()


jsons = [
    Json1(
        messages=[
            {"role": "user", "user": "你好"},
            {"role": "assistant", "user": "你好, 我可以为你做什么?"},
        ]
    ),
    Json1(
        messages=[
            {"role": "user", "user": "你好"},
            {"role": "assistant", "user": "你好, 我可以为你做什么?"},
        ]
    ),
]


session.add_all(jsons)
session.commit()

results = session.query(Json1).all()
for result in results:
    print(result)
    print(result.messages, type(result.messages), type(result.messages[0]))
# <Json1(id=3, messages=[{'role': 'user', 'user': '你好'}, {'role': 'assistant', 'user': '你好, 我可以为你做什么?'}])>
# [{'role': 'user', 'user': '你好'}, {'role': 'assistant', 'user': '你好, 我可以为你做什么?'}] <class 'list'> <class 'dict'>
# <Json1(id=4, messages=[{'role': 'user', 'user': '你好'}, {'role': 'assistant', 'user': '你好, 我可以为你做什么?'}])>
# [{'role': 'user', 'user': '你好'}, {'role': 'assistant', 'user': '你好, 我可以为你做什么?'}] <class 'list'> <class 'dict'>
