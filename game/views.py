from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Items_List,UserScore
import random
import time


# def startgame(request):

#     return render(request, 'game/game.html', {})
# def startgame(request):
#     item = Items.objects.get()
#     return render(request, 'game/game.html', {"data": Items})
def startgame(request):
    # DB에서 이미지 목록 가져오기
    items = Items_List.objects.all()
    img_list = [items.imgs for items in items]
    context = {'items':items}
    # 이미지 랜덤으로 선택하기
    selected_imgs = random.sample(img_list, 20)

    # HTML에 이미지 출력하기
    # 이미지 1장씩 보여주기
    
    latest_nickname = UserScore.objects.latest('id').nickname
    score = 0
    score = UserScore.score
    for selected_img in selected_imgs:
        context['selected_img'] = selected_img
        if request.method == 'POST':
            break
        time.sleep(5)
        if Items_List.objects.filter(name="img_name").exists():
                score += 1
           # 5초 동안 대기
    score.save()
    return render(request, 'game/game.html', {'selected_imgs': selected_imgs})
    return render(request, 'game/game.html', context)