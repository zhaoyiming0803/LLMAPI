# LLMAPI

Deploy large language model eg: deepseek / Qwen independently and provide http api service.

- CPU Only
- python 3.10.11

## deploy

- Install dependencies:
```shell
pip install -r requirements.txt
```

```shell
yum install nodejs

npm install -g pm2
```

- Server: 
``` shell
pm2 start ecosystem.config.js
```

- Nginx:
``` shell
server {
  listen 80;
  server_name xxx.com;

  location / {
    proxy_pass http://127.0.0.1:9001;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}
```

- Client:
``` ts
interface ChatMessage {
  role: 'system' | 'user',
  content: string
}

const messages: ChatMessage[] = []

// step1:
messages.push({
  role: 'user',
  content: '1+1等于几'
})

const result1 = await post(messages)

// step2:
messages.push({
  role: 'system',
  content: result1
})

messages.push({
  role: 'user',
  content: '为什么不是3呢？'
})

const result2 = await post(messages)

// step3:
messages.push({
  role: 'system',
  content: result2
})

messages.push({
  role: 'user',
  content: '我觉得1+1就是等于3'
})

const result3 = await post(messages)

// ........
```