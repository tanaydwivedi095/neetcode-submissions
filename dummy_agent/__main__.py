from a2a.types import AgentCard, AgentSkill, AgentCapabilities, AgentInterface

def main():
    greeting_skill = AgentSkill(
        id="hello_world",
        name="Greet",
        description="Return a greeting",
        tags=["Hey", "Hi", "Hello"],
        examples=["Hey", "Hi", "Hello"]
    )
    agent_card = AgentCard(
        name="Greeting Agent",
        description="A simple agent that returns a greeting",
        version="1.0.0",
        default_input_modes=["text"],
        default_output_modes=["text"],
        skills=[greeting_skill],
        capabilities=AgentCapabilities(),
        supported_interfaces=[
            AgentInterface(
                url="http://localhost:9999",
                protocol_binding="JSONRPC",
                protocol_version="1.0",
            )
        ],
    )

    # request handler
    from a2a.server.request_handlers import DefaultRequestHandler
    from dummy_agent.agent_executor import GreetingAgentExecutor
    from a2a.server.tasks import InMemoryTaskStore

    request_handler = DefaultRequestHandler(
        agent_executor=GreetingAgentExecutor(),
        task_store=InMemoryTaskStore(),
        agent_card=agent_card,
    )

    from a2a.server.routes import create_agent_card_routes, create_jsonrpc_routes
    from starlette.applications import Starlette
    import uvicorn

    routes = []
    routes.extend(create_agent_card_routes(agent_card))
    routes.extend(create_jsonrpc_routes(request_handler, rpc_url="/"))

    app = Starlette(routes=routes)
    uvicorn.run(app, host="0.0.0.0", port=9999)

if __name__ == "__main__":
    main()