from app import Session, User, Model, Conversation


messages1 = [
    {"role": "user", "user": "你好"},
    {"role": "assistant", "user": "你好, 我可以为你做什么?"},
]

messages2 = [
    {"role": "user", "user": "苹果好吃吗?"},
    {"role": "assistant", "user": "苹果很好吃, 而且营养价值很高!"},
]


def insert_records(session):
    # Check if the user already exists
    existing_user1: User = (
        session.query(User).filter(User.username == "Tom").one_or_none()
    )
    if existing_user1:
        user1 = existing_user1
    else:
        user1 = User(username="Tom", password="123456", email="123@qq.com")
        # 这一行可以省略, 添加 Employee 时会自动添加 department
        session.add(user1)

    existing_user2: User = (
        session.query(User).filter(User.username == "Jerry").one_or_none()
    )
    if existing_user2:
        user2 = existing_user2
    else:
        user2 = User(username="Jerry", password="123456", email="456@qq.com")
        # 这一行可以省略, 添加 Employee 时会自动添加 department
        session.add(user2)

    existing_model: Model = (
        session.query(Model).filter(Model.model_name == "gpt4o").one_or_none()
    )
    if existing_model:
        model = existing_model
    else:
        model = Model(model_name="gpt4o", version="2407", desc="GPT-40 by OpenAI")
        session.add(model)

    conversaton1 = Conversation(
        messages=messages1,
        user=user1,
        model=model,
    )

    conversaton2 = Conversation(
        messages=messages2,
        user=user1,
        model=model,
    )

    conversaton3 = Conversation(
        messages=messages2,
        user=user2,
        model=model,
    )

    session.add_all([conversaton1, conversaton2, conversaton3])

    session.commit()


def select_records(session):
    # 查询所有用户
    users = session.query(User).all()
    for user in users:
        print(user)
        for conversation in user.conversations:
            print(conversation)
        print()


# <User(id=1, username='Tom', email='123@qq.com', phone='None', status='None', conversation_num=2)>
# <Conversation(id=1, user_id=1, model_id=1, messages=[{'role': 'user', 'user': '你好'}, {'role': 'assistant', 'user': '你好, 我可以为你做什么?'}], input_tokens_sum=0, output_tokens_sum=0, status='None')>
# <Conversation(id=2, user_id=1, model_id=1, messages=[{'role': 'user', 'user': '苹果好吃吗?'}, {'role': 'assistant', 'user': '苹果很好吃, 而且营养价值很高!'}], input_tokens_sum=0, output_tokens_sum=0, status='None')>
# <User(id=2, username='Jerry', email='456@qq.com', phone='None', status='None', conversation_num=1)>
# <Conversation(id=3, user_id=2, model_id=1, messages=[{'role': 'user', 'user': '苹果好吃吗?'}, {'role': 'assistant', 'user': '苹果很好吃, 而且营养价值很高!'}], input_tokens_sum=0, output_tokens_sum=0, status='None')>


session = Session()

insert_records(session)
select_records(session)
