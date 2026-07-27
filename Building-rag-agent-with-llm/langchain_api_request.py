from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = ChatNVIDIA(
  model="mistralai/mixtral-8x7b-instruct-v0.1",
  api_key="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", 
  temperature=0.5,
  top_p=1,
  max_completion_tokens=1024,
)

for chunk in client.stream([{"role":"user","content":""}]): 
  print(chunk.content, end="")
