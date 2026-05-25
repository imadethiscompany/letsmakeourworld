PRO VIDEO ENGINE — Unified professional video creation for Project Nexus CEO.

Single entry point for all video creation. Handles:
- Script generation (Claude Opus)
- Voiceover (mine.voicebox → LuxTTS → ElevenLabs fallback)
- Visual generation (AI images, Pexels stock, screen recordings)
- Remotion motion graphics rendering
- HyperFrames HTML compositions
- Post-production (color grading, audio mastering, captions, branding)
- Smart trimming / jump cuts
- YouTube/TikTok metadata generation

Usage:
  python execution/pro_video_engine.py \ 
    --topic "AI Agents Taking Over in 2026" \ 
    --niche tech \ 
    --duration 45 \ 
    --style cyber \ 
    --output_dir video-generator/out

Or programmatically:
  from execution.pro_video_engine import ProVideoEngine
  engine = ProVideoEngine()
  result = engine.create_video(topic="...", niche="tech", duration=45)