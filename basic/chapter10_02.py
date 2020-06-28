## chapter10-02

## Mini Game : Hangman (2)
# 2. 정답 단어 무작위 선택, 힌트 및 사운드 추가 보완 : 동적 프로그램
# 3. 최종 테스트

import time
import csv
import random
# import winsound # 아마도 윈도우에 내장되어 있는 외부함수 인듯

# 처음 인사
name = input('What is your name? ')
print('Hi,', name + '. Time to play Hangman game!')
time.sleep(1)
print()

print('Start Loading...')
time.sleep(0.5)
print()

# 정답 단어 : CSV파일 로드
words = []
with open('./resource/word_list.csv', 'r') as f:
    r = csv.reader(f)
    next(r)
    for li in r:
        words.append(li)

# 리스트 섞기
random.shuffle(words)

# 정답 단어 랜덤 뽑기
q = random.choice(words)

# 정답 단어
word = q[0]

# 추측 단어
guesses = ''

# 추측 기회 횟수
turns = 5

# *** 핵심 : while loop ***
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 회수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
        else:
            # 틀린 경우 언더라인으로 처리
            print('_', end=' ')
            failed += 1

    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        # 성공 사운드
        # winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        # 게임 성공 메시지
        print('Congratulations! The guess is correct!')
        break
    print()

    # 추측 단어를 문자 단위로 입력 : 정답 단어보다 더 많은 문자 입력시 재입력 요구
    guess = ''
    while True:
        guess = input('Guess a word >>> ')
        if len(guess) <= len(word):
            break
        print('Enter the same number of characters at most!')   
    print()

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        # 추측 기회 횟수 감소
        turns -= 1
        # 오류 메시지
        print('Oops! Wrong!')
        # 남은 기회 출력
        print('You have', turns, 'more guesses!')
        # 힌트 출력
        print('>>> Hint:', q[1].strip())

        if turns == 0:
            # 성공 사운드
            # winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            # 게임 실패 메시지
            print('You failed to Hangman game. Bye!')
