# Create a dummy agent
class GreetingAgent():
    """Greeting agent that returns a greeting"""
    async def invoke(self) -> str:
        return "Hi Everyone! Welcome!"
    

# Create Agent Executor
from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.helpers import new_text_message

class GreetingAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = GreetingAgent()
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        result = await self.agent.invoke()
        await event_queue.enqueue_event(new_text_message(result))
    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise Exception("Cancel not supported")
     
