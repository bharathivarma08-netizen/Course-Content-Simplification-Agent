from core.granite_client import ask_granite
from core.retriever import retrieve_context


# =========================================
# LEVEL-BASED TEACHING INSTRUCTIONS
# =========================================
LEVEL_INSTRUCTIONS = {

    "6th Class":
    "Use extremely simple words. Short sentences. "
    "Explain like teaching an 11-year-old child.",

    "10th Class":
    "Use simple English. Avoid difficult jargon. "
    "Use relatable daily-life examples.",

    "Intermediate":
    "Use moderately simple language. "
    "Some technical terms are okay if explained.",

    "Diploma":
    "Use practical technical explanations. "
    "Focus on real-world understanding.",

    "BTech":
    "Use technical explanations with theory and implementation details.",

    "Beginner":
    "Assume zero prior knowledge. "
    "Build concepts from scratch using analogies.",

    "Advanced":
    "Use advanced terminology and deeper conceptual discussion."
}


# =========================================
# LEARNING STYLE INSTRUCTIONS
# =========================================
STYLE_INSTRUCTIONS = {

    "Visual learner":
    "Use visual metaphors, spatial explanations, and diagram-like descriptions.",

    "Step-by-step learner":
    "Break concepts into small numbered steps. "
    "Explain one idea at a time.",

    "Real-world examples":
    "Connect every concept with real-life applications and industry scenarios.",

    "Exam-focused learner":
    "Focus on definitions, key points, and exam-oriented answers.",

    "Quick revision learner":
    "Keep explanations concise using bullet points and summaries."
}


# =========================================
# SYSTEM PROMPT BUILDER
# =========================================
def build_system_prompt(level: str, style: str) -> str:

    level_inst = LEVEL_INSTRUCTIONS.get(
        level,
        LEVEL_INSTRUCTIONS["BTech"]
    )

    style_inst = STYLE_INSTRUCTIONS.get(
        style,
        STYLE_INSTRUCTIONS["Step-by-step learner"]
    )

    return f"""
You are EduBot — an intelligent adaptive educational AI teacher.

Your responsibility:
- teach concepts clearly
- simplify difficult topics
- adapt to student level
- personalize explanations

Student Level Instruction:
{level_inst}

Teaching Style Instruction:
{style_inst}

STRICT RULES:
- Never use difficult jargon without explanation
- Keep explanations student-friendly
- Explain patiently like a human teacher
- Use examples and analogies
- Keep explanations warm and encouraging
- Preserve technical correctness
"""


# =========================================
# MAIN EXPLANATION GENERATOR
# =========================================
def generate_explanation(
    topic: str,
    level: str,
    style: str
) -> str:

    # Adaptive teaching system
    system = build_system_prompt(level, style)

    # =====================================
    # RAG CONTEXT RETRIEVAL
    # =====================================
    try:

        retrieved_context = retrieve_context(topic)

    except Exception:

        retrieved_context = ""

    # =====================================
    # EDUCATIONAL PROMPT
    # =====================================
    prompt = f"""
Explain the topic:

"{topic}"

Student Level:
{level}

Learning Style:
{style}

Trusted Educational Context:
{retrieved_context}

IMPORTANT:
- Use the trusted educational context while teaching
- Simplify difficult concepts
- Preserve exact meaning
- Avoid robotic explanation style
- Use examples and analogies
- Make it exam-friendly
- Use small understandable sentences

Structure your response EXACTLY like this:

## A. Why this concept exists
(Explain why this concept was created.)

## B. What it is
(Complete simplified explanation.)

## C. Real-world examples
(2-3 practical applications.)

## D. Key points to remember
(Maximum 5 important bullet points.)

## E. Exam keywords
(Important terms students should remember.)
"""

    return ask_granite(
        prompt=prompt,
        system=system
    )


# =========================================
# DOUBT SOLVER
# =========================================
def generate_doubt_response(
    doubt: str,
    topic: str = "",
    level: str = "BTech",
    style: str = "Step-by-step learner",
    context: str = ""
) -> str:

    system = build_system_prompt(
        level,
        style
    )

    # Optional RAG retrieval
    try:

        retrieved_context = retrieve_context(
            topic + " " + doubt
        )

    except Exception:

        retrieved_context = ""

    prompt = f"""
The student is studying:

{topic}

Student doubt:

{doubt}

Previous learning context:
{context}

Retrieved educational context:
{retrieved_context}

Instructions:
- Answer clearly and simply
- Adapt to student level
- Use examples if needed
- Avoid difficult jargon
- Keep explanation concise
- Be encouraging
"""

    return ask_granite(
        prompt=prompt,
        system=system
    )
 