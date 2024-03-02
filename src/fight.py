import asyncio

from enum import Enum, auto
from random import choice
from random import random


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:

    def __aiter__(self, health=5):
        self.health = health
        self.actions = list(Action)
        return self

    async def __anext__(self):
        return choice(self.actions)


async def fight() -> None:
    agent = Agent()
    async for agent_action in agent:
        if agent_action == Action.HIGHKICK:
            neo_ation = Action.HIGHBLOCK
        elif agent_action == Action.LOWKICK:
            neo_ation = Action.LOWBLOCK
        elif agent_action == Action.HIGHBLOCK:
            neo_ation = Action.LOWKICK
            agent.health -= 1
        else:
            neo_ation = Action.HIGHKICK
            agent.health -= 1
        print((
            f'Agent: {agent_action}, Neo: {neo_ation},'
            f' Agent Health: {agent.health}'
        ))
        if agent.health == 0:
            break
    print('Neo wins!')


async def fightone(agent: Agent, num=None) -> None:
    async for agent_action in agent:
        if agent_action == Action.HIGHKICK:
            neo_ation = Action.HIGHBLOCK
        elif agent_action == Action.LOWKICK:
            neo_ation = Action.LOWBLOCK
        elif agent_action == Action.HIGHBLOCK:
            neo_ation = Action.LOWKICK
            agent.health -= 1
        else:
            neo_ation = Action.HIGHKICK
            agent.health -= 1
        res = await asyncio.sleep(random(), result=(
            f'Agent {num}: {agent_action}, Neo: {neo_ation},'
            f' Agent Health: {agent.health}'
        ))
        print(res)
        if agent.health == 0:
            break


async def fightmany(n: int) -> None:
    agents = [Agent() for _ in range(n)]
    tasks = [asyncio.create_task(
        fightone(agent, num)
    ) for num, agent in enumerate(agents)]
    for task in tasks:
        await task
    print('Neo wins!')


def main():
    # asyncio.run(fight())
    asyncio.run(fightmany(3))


if __name__ == '__main__':
    main()
