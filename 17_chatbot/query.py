from app import Session, UserDB, ModelDB, ConversationDB, get_password_hash


messages1 = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好, 我可以为你做什么?"},
]

messages2 = [
    {"role": "user", "content": "苹果好吃吗?"},
    {"role": "assistant", "content": "苹果很好吃, 而且营养价值很高!"},
]


def insert_records(session):
    # Check if the user already exists
    existing_user1: UserDB = (
        session.query(UserDB).filter(UserDB.username == "Tom").one_or_none()
    )
    if existing_user1:
        user1 = existing_user1
    else:
        user1 = UserDB(
            username="Tom", password=get_password_hash("123456"), email="123@qq.com"
        )
        # 这一行可以省略, 添加 Employee 时会自动添加 department
        session.add(user1)

    existing_user2: UserDB = (
        session.query(UserDB).filter(UserDB.username == "Jerry").one_or_none()
    )
    if existing_user2:
        user2 = existing_user2
    else:
        user2 = UserDB(
            username="Jerry", password=get_password_hash("123456"), email="456@qq.com"
        )
        # 这一行可以省略, 添加 Employee 时会自动添加 department
        session.add(user2)

    existing_model: ModelDB = (
        session.query(ModelDB).filter(ModelDB.model_name == "gpt4o").one_or_none()
    )
    if existing_model:
        model = existing_model
    else:
        model = ModelDB(model_name="gpt4o", version="2407", desc="GPT-40 by OpenAI")
        session.add(model)

    input_tokens = sum(len(message["content"]) for message in messages1[:-1])
    output_tokens = len(messages1[-1]["content"])
    conversaton1 = ConversationDB(
        messages=messages1,
        user=user1,
        model=model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
    )

    input_tokens = sum(len(message["content"]) for message in messages2[:-1])
    output_tokens = len(messages2[-1]["content"])
    conversaton2 = ConversationDB(
        messages=messages2,
        user=user1,
        model=model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
    )

    input_tokens = sum(len(message["content"]) for message in messages2[:-1])
    output_tokens = len(messages2[-1]["content"])
    conversaton3 = ConversationDB(
        messages=messages2,
        user=user2,
        model=model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
    )

    session.add_all([conversaton1, conversaton2, conversaton3])

    session.commit()


def select_records(session):
    # 查询所有用户
    users: list[UserDB] = session.query(UserDB).all()
    for user in users:
        print(user)
        for conversation in user.conversations:
            print(conversation)
        print()

# <User(id=1, username='Tom', email='123@qq.com', phone='None', status='None', uuid='71452150-9c80-43dd-a3c9-11e3e1e19aa9', created_at='2024-10-14 19:26:06.679056', updated_at='2024-10-14 19:26:06.679056', deleted_at='None', conversation_num=2)>
# <Conversation(id=1, user_id=1, model_id=1, title='None', messages=[{'role': 'user', 'content': '你好'}, {'role': 'assistant', 'content': '你好, 我可以为你做什么?'}], desc='None', input_tokens=2, output_tokens=13, status='None')>
# <Conversation(id=2, user_id=1, model_id=1, title='None', messages=[{'role': 'user', 'content': '苹果好吃吗?'}, {'role': 'assistant', 'content': '苹果很好吃, 而且营养价值很高!'}], desc='None', input_tokens=6, output_tokens=16, status='None')>
# <User(id=2, username='Jerry', email='456@qq.com', phone='None', status='None', uuid='91921e6d-4424-4a4b-b354-f98a7a00a4cf', created_at='2024-10-14 19:26:06.679056', updated_at='2024-10-14 19:26:06.679056', deleted_at='None', conversation_num=1)>
# <Conversation(id=3, user_id=2, model_id=1, title='None', messages=[{'role': 'user', 'content': '苹果好吃吗?'}, {'role': 'assistant', 'content': '苹果很好吃, 而且营养价值很高!'}], desc='None', input_tokens=6, output_tokens=16, status='None')>


session = Session()

insert_records(session)
select_records(session)
