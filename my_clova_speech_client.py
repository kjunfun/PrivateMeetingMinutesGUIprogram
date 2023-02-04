import requests
import json

# clova api와 통신하기 위한 class -> 클로바 speech에서 생성한 도메인마다 고유의 호출 url이 생성된다.
# 다음 두 정보 invoke url, secret key 정보를 서비스 빌더에서 확인 한다.
class ClovaSpeechClient:
    # Clova Speech invoke URL
    ## -> 이 부분은 그냥 ''냅둬도 됨. -> 클래스 내에 멤버변수가 있기만 즉 명시만 하면 쓸 수 있는거고,
    invoke_url = ''
    # Clova Speech secret key
    secret = ''

    def setInvoke_url(self, url):
        self.invoke_url = url

    def setSecret(self, secretKey):
        self.secret = secretKey

    # 로컬의 파일 업로드해서 요청(파일시스템의 경로를 이용) --> 이걸 쓰는 거니깐 API 공식문서 상 위의 두가지 방식은 지워버려도 된다!
    def req_upload(self, file, completion, callback=None, userdata=None, forbiddens=None, boostings=None,
                   wordAlignment=True, fullText=True, diarization=None):
        request_body = {
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
        files = {
            'media': open(file, 'rb'),
            'params': (None, json.dumps(request_body, ensure_ascii=False).encode('UTF-8'), 'application/json')
        }
        response = requests.post(headers=headers, url=self.invoke_url + '/recognizer/upload', files=files)
        return response


if __name__ == '__main__': # 이 부분은 해당 파일만을 실행하기 위한 부분이므로 없어도 됨.
    # res = ClovaSpeechClient().req_url(url='http://example.com/media.mp3', completion='sync')
    # res = ClovaSpeechClient().req_object_storage(data_key='data/media.mp3', completion='sync')
    res = ClovaSpeechClient().req_upload(file='/data/media.mp3', completion='sync')
    # sync로 요청 받아서 인식 완료되면 response 결과 json으로 받고 있고, 해당 파일 경로 요기 파이참에 넣으면 된다.
    print(res.text)

