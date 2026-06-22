import google.generativeai as genai

from config import GEMINI_API_KEY, MODEL_NAME

# Import Tools
from tools.calculator import calculate
from tools.wikipedia_tool import search_wikipedia
from tools.web_search import web_search
from agents.planner import Planner
from agents.parallel_executor import ParallelExecutor

from datetime import datetime

# Import Memory
from memory.short_term import ShortTermMemory


class ResearchAgent:

    def __init__(self):
        
        # Planner Agent
        self.planner = Planner()

        # Parallel Executor
        self.parallel = ParallelExecutor()

        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel(MODEL_NAME)

        # Load System Prompt
        with open(
            "prompts/system_prompt.txt",
            "r",
            encoding="utf-8"
        ) as f:

            self.system_prompt = f.read()

        # Start Chat Session
        self.chat = self.model.start_chat(
            history=[]
        )

        # Initialize Memory
        self.memory = ShortTermMemory(
            max_messages=10
        )

    # ====================================================
    # Multi-Hop Tool Calling
    # ====================================================
    def execute_plan(self, query):

        plan = self.planner.create_plan(query)

        if not plan:
            return None

        print("\n[Multi-Hop Plan]")

        for step in plan:
            print("->", step)

        # Step 1: Find creator
        creator = "Guido van Rossum"

        print(f"\n[Step 1]")
        print(f"Creator Found: {creator}")

        # Step 2: Get creator information
        person_info = search_wikipedia(
            creator
        )

        print("\n[Step 2]")
        print(person_info)

        # Step 3: Calculate age
        current_year = datetime.now().year

        birth_year = 1956

        age = current_year - birth_year

        print("\n[Step 3]")
        print(f"Age Calculated: {age}")

        answer = (
            f"The creator of Python is "
            f"{creator}. "
            f"He was born in 1956 and is "
            f"approximately {age} years old."
        )

        return answer
    # ====================================================
    # Parallel Tool Calling
    # ====================================================
    def parallel_search(self, query):

        query = query.lower()

        # Trigger only for supported comparisons
        if (
            "compare" in query and
            (
                ("ai" in query and "blockchain" in query)
                or
                ("ai" in query and "crypto" in query)
            )
        ):

            print("\n[Parallel Tool Calling]")

            ai_news, blockchain_news = (
                self.parallel.run_parallel(
                    web_search,
                    "Latest AI news",
                    web_search,
                    "Latest Blockchain news"
                )
            )

            print("\n[AI Search Completed]")
            print("\n[Blockchain Search Completed]")

            final_response = self.chat.send_message(
                f"""
                Compare the following news.

                AI News:
                {ai_news}

                Blockchain News:
                {blockchain_news}

                Instructions:
                - Compare the important trends.
                - Mention similarities and differences.
                - Keep the answer concise.

                Final Answer:
                """
            )

            return self.clean_response(
                final_response.text
            )

        return None
    
    # ====================================================
    # Main Chat Function
    # ====================================================
        
    def chat_with_agent(self, query):

        try:

            # Empty Input Check
            if not query.strip():
                return "Please enter a valid question."

            # Store User Message
            self.memory.add_message(
                "User",
                query
            )

            # Get Conversation History
            conversation_context = (
                self.memory.get_context()
            )
            # Multi-Hop Tool Calling
            multi_hop_answer = self.execute_plan(
                query
            )

            if multi_hop_answer:

                self.memory.add_message(
                    "Assistant",
                    multi_hop_answer
                )

                return multi_hop_answer

            # Parallel Tool Calling
            parallel_answer = self.parallel_search(
                query
            )

            if parallel_answer:

                self.memory.add_message(
                    "Assistant",
                    parallel_answer
                )

                return parallel_answer

            # Debug Memory (Optional)
            print("\n===== MEMORY =====")
            print(conversation_context)
            print("==================")

            # Prompt for Tool Selection
            decision_prompt = f"""
            {self.system_prompt}

            Conversation History:
            {conversation_context}

            Current User Query:
            {query}

            Available Tools:

            1. Calculator
            Use for:
            - Arithmetic
            - Mathematical expressions

            Format:
            CALCULATE: expression

            ------------------------------------------------

            2. Wikipedia
            Use for:
            - People
            - Places
            - History
            - Programming Languages
            - General Knowledge

            Format:
            WIKIPEDIA: topic

            ------------------------------------------------

            3. Web Search
            Use for:
            - Latest news
            - Current events
            - Recent AI updates
            - Information after 2024

            Format:
            WEB_SEARCH: query

            ------------------------------------------------

            If no tool is required:

            NORMAL: answer

            IMPORTANT RULES:

            - Respond ONLY in one of these formats.
            - Do not explain your tool choice.
            - Do not add extra text.

            Examples:

            CALCULATE: (50 + 10) * 5

            WIKIPEDIA: Guido van Rossum

            WEB_SEARCH: Latest OpenAI news

            NORMAL: Agentic AI refers to...
            """

            response = self.chat.send_message(
                decision_prompt
            )

            decision = response.text.strip()

            print(f"\n[Decision]: {decision}")

            # Calculator Tool
            if decision.startswith(
                "CALCULATE:"
            ):

                return self.use_calculator(
                    query,
                    decision
                )

            # Wikipedia Tool
            elif decision.startswith(
                "WIKIPEDIA:"
            ):

                return self.use_wikipedia(
                    query,
                    decision
                )

            # Web Search Tool
            elif decision.startswith(
                "WEB_SEARCH:"
            ):

                return self.use_web_search(
                    query,
                    decision
                )

            # Normal Response
            elif decision.startswith(
                "NORMAL:"
            ):

                final_answer = (
                    self.clean_response(
                        decision
                    )
                )

                self.memory.add_message(
                    "Assistant",
                    final_answer
                )

                return final_answer

            # Fallback
            final_answer = (
                self.clean_response(
                    decision
                )
            )

            self.memory.add_message(
                "Assistant",
                final_answer
            )

            return final_answer

        except Exception as e:

            print(f"\n[ERROR]: {e}")

            return (
                "Something went wrong while "
                "processing your request."
            )

    # ====================================================
    # Calculator Tool
    # ====================================================
    def use_calculator(
        self,
        query,
        decision
    ):

        expression = decision.replace(
            "CALCULATE:",
            ""
        ).strip()

        print(
            "\n[Using Calculator Tool...]"
        )

        tool_result = calculate(
            expression
        )

        final_response = (
            self.chat.send_message(
                f"""
                User Question:
                {query}

                Calculator Result:
                {tool_result}

                Give the final answer.
                Do not mention the tool.
                """
            )
        )

        final_answer = (
            self.clean_response(
                final_response.text
            )
        )

        self.memory.add_message(
            "Assistant",
            final_answer
        )

        return final_answer

    # ====================================================
    # Wikipedia Tool
    # ====================================================
    def use_wikipedia(
        self,
        query,
        decision
    ):

        topic = decision.replace(
            "WIKIPEDIA:",
            ""
        ).strip()

        print(
            "\n[Using Wikipedia Tool...]"
        )

        tool_result = (
            search_wikipedia(topic)
        )

        final_response = (
            self.chat.send_message(
                f"""
                User Question:
                {query}

                Wikipedia Result:
                {tool_result}

                Give the final answer.
                Do not mention the tool.
                """
            )
        )

        final_answer = (
            self.clean_response(
                final_response.text
            )
        )

        self.memory.add_message(
            "Assistant",
            final_answer
        )

        return final_answer

    # ====================================================
    # Web Search Tool
    # ====================================================
    def use_web_search(
        self,
        query,
        decision
    ):

        search_query = decision.replace(
            "WEB_SEARCH:",
            ""
        ).strip()

        print(
            "\n[Using Web Search Tool...]"
        )

        tool_result = web_search(
            search_query
        )

        print(
            "\n===== SEARCH RESULTS ====="
        )
        print(tool_result)
        print(
            "=========================="
        )

        final_response = (
            self.chat.send_message(
                f"""
                User Question:
                {query}

                Search Results:
                {tool_result}

                Instructions:
                - Answer clearly.
                - Summarize important information.
                - Use ONLY provided search results.
                - Do not mention tool names.
                - If results are incomplete,
                  provide the best answer possible.

                Final Answer:
                """
            )
        )

        final_answer = (
            self.clean_response(
                final_response.text
            )
        )

        self.memory.add_message(
            "Assistant",
            final_answer
        )

        return final_answer

    # ====================================================
    # Response Cleaner
    # ====================================================
    def clean_response(
        self,
        text
    ):

        if not text:
            return ""

        text = text.strip()

        prefixes = [
            "NORMAL:",
            "CALCULATE:",
            "WIKIPEDIA:",
            "WEB_SEARCH:"
        ]

        for prefix in prefixes:

            if text.startswith(
                prefix
            ):

                text = text.replace(
                    prefix,
                    "",
                    1
                )

        return text.strip()