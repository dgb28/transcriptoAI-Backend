# 🧠 AI-Powered Meeting Companion

An end-to-end AI assistant that helps teams make the most out of their meetings by transcribing audio/video, generating intelligent summaries, extracting action items with timestamps, and analyzing speaker sentiment  all within a sleek React dashboard.

## 🚀 Overview

This project was built for a hackathon and aims to streamline post-meeting analysis using state-of-the-art AI models. Users can upload recorded meetings, and our system intelligently breaks down the content into:

- *Transcription* (verbatim)
- *Summaries* (in multiple formats)
- *Action Items & Time Extracts*
- *Speaker Sentiment Analysis*

Everything is displayed inside a fully responsive React-based dashboard, with options to download all outputs in one click.

## 🔄 Workflow

1. *Ingestion* – Upload MP3, WAV, or MP4 via the dashboard  
2. *Transcription* – Convert speech to text using a transcription module  
3. *Segmentation* – Split output into:
   - Full Transcript  
   - AI-generated Summary  
   - Extracted Tasks & Timestamps  
4. *Summary Filters* – Choose from:
   - One-Line Summary  
   - Bullet-Point Summary  
   - Paragraph Summary  
   - In-Depth Summary  
   - TL;DR Summary  
5. *Sentiment Analysis* – Gauge tone per speaker using GPT-4.0  
6. *Visualization* – View all outputs in a clean, scrollable React UI  
7. *Download* – Export transcripts, summaries, and task lists

## 🎯 Key Features

- ✅ Upload Audio or Video Recordings
- ✅ Real-Time and Post-Processing Transcription
- ✅ Multi-Level Summarization via GPT-4.0
- ✅ Action Item & Decision Extraction with Timestamps
- ✅ Speaker-wise Sentiment/Tone Analysis
- ✅ Responsive React Dashboard (with filters and download support)

## 🧠 Tech Stack

- *Frontend*: React, CSS  
- *AI Models*: OpenAI GPT-4.0  
- *Transcription*: Whisper/Custom Model

## 🏆 Accomplishments

- Integrated all modules seamlessly in a single platform  
- Delivered five distinct summary modes  
- Extracted actionable insights and timestamped tasks  
- Built a smooth, responsive UI with scrollable card views  
- Completed a working hackathon demo in record time  

## ⚠ Challenges Faced

- Varying audio quality impacted transcription  
- Prompt engineering was needed to shape summary output styles  
- UI optimization for long transcripts  
- Managed GPT-4 rate limits and async workflow handling  
- Ensured cross-browser compatibility and responsiveness

## 🔮 Future Work 
 📆 Calendar Integration (Google/Outlook)  

## 📁 Downloads Available

- ✅ Transcripts  
- ✅ Summaries (filtered by user)  

## 🧪 How to Run Locally

```bash
git clone https://github.com/yourusername/ai-meeting-companion.git
cd ai-meeting-companion
npm install
npm start





✅ Inspiration
We were inspired by the inefficiencies we all face during meetings—poor note-taking, missed action items, and forgotten decisions. We wanted to build something that truly listens and acts, transforming conversations into organized, actionable summaries. Our goal was to help teams focus on discussions rather than documentation.

✅ What it does
Transcripto is an AI-powered assistant that allows users to upload or stream meeting recordings and automatically:
Transcribes audio/video content


Generates summaries in five formats (one-line, bullet-point, paragraph, in-depth, TL;DR)


Extracts action items and decisions


Analyzes tone and sentiment per speaker


Displays speaker contributions and topic focus


Lets users download all insights and outputs for future reference



✅ How we built it
Frontend: Built with React for a clean, responsive dashboard, including filter dropdowns, scrollable panels, and download controls.


Backend: Python-based APIs handling transcription parsing, action extraction, and tone analysis.


AI Models: Used OpenAI GPT-4 for summaries and sentiment; Whisper for transcription.


Real-Time: Implemented live transcription using Streamlit and WebSocket for dynamic updates during meetings.



✅ Challenges we ran into
Handling poor audio quality and speaker overlap in recordings


Crafting effective prompts to consistently generate high-quality summaries


Keeping the UI smooth and responsive with large amounts of transcript data


Managing asynchronous tasks like uploading, transcription, and response generation without blocking the interface


Operating within strict GPT-4 API rate and usage limits during the hackathon timeframe



✅ Accomplishments that we're proud of
Successfully delivered a polished, end-to-end AI meeting assistant in under 48 hours


Built a real-time transcription pipeline using Streamlit and WebSocket


Developed multiple summary styles with GPT-4


Enabled users to interactively filter, explore, and download meeting insights


Designed a sleek and intuitive frontend from scratch



✅ What we learned
Effective UI/UX plays a crucial role in how users engage with AI-generated output


Prompt design can significantly alter the quality and format of language model outputs


Real-time systems require special attention to stream handling and frontend reactivity


Good team coordination and clear task delegation were essential to shipping on time



✅ What's next for Transcripto – from talk to task instantly
We aim to evolve Transcripto into a fully intelligent meeting companion by adding:

Integration with calendars (Google, Outlook) for automatic meeting capture


Native mobile apps for seamless on-the-go usage
