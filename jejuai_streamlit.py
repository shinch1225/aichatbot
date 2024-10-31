import requests
import streamlit as st


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "5ad8a910-9749-11ef-994e-b7bbb9cee7dd3560d19d-0d45-4c95-8a82-f32b11228b23"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
while True : # 반복실행 
    # qu = input('제주도에 대해 궁금한 것을 물어봐 주세요.>>')
    qu = st.text_input('제주도에 대해 궁금한 것을 물어봐 주세요.>>')

    if qu !='':

        if qu == "나가기":
                break
        else:
            demo = classify(qu)

            label = demo["class_name"]
            confidence = demo["confidence"]

            if confidence < 70:
                st.write("제가 질문을 이해하지 못했어요.다시 질문해 주세요")
                st.write("답변 정확도 : ", confidence)
            elif label == "food":
                st.write("제주도하면 고기국수를 먹어보세요. 어디든 다 맛있답니다.\
            유명 흑돼지집에서 흑돼지 고기를 먹어보는 것도 좋겠어요")
                st.write("답변 정확도 : ", confidence)

            elif label == "cafe":
                st.write("애월에는 예쁘고 유명한 카페들이 많아요.\
            어디든 전망도 좋고 커피도 맛있으니 그 중에서 골라보세요.\
            참, 요즘엔 도넛집도 핫하다고 해요.")
                st.write("답변 정확도 : ", confidence)
            elif label == "hotplace":
                st.write("제주도에서 올레길 한번은 걸어보는 것도 좋겠죠?\
            저녁엔 야시장을 둘러보는 것도 추천해요. 무엇보다 제주하면 바다죠?\
            예쁜 세화해변도 추천해요.")
                st.write("답변 정확도 : ", confidence)

            # if confidence < 70:
            #     print("제가 질문을 이해하지 못했어요.다시 질문해 주세요")
            #     print("답변 정확도 : ", confidence)
            # elif label == "food":
            #     print("제주도하면 고기국수를 먹어보세요. 어디든 다 맛있답니다.\
            # 유명 흑돼지집에서 흑돼지 고기를 먹어보는 것도 좋겠어요")
            #     print("답변 정확도 : ", confidence)

            # elif label == "cafe":
            #     print("애월에는 예쁘고 유명한 카페들이 많아요.\
            # 어디든 전망도 좋고 커피도 맛있으니 그 중에서 골라보세요.\
            # 참, 요즘엔 도넛집도 핫하다고 해요.")
            #     print("답변 정확도 : ", confidence)
            # elif label == "hotplace":
            #     print("제주도에서 올레길 한번은 걸어보는 것도 좋겠죠?\
            # 저녁엔 야시장을 둘러보는 것도 추천해됴. 무엇보다 제주하면 바다죠?\
            # 예쁜 세화해변도 추천해요.")
            #     print("답변 정확도 : ", confidence)

        # CHANGE THIS to do something different with the result
        st.write("분류 : '%s'(%d%%의 정확도)" % (label, confidence))
        # print("분류:'%s'(%d%%의 정확도)" % (label, confidence))
        # print("result: '%s' with %d%% confidence" % (label, confidence))
    else:
        st.write("데이타 입력해 주세요")

    # while True : # 반복실행
    # ans_qu()
    #   input('계속할까요? y')
        