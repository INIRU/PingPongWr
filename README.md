# PingPongWr

파이썬으로 제작된 핑퐁 빌더 Custom Api를 좀 더 쉽고 간편하게 사용할 수 있게 해주는 모듈입니다.
</br>
`별도의 출처를 밝힐필요 없습니다.`

</br>

# Installing

```
# Linux/macOS
python3 -m pip install -U PingPongWr

# Windows
py -3 -m pip install -U PingPongWr
```

# Quick Example

### 독자적 사용 예시

```python
import PingPongWr # 메인 모듈
import asyncio # 비동기 실행을 위한 모듈

url = "커스텀 API 링크"  # 핑퐁빌더 Custom API URL
pingpong_token = "인증 토큰"  # 핑퐁빌더 Custom API Token

Ping = PingPongWr.Connect(url, pingpong_token)  # 핑퐁 모듈 클래스 선언

async def Example(): # 비동기식 함수
    str_text = input("나: ")  # 대화할 말 입력받기
    return_data = await Ping.Pong(session_id ="Example", text = str_text, topic = True, image = True, dialog = True) # 핑퐁빌더 API에 Post 요청

    print(return_data) # {"text": "안녕안녕입니다", "topic": None, "Image": None}

asyncio.run(Example())  # 비동기로 함수 실행
```

# Discord Example

### 디스코드에서 사용예시

```python
import discord
import PingPongWr

from discord.ext import commands

bot = commands.Bot(command_prefix='>')

url = "커스텀 API 링크"  # 핑퐁빌더 Custom API URL
pingpong_token = "인증 토큰"  # 핑퐁빌더 Custom API Token

Ping = PingPongWr.Connect(url, pingpong_token)  # 핑퐁 모듈 클래스 선언

@bot.event()
async def on_message(message):

    if message.author == bot.user:
            return

     if message.content.startswith("봇"):
        str_text = (message.content.split(" "))[1]
        return_data = await Ping.Pong(session_id ="Example", text = str_text, topic = True, image = True, dialog = True) # 핑퐁빌더 API에 Post 요청
        await message.channel.send(f"{message.author.mention}, {return_data["text"]}")

bot.run("token")
```

# Links

-   `Team. Warin Discord:` https://discord.gg/cGM4PcHvQq
