from setuptools import setup

with open("./README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="PingPongWr",
    version="0.0.6",
    description="PingPongBuilder Custom Api Module",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="INIRU",
    author_email="duswptkfkd59@naver.com",
    install_requires=["aiohttp"],
    packages=["PingPongWr"],
    license="MIT",
    python_requires='>=3.8.0',
    keywords=['pingpong', 'ping', 'pong', 'api'],
)
