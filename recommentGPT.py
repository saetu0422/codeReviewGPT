import srcsearch
import openai
import glob
import mykey
import random
import pandas as pd

openai.api_key=mykey.open_api

file_path = './output.txt'


# # 파일 평가
def reCommentGPT():
    files = (srcsearch.fileAll())

    # 파일 리스트를 문자열로 변환합니다.
    file_list_str = '\n'.join(files)

    # GPT-3.5 Turbo에 보낼 메시지를 작성합니다.
    prompt = f"다음은 현재 디렉토리에서 찾은 파일 목록입니다:\n{file_list_str}\n이 파일들에 대해 무엇을 할 수 있을까요?"

    # OpenAI API를 사용하여 GPT-3.5 Turbo에 요청을 보냅니다.
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt + "What is the overall structure of this file?"}
        ]
    )

    # 모델의 응답을 출력합니다.
    print(response.choices[0].message.content)

#file 랜덤
a = random.randrange(1,100)
print(a)
# 파일 코드 검사
def fileCodeCheck():
    files = (srcsearch.filePy())

    # 파일 한개 검사
    file = open(files[a],'r',encoding='UTF8')
    code = ""
    while True:
         line = file.readline()
         if not line:
             break
         code += line
    file.close()
    print(code)
    # Gpt 사용하여 내용 물어보기
    respones = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": code + "\n how you give score is this code Max score is 10"},
            {'role': "assistant", "content": "To give a score to this code, we can evaluate it based on several criteria such as readability, modularity, error handling, efficiency, and adherence to best practices. Extract evaluation items in json format."},
            {'role': "assistant", "content": 
'''The output format example is like this : {
    "Readability":"score",
    "Modularity": "score",
    "Error Handling": "score",
    "Efficiency": "score",
    "Best Practices": "score"
}'''
            }
        ],
        temperature=0
    )
    print(respones.choices[0].message.content)
    with open(file_path, 'w') as file:
        file.write(respones.choices[0].message.content)


    #Py 파일 전체 확인
    # for i in range(len(files)):

    #     file = open(files[i], 'r', encoding='UTF8')
    #     code = ""
    #     while True:
    #      line = file.readline()
    #      if not line:
    #          break
    #      code += line
    # file.close()
    # print(code)
#보안
def securityCheck():
    pass

#다중선언 및 불필요 함수
def noUseCheck():
    pass

#패키지 확인
def requirementCheck():
    print(srcsearch.fileRQ())
    files = srcsearch.fileRQ()
    file = open(files[0],'r', encoding='UTF-8')
    code = ""
    while True:
        line = file.readline()
        if not line:
            break
        code += line
    file.close()
    print(code)

#점수 확인 및 PM
def scoreCheck():
    pass