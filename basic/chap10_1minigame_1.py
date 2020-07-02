## chapter10-01

## Mini Game : Hangman (1)
# 1. 기본 프로그램 제작 및 중간 테스트 : 정답 단어를 정해 놓고 제작(정적프로그램)

import time

# 처음 인사
name = input('What is your name? ')
print('Hi,', name + '. Time to play Hangman game!')
time.sleep(1)
print()

print('Start Loading...')
time.sleep(0.5)
print()

# 정답 단어
word = 'secret'

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
        print('Congratulations! The guess is correct!')
        break
    print()

    # 추측 단어의 문자 단위 입력
    print()
    guess = input('Guess a word. ')

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

        if turns == 0:
            # 게임 실패 메시지
            print('You failed to Hangman game. Bye!')
