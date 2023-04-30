from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Items_List,UserScore
import random
import time

def startgame(request):
    # DB에서 이미지 목록 가져오기
    items = Items_List.objects.all()
    img_list = [item.imgs for item in items]
    selected_imgs = random.sample(img_list, 20)
    context = {'selected_imgs':selected_imgs}
    # 이미지 랜덤으로 선택하기

    # HTML에 이미지 출력하기
    # 이미지 1장씩 보여주기
    
    latest_nickname = UserScore.objects.latest('nickname').nickname
    score = 0
    score = UserScore.score

    for selected_img in selected_imgs:
        context['selected_img'] = selected_img
        if request.method == 'POST':
            user_input_name = request.POST.get('img_name')
            if user_input_name == "pass":
                break
            else :
                time.sleep(5)
                if Items_List.objects.filter(name="img_name").exists():
                    score += 1
           # 5초 동안 대기
    UserScore.objects.create(nickname=latest_nickname, score=score)
    return render(request, 'game/game.html', context)
