# Exercise 4: Model Context Protocol - RAG

This will be today's last exercise, where we'll combine the lessons from earlier exercises with MCP, by offering a tool that uses a vector store to provide RAG capabilities.

## Part 0: Set up your Environment
Note: If Hermit is already active, use `deactive-hermit` to drop the active Hermit context. 

1. Use `. bin/activate-hermit` in this folder to activate Hermit.
2. Start the project using `npx @modelcontextprotocol/inspector uv run mcp-rag`

## Part 1: Tool design
In contrast to the previous exercise the tool definition has been removed. As the vector store may contain some pages from the Pathfinder 2 Core Rulebook, design the interface of the tool such that an LLM may know how to pick it up.

## Part 2: Implement vector store querying
Reuse the code from exercise 2 to query the vector store. Instead of creating a new vector store like in exercise 2, use `vs_684604001f4c8191828b023de98548d0`. Keep in mind that the tool itself will need to have the OpenAI API key - try to deliver this through an environment variable again.

## Part 3: Use with a MCP client
1. (Optional) Install Goose as per `https://block.github.io/goose/docs/getting-started/installation`
2. (Optional) During installation, choose for provider `OpenAI` with model `gpt4o`, use your provided API key to connect
3. Configure a new extension using `goose configure`
   1. Ensure you're in the same folder as your project
   2. Select `Command-line extension`
   3. Give your extension a name
   4. Answer `uv run mcp-rag` for "What command should we run?" 
   5. Add the environment variable `OPENAI_API_KEY` with your provided key
4. Start Goose with `goose`
5. Ask questions about Pathfinder 2!