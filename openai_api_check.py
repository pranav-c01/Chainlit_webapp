import openai

# Set your OpenAI API key
openai.api_key = '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'

# Retrieve the remaining free tokens
usage = openai.Usage.retrieve()
remaining_tokens = usage['data']['remaining']
print("Remaining free tokens:", remaining_tokens)

# Get token usage by models
models = openai.Completion.list_models()
for model in models:
    model_id = model['id']
    usage = openai.Usage.retrieve(model=model_id)
    tokens_used = usage['data']['usage']['prompt_tokens']
    print(f"Model {model_id} used {tokens_used} tokens")

# Fetch rate limits (requests per minute)
limits = openai.RateLimits.retrieve()
rpm_limit = limits['data'][0]['limit']
rpm_remaining = limits['data'][0]['remaining']
print("Requests per minute limit:", rpm_limit)
print("Remaining requests per minute:", rpm_remaining)
