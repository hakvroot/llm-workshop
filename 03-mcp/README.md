# Exercise 3: Model Context Protocol

In this exercise we will implement a tool using MCP and use it with an LLM. Although you may implement anything you want, the provided example will get the next garbage collections from ROVA for a given postcode and house number.

## Part 0: Set up your Environment
Note: If Hermit is already active, use `deactive-hermit` to drop the active Hermit context. 

1. Use `. bin/activate-hermit` in this folder to activate Hermit.
2. Start the project using `npx @modelcontextprotocol/inspector uv run mcp-exercise`

## Part 1: Query Rova
Implement the tool to query Rova's garbage collection from `https://rova.nl/api/waste-calendar/upcoming?postalcode={postalcode}&houseNumber={housenumber}&addition=&take=5`.

If you've ran the tool using MCP Inspector, open the inspector in your web browser to test your tool.

## Part 2: Connecting with an LLM
1. Install Goose as per `https://block.github.io/goose/docs/getting-started/installation`
2. During installation, choose for provider `OpenAI` with model `gpt4o`, use your provided API key to connect
3. Configure a new extension using `goose configure`
   1. Ensure you're in the same folder as your project
   2. Select `Command-line extension`
   3. Give your extension a name
   4. Answer `uv run mcp-exercise` for "What command should we run?" 
4. Start Goose with `goose`
5. Ask questions about garbage collection (given a postal code and house number)