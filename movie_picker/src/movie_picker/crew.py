from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from crewai_tools import SerperDevTool

from typing import List
from pydantic import BaseModel, Field


search_tool = SerperDevTool()


class Movie(BaseModel):
    title: str = Field(..., description="Movie title")
    year: int = Field(..., description="Release year")
    rating: float = Field(..., description="IMDb rating")
    genre: str = Field(..., description="Movie genre")
    description: str = Field(..., description="Short movie description")


class MovieList(BaseModel):
    movies: List[Movie] = Field(..., description="List of recommended movies")


@CrewBase
class MoviePicker():
    """Movie recommendation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def movie_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["movie_manager"],
            verbose=True,
            allow_delegation=True,
            memory=True
        )

    @agent
    def movie_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["movie_researcher"],
            tools=[search_tool],
            verbose=True,
            memory=True
        )

    @agent
    def movie_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config["movie_formatter"],
            verbose=True,
            memory=True
        )

    @task
    def movie_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["movie_research_task"],
            output_pydantic=MovieList
        )

    @task
    def movie_formatting_task(self) -> Task:
        return Task(
            config=self.tasks_config["movie_formatting_task"],
            output_file="report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MoviePicker crew"""

        return Crew(
            agents=[agent for agent in self.agents if agent != self.movie_manager()],
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.movie_manager(),
            memory=True,
            verbose=True
        )