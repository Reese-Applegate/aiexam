from openai_chat import ChatMessage

while True:
    msg = input("질문[q:종료]:")
    if msg == "q":
        exit()
    rst = ChatMessage(msg)
    print(rst)
    
MODEL = "gpt-4o"

def ChatMessage(msg):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
당신은 소프트웨어 전문 개발자입니다.
사용자가 소프트웨어 개발에 관련된 질문을 할 경우
컴퓨터 관련 지식과 경험으로 설명을 해주시고
설명은 개발 언어, 관련된 방법, 처리 개발 프로세스에 대해.

예시.
질문 : 챗봇을 만드는 방법.
답변 : 챗봇을 만들기 위해서는 다음과 같은 단계를 거쳐야 합니다.
개발 : 개발에 사용하는 언어, 개발방법, 개발 프로세스에 대해 설명.
"""
            },
            {
                "role": "assistant",
                "content":""
            }
            {
                "role": "user",
                "content": msg
            }
        ]
        temperature=0.7
    )

    print(response)
    return response.choices[0].message.content