# Teen AI YT - Automated Streaming & Editing App

Based on your clarification regarding the `aios/projects` symlinks and our online search across GitHub and skills.sh, here is the updated game plan. We've identified the top 10 skills and tools we can leverage to plan, record, edit, and broadcast for the @AICourseforKidsandTeens channel.

## Top 10 Keywords & Skills Identified

### Planning & Viral Ideas
1. **`youtube-video-analyst`** *(skills.sh)*: An AI agent skill designed to deconstruct YouTube videos to extract viral formulas, hooks, and retention mechanics. Perfect for planning our episodes.
2. **`seo-keyword-strategist`** *(skills.sh)*: Helps craft titles and descriptions optimized for YouTube search.
3. **`youtube-prompt-engineer`** *(Custom Skill)*: A custom skill we will build that uses the existing `find-skills` tool to search local and online repos, dynamically injecting relevant skills into our prompts to make them production-ready before execution.

### Recording & AI Generation
3. **`fal-platform` / `wan` / `veo-cli`** *(skills.sh)*: AI video generation models. We can use these to generate b-roll, AI avatars, or animations for the kids/teens course without manual filming.
4. **`higgsfield-cli`** *(skills.sh)*: A skill specifically tuned for generating high-click-through-rate (CTR) YouTube thumbnails.

### Programmatic Video Editing
5. **`remotion`** *(GitHub)*: A powerful framework that allows us to build videos programmatically using React. We can create templates for our courses and generate dynamic videos on the fly.
6. **`editly`** *(GitHub)*: A declarative tool for Node.js that uses FFmpeg to assemble videos, images, and audio. Great for fast, automated rendering pipelines.
7. **`moviepy`** *(GitHub)*: If we prefer a Python backend, this library allows deep control over video cutting, text overlays, and effects.
8. **`shorts-generator`** *(skills.sh)*: Auto-generates viral 9:16 YouTube Shorts clips from our longer course videos.

### Live Broadcasting & Automation
9. **`youtube-live-streaming-api`** *(GitHub/Google)*: The core official API used to programmatically schedule, create, and manage live broadcasts on YouTube.
10. **`pylivestream`** *(GitHub)*: An open-source Python tool that wraps FFmpeg to handle the actual RTMP streaming to YouTube Live.
11. **`obs-cli`** *(GitHub)*: A command-line remote control for OBS Studio. Allows us to programmatically trigger scenes, start/stop streaming, and manage the live broadcast directly from our automation scripts without manual clicks.

---

## Game Plan Architecture

### MVP Phase 1: OBS Automation & Content Capture (Current Focus)
- **Keep it Simple:** No complex dashboards yet. We will focus strictly on getting content recorded and live.
- **OBS Studio as the Core:** Use OBS Studio to capture screen recordings and Google Meet sessions.
- **Automation via `obs-cli`:** Use `obs-cli` to automate the manual steps (starting stream, starting recording, switching scenes) via shell scripts.
- **Content Pipeline:** The pipeline will output raw video files from OBS recordings. We will then process these files to generate short clips and polished edits for repurposing.

### Phase 2: AI Repurposing & Clipping
- Feed the raw OBS recordings into our AI video analyst and editing scripts (using basic Python or FFmpeg).
- Automatically extract highlight clips (9:16 format) for YouTube Shorts and TikTok.
- Generate SEO-optimized titles and descriptions using our prompt engineering skill.

### Phase 3: The "Studio App" (Future)
- Once the manual pipeline is proven, we will build the Next.js/Supabase dashboard.
- Integrate programmatic editing (Remotion/MoviePy) for fully synthesized AI videos.

### Workflow Management (GSD)
- We will adopt the **GSD (Get Shit Done)** framework for managing this project's lifecycle, specifically leveraging `gsd-plan-phase`, `gsd-execute-phase`, and `gsd-manager`. 
- This will keep our agents focused, track milestones, and ensure we stay on track as we build out the editing engine and streaming pipeline.

## User Review Required

> [!IMPORTANT]
> **MVP Folder Structure Ready:**
> The MVP focuses on OBS configuration and basic automation scripts. I will now create the directory structure and commit this plan to the repository!
