# _RAG_: What is it?

RAG, short for Retrieval-Augmented Generation, is basically a technique to give context to LLMs.

As we know, LLMs are trained on a LARGE amount of data. But they are trained on past data. They have a cutoff date for their knowledge. Another problem is that, LLMs cannot possibly know everything related to what a user might be asking.

To tackle such problems, we need to provide additional context to the LLM, which can be done by fetching relevant information. This could be fetched via a tool call by the LLM itself, or at the application level, whatever suits the use case better.
