import asyncio
import httpx
from a2a.client import A2ACardResolver, ClientConfig, create_client
from a2a.helpers import new_text_message
from a2a.types.a2a_pb2 import Role, SendMessageRequest

BASE_URL = "http://localhost:9999"

async def main():
    async with httpx.AsyncClient() as httpx_client:
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url=BASE_URL,
        )
        agent_card = await resolver.get_agent_card()
        print(agent_card)

        config = ClientConfig(streaming=False)
        client = await create_client(agent=agent_card, client_config=config)

        message = new_text_message("Hi, How are you?", role=Role.ROLE_USER)
        request = SendMessageRequest(message=message)

        async for chunk in client.send_message(request):
            print("Response:", chunk)

if __name__ == "__main__":
    asyncio.run(main())