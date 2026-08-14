---
name: youtube-prompt-engineer
description: "A custom skill for the Teen AI YT project that intercepts vague ideas, automatically invokes find-skills to find relevant tools, and outputs a production-ready prompt for the execution agent."
---

# YouTube Prompt Engineer

This skill is designed to take a basic content or automation idea for the `@AICourseforKidsandTeens` channel and transform it into a highly specific, production-ready prompt that can be directly fed to an execution agent.

## When to Use
- When planning a new episode and needing an AI agent to write the script.
- When you want to automate a new piece of the pipeline but aren't sure which skills to load.
- When a prompt needs to be enriched with local project context and available agent skills.

## How it Works (The Workflow)
1. **Analyze the Request:** Understand what the user wants to achieve (e.g., "Write a script about neural networks").
2. **Skill Discovery:** Automatically run `find-skills` (or search the local `.agent/skills` directory) to find relevant skills (e.g., `seo-keyword-strategist`, `youtube-video-analyst`).
3. **Context Injection:** Inject the context of the `Teen AI YT` project (target audience: kids/teens, format: 15-min educational video).
4. **Prompt Synthesis:** Output a polished markdown prompt that the user can copy/paste to a new agent or feed directly into an automated pipeline.

## Output Format
The skill should output the final prompt in a markdown code block:

```markdown
**Role:** You are an expert AI YouTube producer for kids and teens.
**Task:** [Specific task]
**Required Skills to Load:** [List of skills from find-skills]
**Context:** [Project context]
**Constraints:** [Time limits, tone, etc.]
```
