# weird-text-task
[![CircleCI](https://circleci.com/gh/Kamig95/weird-text-task.svg?style=svg)](https://app.circleci.com/pipelines/github/Kamig95/weird-text-task?branch=master&filter=all)

## API
WeirdText API is available at [https://weird-text-task.herokuapp.com/](https://weird-text-task.herokuapp.com/).
It has two endpoints: `/v1/encode?text=<text_to_encode>` and `/v1/encode?text=<text_to_decode>`

###Examples
Request to encode text: `This is a long looong test sentence, \nwith some big (biiiiig) words!`<br />
[https://weird-text-task.herokuapp.com/v1/encode?text=This%20is%20a%20long%20looong%20test%20sentence%2C%20%0Awith%20some%20big%20%28biiiiig%29%20words%21](https://weird-text-task.herokuapp.com/v1/encode?text=This%20is%20a%20long%20looong%20test%20sentence%2C%20%0Awith%20some%20big%20%28biiiiig%29%20words%21)

Request to decode text: `\n—weird—\nTihs is a lnog lnooog tset setnncee, \nwtih smoe big (biiiiig) wdors!!\n—weird—\nlong looong sentence some test This with words`<br />
[https://weird-text-task.herokuapp.com/v1/decode?text=%0A%E2%80%94weird%E2%80%94%0ATihs%20is%20a%20lnog%20lnooog%20tset%20setnncee%2C%20%0Awtih%20smoe%20big%20%28biiiiig%29%20wdors%21%21%0A%E2%80%94weird%E2%80%94%0Along%20looong%20sentence%20some%20test%20This%20with%20words](https://weird-text-task.herokuapp.com/v1/decode?text=%0A%E2%80%94weird%E2%80%94%0ATihs%20is%20a%20lnog%20lnooog%20tset%20setnncee%2C%20%0Awtih%20smoe%20big%20%28biiiiig%29%20wdors%21%21%0A%E2%80%94weird%E2%80%94%0Along%20looong%20sentence%20some%20test%20This%20with%20words)

## Run locally
Run the virtual environment in the root folder 
```shell
pipenv shell
```
Start application
```shell
gunicorn wsgi:app
```