# _MCP Server_: What is it all about?

> Official Write-up [here](https://www.anthropic.com/news/model-context-protocol)!
>
> [docs here](https://modelcontextprotocol.io/introduction)

It all starts with LLMs...

They are fancy next word predictors that are very advacned and have seen large amounts of data, either in form of text or otherwise.

Basically, bro can help you write an essay on a specific topic, answer a query based on what it knows already.

But, bro fails to email this essay to Sam Altman, or run a SQL query on a database, things that are out of its reach to do.

SO, there are many things that an LLM can't do. But, it has enough knowleadge about most of these things. So, we can wrap the LLM around our service to make it do a specific task.
Some examples include:
1. Search the internet (perplexity, etc.)
1. Edit code files (copilot, cursor)
1. Create figma designs
1. create premier pro editing 

These are called tools nowadays.

There was no standard/protocol that was set to make all these things happen.

MCP is that standard that can be used now.

```mermaid
graph LR

    subgraph Client
        Cursor[Cursor<br/>windsurf]
    end

    Cursor <--> MCP["<div style='font-size:20px'><b>MCP server</b></div>"]

    MCP --> ToolsRight[Tools]
    ToolsRight --> Write[write to file]
    ToolsRight --> ReadDocs[Read from docs]
    ToolsRight --> ReadErr[Read error<br/>from console]

    MCP --> ToolsDown[Tools]
    ToolsDown --> DB[MongoDB]

    classDef header font-size:18px,font-weight:bold;
```

## Model Context Protocol

```mermaid
graph TD

    subgraph MCP
        Server["MCP Server"]
    end

    MCP <--> AIModel["<div style='font-size:20px'><b>AI Model</b></div>"]

    AIModel --> Model["Model: Text, Images, Video"]
    Model --> te["LLM models like GPT, Gemini, Claude, etc"]

    MCP --> Context[Context]
    Context --> impo[most important for any LLM]
    impo --> msg[Check if the error that I am getting in this repo is mentioned in any issue or being discussed in slack]
    msg -- context: MCP server to get slack  --> xx[Need access to slack messages]
    msg -- context: MCP server to get repo issues --> xxy[Need access to repo]

    MCP --> Protocol[set of rules / standards]
    Protocol --> c[reflection request]
```
