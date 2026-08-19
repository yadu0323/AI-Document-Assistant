import asyncio

from mcp.client import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def call_mcp_tool(
    tool_name: str,
    arguments: dict
):

    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (
        read_stream,
        write_stream
    ):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments
            )

            return result.structured_content["result"]


def run_tool(
    tool_name: str,
    arguments: dict
):
    return asyncio.run(
        call_mcp_tool(
            tool_name,
            arguments
        )
    )

async def list_mcp_tools():

    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )

    async with stdio_client(
        server_params
    ) as (
        read_stream,
        write_stream
    ):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            tools = await session.list_tools()

            return tools


def get_tools():

    return asyncio.run(
        list_mcp_tools()
    )