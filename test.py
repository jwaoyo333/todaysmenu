import json
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# PyTorch를 사용하여 GPU 설정

secrets_file_path = './secret.json'
with open(secrets_file_path) as f:
    secrets = json.loads(f.read())
os.environ["GOOGLE_API_KEY"] = secrets["api_key"]


# LangChain Google Generative AI 초기화

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    system_prompt="answer using a sentence only",  # 시스템 프롬프트 설정
    temperature=0.7)

title1 = "[속보] 드디어 음바페 'HERE WE GO' 나왔다… 계약 완료, 다음 주 영입 발표 예정"
title2 = "‘복덩이’ 박병호 결승타 쾅! 삼성, 한화 꺾고 파죽의 4연승…문동주 7이닝 무실점 [대구 리뷰] "
title3 =  "[GOAL 현장리뷰] '베카 결승골' 광주, 서울 원정서 2-1 승리... 서울 홈 5연패 충격"
title4 = "[k1.live] '관중은 많은데...' 김기동의 서울, 상암벌에서 '5연패' 최악의 부진"
title5 = "외국선수 MVP 로슨 중국으로? DB ‘용병농사’ 다시 시작"
input_text = f"'{title1}','{title2}','{title3}','{title4}','{title5}' 중 축구에 대한 이야기가 아닌 것을 모두 골라줘"
    
    
# input_text = "뉴진스가 누구야?"
response = llm.invoke(input_text)
print(response.content)
