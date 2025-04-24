
## How to run??

#### 1. First Need to install `uv`, after that **clone this repo**.

#### 2. Then install dependencies by:

```
uv sync
```

#### 3. (Optional) Then Start local server to test:
```
uv run -- python server.py
```
#### 4. Check for `url` in **main.py**, enter target url (default will target above server):
```
uv run -- python main.py
```


> It will then start sending requests to that url, and keep doing to set time in **main.py** file as `run_time_seconds`, \
> Once code is stopped you may see that local server will crash.