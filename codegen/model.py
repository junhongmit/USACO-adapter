# Import ClaudeCodeAgent
try:
    from claude_code.claude_code_agent import ClaudeCodeAgent
except ImportError:
    ClaudeCodeAgent = None

# Import CodexAgent
try:
    from codex.codex_agent import CodexAgent
except ImportError:
    CodexAgent = None


def make_model(name: str, batch_size: int = 1, temperature: float = 0.8):
    if name == "claude-code-4-opus":
        if ClaudeCodeAgent is None:
            raise ImportError("ClaudeCodeAgent not available. Please ensure claude_code module is installed.")
        return ClaudeCodeAgent(
            batch_size=batch_size,
            name="claude-code-4-opus",
            temperature=temperature,
            model_name="claude-4-opus-20250514",
        )
    elif name == "claude-code-4-sonnet":
        if ClaudeCodeAgent is None:
            raise ImportError("ClaudeCodeAgent not available. Please ensure claude_code module is installed.")
        return ClaudeCodeAgent(
            batch_size=batch_size,
            name="claude-code-4-sonnet", 
            temperature=temperature,
            model_name="claude-4-sonnet-20250514",
        )
    elif name == "codex-gpt-4o":
        if CodexAgent is None:
            raise ImportError("CodexAgent not available. Please ensure codex module is installed.")
        return CodexAgent(
            batch_size=batch_size,
            name="codex-gpt-4o",
            temperature=temperature,
            model_name="gpt-4o",
        )
    elif name == "codex-o4-mini":
        if CodexAgent is None:
            raise ImportError("CodexAgent not available. Please ensure codex module is installed.")
        return CodexAgent(
            batch_size=batch_size,
            name="codex-o4-mini",
            temperature=temperature,
            model_name="o4-mini",
        )

    raise ValueError(f"Invalid model name: {name}")