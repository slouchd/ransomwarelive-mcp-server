# Ransomware Live MCP Server

This model context protocol (MCP) server interfaces with the [ransomware.live](https://github.com/JMousqueton/api.ransomware.live) API. Allowing you to use any LLM/MCP client of your choosing to reason over this data and find insights.

Credit for ransomware.live goes to its creator [Julien Mousqueton](https://github.com/JMousqueton).

Usage
---
Start the server using the default stdio transport

```bash
uv run server.py
```

Usage (Development)
---
Start the server and test it with the MCP inspector

```bash
uv add "mcp[cli]"
mcp dev server.py
```

Example Use Case
---
Using the MCP server with Claude desktop (you must have Claude desktop installed)

```bash
uv add "mcp[cli]"
mcp install server.py --name "Ransomware Live MCP Server"
```

With a basic prompt:

![Claude desktop MCP test](./claude-desktop-mcp-test.png)

With a basic prompt and visual output:

![Claude desktop MCP test](./claude-desktop-mcp-test2.png)

License
---
MIT License