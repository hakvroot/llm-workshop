import anyio
import click
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.shared._httpx_utils import create_mcp_http_client

async def garbage_when(
    postalcode: str,
    housenumber: str,
) -> list[
    types.TextContent | types.ImageContent | types.EmbeddedResource
]:
    headers = {
        "User-Agent": "MCP Test Server (github.com/modelcontextprotocol/python-sdk)"
    }

    # Part 1
    return [types.TextContent(type="text", text="Not implemented yet!")]


@click.command()
def main() -> int:
    app = Server("mcp-rova-helper")

    @app.call_tool()
    async def fetch_tool(
        name: str, arguments: dict
    ) -> list[
        types.TextContent
        | types.ImageContent
        | types.EmbeddedResource
    ]:
        if name != "garbage_when":
            raise ValueError(f"Unknown tool: {name}")
        if "postalcode" not in arguments:
            raise ValueError("Missing required argument 'postalcode'")
        if "housenumber" not in arguments:
            raise ValueError("Missing required argument 'housenumber'")
        return await garbage_when(arguments["postalcode"], arguments['housenumber'])

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="garbage_when",
                description="Lists the next moments garbage is collected",
                inputSchema={
                    "type": "object",
                    "required": ["postalcode", "housenumber"],
                    "properties": {
                        "postalcode": {
                            "type": "string",
                            "description": "Zip code in Dutch format",
                        },
                        "housenumber": {
                            "type": "string",
                            "description": "A house number",
                        }
                    },
                },
            )
        ]

    from mcp.server.stdio import stdio_server

    async def arun():
        async with stdio_server() as streams:
            await app.run(
                streams[0], streams[1], app.create_initialization_options()
            )

    anyio.run(arun)

    return 0
