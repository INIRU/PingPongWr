import json

from aiohttp import ClientSession


def pingpong_custom_url(url: str):
    """ Custom API URL인식
    URL을 자르고 세션ID를 넣었을수도 있기때문에 '/custom/'뒤로 자른다.
    그리고 핑퐁빌더 custom API인지 확인한다.
    """

    if "/custom/" in url:
        return (url.split("/custom/")[0]) + "/custom/"
    elif "/custom/" not in url:
        raise TypeError("Not Custom API URL")


class Conntect:
    """ 핑퐁빌더를 쉽게 사용하게 해주는 모듈 :class: 이다.

    #Example Code
    import PingPongWr

    Ping = PingPongWr.Conntect(url, authorization)
    await Ping.Pong(Session_id, text)

    #Return
        Not Topic & Image:
            {"text": "안녕안녕입니다.", "topic": None, "Image": None}
        Topic:
            {"text": "안녕안녕입니다.", "topic": "오늘은 무슨라면을 먹을까", "Image": None}
        Image:
            {"text": "안녕안녕입니다.", "topic": None, "Image": "https://이미지.png"}

    # Session_id는 구별하기 위해서 사용하는 아이디 입니다. Discord User ID 또는 아무거나 넣으셔도 상관 없습니다.
    """

    def __init__(self, url: pingpong_custom_url, authorization: str):
        self.url = url
        self.headers = {
            "Authorization": authorization,
            "Content-Type": "application/json; charset=utf-8"
        }
        self.dialog = {}

    async def Pong(self, session_id: str, text: str, topic: bool = True, image: bool = True, dialog: bool = True) -> dict:
        """ 핑퐁빌더 API에 POST로 요청을 보내는 구문입니다.
        topic, image은 False로 비활성화 할 수 있습니다.

        dialog는 대화 맥락을 고려한 자동 답변 기능을 이용할 수 있습니다.
        dialog 문맥 데이터는 session_id 로 구별됩니다.
        """

        data = await self.PingPongCustomAPI_Request_POST(session_id, text, dialog=dialog)
        data = data["response"]["replies"]
        return_text_data = {
            "text": data[0]["text"],
            "topic": None,
            "image": None
        }
        if dialog == True:
            self.dialog[session_id].append(data[0]["text"])
        if len(data) == 2:
            if topic == True:
                if "text" in data[1]:
                    return_text_data["topic"] = data[1]["text"]
                    if dialog == True:
                        self.dialog[session_id] = data[1]["text"]
            elif image == True:
                if "image" in data[1]:
                    return_text_data["image"] = data[1]["image"]["url"]
        while len(self.dialog[session_id]) > 5:
            del self.dialog[session_id][0]
        return return_text_data

    async def PingPongCustomAPI_Request_POST(self, session_id: str, text: str, dialog: bool = True) -> dict:
        """ 핑퐁빌더 API에 포스트를 보낼 수 있도록 함수를 미리 지정해놓은 구문입니다.

        session_id, text, dialog는 Pong함수에서 전부 받아옵니다.
        """
        url = self.url + session_id
        if dialog == False:
            data = {
                "request": {
                    "query": text
                }
            }
        elif dialog == True:
            if session_id not in self.dialog:
                self.dialog[session_id] = []
            self.dialog[session_id].append(text)
            data = {
                "request": {
                    "dialog": self.dialog[session_id]
                }
            }
        data = json.dumps(data)
        return await self.AsyncRequestPost_Json(url, self.headers, data)

    async def AsyncRequestPost_Json(self, url: str, headers: dict, data: dict) -> dict:
        """
        aiohttp 모듈을 이용하여 핑퐁빌더에 POST요청을 보내는 것을 미리 함수로 정의해둔 구문입니다.
        """
        async with ClientSession() as pingpongapi:
            async with pingpongapi.post(url, headers=headers, data=data) as reqp:
                return await reqp.json()
