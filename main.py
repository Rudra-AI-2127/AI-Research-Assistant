from agent import ResearchAgent

agent = ResearchAgent()

print("=" * 50)
print("      AI RESEARCH ASSISTANT")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = agent.chat_with_agent(query)

        print("\nAssistant:\n")
        print(response)

    except Exception as e:
        print(f"\nError: {e}")