# Logging : 로그 남기기
# - 프로그램이 실행되는 동안 일어나는 정보를 기록으로 남기기
# - 유저의 접근, 프로그램의 Exception, 특정 함수의 사용 등을 기록
# - 콘솔 화면에 출력, 파일에 남기기, 데이터베이스에 남기기 등
# - 기록된 로그를 분석하여 의미있는 결과를 도출할 수 있음
# - 실행시점에서 남겨야 하는 기록, 개발시점에서 남겨야 하는 기록

# Printing VS Logging
# - 기록을 print로 남기는 것도 가능함, 그러나 콘솔 창에만 남기는 기록은 분석시 사용 불가
# - 때로는 레벨별(개발, 운영)로 구분하여 기록을 남길 필요도 있음
# - 모듈별로 별도로 기록을 남길 필요도 있음
# - 이러한 기능을 체계적으로 지원하는 모듈이 필요함

# Logging Module : 파이썬의 기본 로그 관리 모듈
# import logging
# logging.debug('Wrong!')
# logging.info('Need to check')
# logging.warning('Be careful!')
# logging.error('Something went wrong!!')
# logging.critical('Dangerous!!!')

# Logging Level : 프로 그램 지행 상황에 따라 다른 레벨의 로그를 출력함
# - 개발 시점, 운영 시점마다. 다른 로그가 남을 수 있도록 지원함
# - DEBUG > INFO > WARNING > ERROR > CRITICAL
# - 로그 관리시 가장 기본이 되는 설정 정보
# 1) DEBUG : 개발시 처리 기록을 남겨야 하는 로그 정보를 남김
# 2) INFO : 처리가 진행되는 동안의 정보를 알림
# 3) WARNING : 사용자가 잘못 입력한 정보나 처리는 가능하나 개발시 의도치 않는 정보가 들어왔을 때 알림
# 4) ERROR : 잘못된 처리로 인해 에러가 발생했으나 프로그램은 동작할 수있음을 알림
# 5) CRITICAL : 잘못된 처리로 데이터 손실이나 더이상 프로그램이 동작할 수 없음을 알림

import logging
# logger 선언
logger = logging.getLogger('main')
# logger의 output 방법 선언
stream_handler = logging.StreamHandler()
# logger의 output 등록
logger.addHandler(stream_handler)
# logger의 level 및 상태 등록 : 디버그 모드시 기록되는 로그 상태 정보
logger.setLevel(logging.DEBUG)
logger.debug('Wrong!')
logger.info('Need to check')
logger.warning('Be careful!')
logger.error('Something went wrong!!')
logger.critical('Dangerous!!!')
print()
# 또 다른 level 및 상태 등록 : 디버그 모드가 아닐 시 기록되는 로그 상태 정보
logger.setLevel(logging.CRITICAL)
logger.debug('Wrong!')
logger.info('Need to check')
logger.warning('Be careful!')
logger.error('Something went wrong!!')
logger.critical('Dangerous!!!')
print()
logger.setLevel(logging.WARNING)
logger.debug('Wrong!')
logger.info('Need to check')
logger.warning('Be careful!')
logger.error('Something went wrong!!')
logger.critical('Dangerous!!!')
print()

