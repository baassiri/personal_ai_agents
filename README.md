Automation/
│
├── agents/
│   ├── caption_agent.py
│   ├── post_agent.py
│   ├── tiktok_agent.py
│   └── __init__.py
│
├── ai_engine/
│   ├── content_generator.py
│   └── __init__.py
│
├── platforms/
│   ├── instagram.py
│   ├── tiktok.py
│   ├── twitter.py
│   └── __init__.py
│
├── scheduler/
│   ├── scheduler_agent.py
│   └── __init__.py
│
├── utils/
│   ├── video_tools.py
│   ├── file_manager.py
│   └── __init__.py
│
├── outbox/                  # Where generated posts or videos go
│
├── .env
├── main.py                  # Control center to run agents
├── requirements.txt
└── README.md
