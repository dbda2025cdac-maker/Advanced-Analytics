import asyncio

from ollama import AsyncClient


async def main():
  messages = [
    {
      'role': 'user',
      'content': 'What is logistic regression?',
    },
  ]

  client = AsyncClient()
  response = await client.chat('deepseek-r1:1.5b', messages=messages)
  print(response['message']['content'])


if __name__ == '__main__':
  asyncio.run(main())