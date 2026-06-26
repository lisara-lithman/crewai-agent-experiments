from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Debate():
    """Debate crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def debate_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['debate_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def debater_opponent(self) -> Agent:
        return Agent(
            config=self.agents_config['debater_opponent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'], # type: ignore[index]
            verbose=True
        )


    @task
    def proposal_task(self) -> Task:
        return Task(
            config=self.tasks_config['proposal_task'], # type: ignore[index]
        )

    @task
    def opposition_task(self) -> Task:
        return Task(
            config=self.tasks_config['opposition_task'], # type: ignore[index]
        )

    @task
    def judge_task(self) -> Task:
        return Task(
            config=self.tasks_config['judge_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""
        

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
