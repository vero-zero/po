# from django.shortcuts import render
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Items_List
# import random
# import time


# # def startgame(request):

# #     return render(request, 'game/game.html', {})
# # def startgame(request):
# #     item = Items.objects.get()
# #     return render(request, 'game/game.html', {"data": Items})
# def startgame(request):
#     # DB에서 이미지 목록 가져오기
#     items = Items_List.objects.all()
#     img_list = [img.imgs for img in items]
#     name_list = [names.name for names in items]

#     # 이미지 랜덤으로 선택하기
#     selected_item = random.sample(img_list, 20)

#     # 20개 이미지를 1개씩 5초동안 보여주고, 사용자가 입력한 텍스트가 이미지데이터베이스 기본키 텍스트와 같으면 점수를 1점 부여
#     score = 0
#     for item in selected_item:
#         # 5초간 이미지 출력
#         context = {'image': item}
#         time.sleep(5)
#         # 이미지 출력 후 사용자 입력 받기
#         user_input = request.POST.get('user_input', '')
#         # 사용자 입력과 이미지 데이터베이스 기본키 비교 후 점수 부여
#         if user_input in name_list:
#             score += 1

#     # 총 점수를 세션에 저장
#     request.session['score'] = score

#     # User db table score에 저장
#     if request.user.is_authenticated:
#         user = request.user
#         user.score = score
#         user.save()

#     # HTML에 점수 출력하기
#     return render(request, 'game/result.html', {'score': score})