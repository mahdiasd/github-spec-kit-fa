import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
sections_dir = os.path.join(base_dir, "sections")
output_file = os.path.join(base_dir, "index.html")
artifact_file = r"C:\Users\Mahdi\.gemini\antigravity\brain\ef4e8351-e848-4a02-a1ef-47384b13fc9d\spec-kit-guide-fa.html"

files = [
    "section1_intro_concepts.html",
    "section2_setup_cli.html",
    "section3_step_by_step_new.html",
    "section4_step_by_step_existing.html",
    "section5_extra_commands.html",
    "section6_tips_and_troubleshooting.html"
]

def enhance_code_comments(html_str):
    """
    Finds all code blocks and wraps comment lines (starting with #)
    with a span that enforces the Vazirmatn Persian font and comfortable vertical spacing.
    """
    def code_block_sub(match):
        pre_open = match.group(1)
        code_body = match.group(2)
        lines = code_body.split('\n')
        new_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#') or stripped.startswith('//'):
                new_lines.append(f'<span class="code-comment">{line}</span>')
            else:
                new_lines.append(line)
        return f'{pre_open}<code>' + '\n'.join(new_lines) + '</code></pre>'

    return re.sub(r'(<pre[^>]*>)\s*<code>([\s\S]*?)</code>\s*</pre>', code_block_sub, html_str)

raw_body = ""
for f in files:
    f_path = os.path.join(sections_dir, f)
    with open(f_path, "r", encoding="utf-8") as s:
        raw_body += f"\n<!-- SECTION: {f} -->\n" + s.read() + "\n"

body_content = enhance_code_comments(raw_body)

template = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>راهنمای جامع و کاربردی GitHub Spec Kit | توسعه مبتنی بر مشخصات (SDD)</title>
  
  <!-- Fonts: Vazirmatn & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css">
  
  <style>
    /* CSS Design Tokens - Custom Ocean Steel & Rose Palette */
    :root, [data-theme="dark"] {{
      --bg-canvas: #090e13;
      --bg-surface: #0e161e;
      --bg-surface-elevated: #131e29;
      --bg-card: #0e161e;
      --bg-card-hover: #162432;
      --bg-code: #080d12;
      --code-header-bg: #0d151c;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-strong: rgba(255, 255, 255, 0.15);
      --border-accent: #41a6c4;
      
      --text-main: #f3f6f8;
      --text-muted: #9db1bf;
      --text-dim: #6a7f8e;
      
      --primary: #41a6c4;          /* Ocean Steel Blue */
      --primary-dark: #2f849e;
      --primary-light: #89c0b6;     /* Sage Mint */
      --primary-subtle: rgba(65, 166, 196, 0.12);
      --primary-glow: rgba(65, 166, 196, 0.25);
      
      --accent-pink: #e2adbd;       /* Soft Blush Pink */
      --accent-rose: #d484a0;       /* Dusty Rose */
      --accent-coral: #ed5371;      /* Vibrant Coral Crimson */
      --accent-amber: #e2adbd;      
      --accent-purple: #d484a0;
      --accent-cyan: #89c0b6;
      
      --hero-bg: linear-gradient(180deg, rgba(19, 30, 41, 0.95) 0%, rgba(14, 22, 30, 0.98) 100%);
      --hero-border: rgba(65, 166, 196, 0.28);
      
      --sidebar-width: 335px;
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 14px;
      --radius-xl: 18px;
    }}

    /* CSS Design Tokens - Light Theme */
    [data-theme="light"] {{
      --bg-canvas: #f6f9fb;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #edf4f7;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f7fa;
      --bg-code: #0b1218;
      --code-header-bg: #111b22;
      
      --border-subtle: #dfe8ed;
      --border-strong: #c5d7e0;
      --border-accent: #2f849e;
      
      --text-main: #0c1820;
      --text-muted: #435b6b;
      --text-dim: #677f8f;
      
      --primary: #2f849e;          /* Rich Ocean Blue */
      --primary-dark: #23697e;
      --primary-light: #41a6c4;
      --primary-subtle: rgba(65, 166, 196, 0.1);
      --primary-glow: rgba(65, 166, 196, 0.22);
      
      --accent-pink: #d484a0;
      --accent-rose: #d484a0;
      --accent-coral: #ed5371;
      --accent-amber: #d484a0;
      --accent-purple: #d484a0;
      --accent-cyan: #41a6c4;
      
      --hero-bg: linear-gradient(180deg, #ffffff 0%, #edf4f7 100%);
      --hero-border: rgba(65, 166, 196, 0.25);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      font-size: 16px;
      scrollbar-gutter: stable;
    }}

    body {{
      font-family: 'Vazirmatn', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Tahoma, sans-serif;
      background-color: var(--bg-canvas);
      color: var(--text-main);
      line-height: 1.95;
      direction: rtl;
      text-align: right;
      overflow-x: hidden;
      transition: background-color 0.2s ease, color 0.2s ease;
      -webkit-font-smoothing: antialiased;
    }}

    /* Scroll progress bar */
    #scroll-progress {{
      position: fixed;
      top: 0;
      right: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--primary), var(--primary-light), var(--accent-amber));
      z-index: 1000;
      transform-origin: 100% 50%;
      transform: scaleX(0);
      transition: transform 0.1s ease-out;
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 7px;
      height: 7px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-canvas);
    }}
    ::-webkit-scrollbar-thumb {{
      background: #273644;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #384e61;
    }}

    /* App Layout */
    .app-container {{
      display: flex;
      min-height: 100vh;
      position: relative;
    }}

    /* Mobile Header */
    .mobile-header {{
      display: none;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      padding: 0.9rem 1.4rem;
      position: sticky;
      top: 0;
      z-index: 100;
      align-items: center;
      justify-content: space-between;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .theme-toggle-btn {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-strong);
      color: var(--text-main);
      padding: 0.45rem 0.75rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-family: inherit;
      font-size: 0.82rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }}

    .theme-toggle-btn:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}

    .menu-toggle {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-strong);
      color: var(--text-main);
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-family: inherit;
      font-size: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }}

    /* Sidebar Navigation */
    .sidebar {{
      width: var(--sidebar-width);
      background: var(--bg-surface);
      border-left: 1px solid var(--border-subtle);
      height: 100vh;
      position: sticky;
      top: 0;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      z-index: 50;
      transition: background 0.2s ease, border-color 0.2s ease;
    }}

    .sidebar-header {{
      padding: 1.2rem 1.2rem 1rem;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .brand-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
    }}

    .brand-logo {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
    }}

    .brand-icon-box {{
      width: 36px;
      height: 36px;
      border-radius: 9px;
      background: var(--primary-subtle);
      border: 1px solid rgba(65, 166, 196, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
    }}

    .brand-text h1 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.3;
    }}

    .brand-text span {{
      font-size: 0.74rem;
      color: var(--text-dim);
      display: block;
      margin-top: 0.1rem;
    }}

    /* Search Box */
    .search-box {{
      margin-top: 1rem;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 0.6rem 0.9rem 0.6rem 2.3rem;
      color: var(--text-main);
      font-family: inherit;
      font-size: 0.84rem;
      outline: none;
      transition: all 0.15s ease;
    }}

    .search-input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 2px rgba(65, 166, 196, 0.2);
    }}

    .search-icon {{
      position: absolute;
      left: 0.8rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 0.9rem;
      pointer-events: none;
    }}

    /* Navigation List */
    .sidebar-nav {{
      flex: 1;
      overflow-y: auto;
      padding: 1rem 0.75rem 2rem;
      scroll-behavior: smooth;
    }}

    .nav-group-title {{
      font-size: 0.72rem;
      text-transform: uppercase;
      color: var(--text-dim);
      font-weight: 700;
      padding: 0.5rem 0.6rem 0.4rem;
      letter-spacing: 0.5px;
    }}

    .nav-section-group {{
      margin-bottom: 0.35rem;
    }}

    .nav-item {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.55rem 0.75rem;
      border-radius: var(--radius-sm);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.86rem;
      transition: all 0.15s ease;
      border: 1px solid transparent;
      line-height: 1.5;
    }}

    .nav-item:hover {{
      background: var(--bg-surface-elevated);
      color: var(--text-main);
    }}

    .nav-item.active {{
      background: var(--primary-subtle);
      color: var(--primary);
      font-weight: 700;
      border-color: rgba(65, 166, 196, 0.3);
    }}

    .nav-num {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 20px;
      height: 20px;
      border-radius: 4px;
      background: var(--bg-surface-elevated);
      color: var(--text-dim);
      font-size: 0.72rem;
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-weight: 600;
    }}

    .nav-item.active .nav-num {{
      background: rgba(65, 166, 196, 0.25);
      color: var(--primary);
    }}

    /* Nested Sub-navigation for Commands */
    .nav-sub-items {{
      margin-right: 0.9rem;
      padding-right: 0.65rem;
      border-right: 1.5px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
      margin-top: 0.25rem;
      margin-bottom: 0.6rem;
    }}

    .nav-sub-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      padding: 0.35rem 0.55rem;
      border-radius: var(--radius-sm);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.78rem;
      transition: all 0.15s ease;
      border: 1px solid transparent;
      line-height: 1.4;
    }}

    .nav-sub-item:hover {{
      background: var(--bg-surface-elevated);
      color: var(--text-main);
    }}

    .nav-sub-item.active {{
      background: var(--primary-subtle);
      color: var(--primary);
      font-weight: 600;
      border-color: rgba(65, 166, 196, 0.25);
    }}

    .nav-sub-item code {{
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-size: 0.72rem;
      color: var(--primary);
      background: var(--primary-subtle);
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
      direction: ltr;
      display: inline-block;
    }}

    .nav-sub-item .nav-sub-label {{
      font-size: 0.74rem;
      color: var(--text-dim);
      white-space: nowrap;
    }}

    .nav-sub-item:hover .nav-sub-label,
    .nav-sub-item.active .nav-sub-label {{
      color: var(--text-muted);
    }}

    /* Main Reading Area */
    .main-content {{
      flex: 1;
      max-width: 880px;
      padding: 3.5rem 3.5rem 7rem;
      margin: 0 auto;
    }}

    /* Engineering Hero Console with Stats Boxes */
    .hero-banner {{
      background: var(--hero-bg);
      border: 1px solid var(--hero-border);
      border-radius: var(--radius-xl);
      padding: 2.6rem 2.6rem 2.2rem;
      margin-bottom: 4rem;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.25);
    }}

    .hero-banner::after {{
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      left: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--primary), var(--accent-amber), transparent);
    }}

    .hero-tag-row {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }}

    .hero-status-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--primary-subtle);
      border: 1px solid rgba(65, 166, 196, 0.35);
      color: var(--primary);
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 700;
    }}

    .status-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--primary);
      box-shadow: 0 0 10px var(--primary);
      animation: pulse 2s infinite ease-in-out;
    }}

    @keyframes pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.5; transform: scale(0.8); }}
    }}

    .hero-badge {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      font-size: 0.76rem;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
    }}

    .hero-title {{
      font-size: 2.25rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 1rem;
      line-height: 1.35;
      letter-spacing: -0.01em;
    }}

    .hero-desc {{
      color: var(--text-muted);
      font-size: 1.08rem;
      line-height: 1.9;
      max-width: 800px;
      margin-bottom: 2rem;
    }}

    .hero-stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.4rem;
      border-top: 1px solid var(--border-subtle);
      padding-top: 1.6rem;
    }}

    .stat-item {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.1rem 1.3rem;
      transition: all 0.2s ease;
    }}

    .stat-item:hover {{
      border-color: rgba(65, 166, 196, 0.35);
      background: var(--bg-card-hover);
    }}

    .stat-item h4 {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 0.25rem;
      font-family: 'JetBrains Mono', 'Vazirmatn', monospace;
    }}

    .stat-item p {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.55;
    }}

    /* Section Styling */
    .doc-section {{
      margin-bottom: 6rem;
      scroll-margin-top: 5rem;
    }}

    .section-header {{
      margin-bottom: 2.8rem;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 1.8rem;
      position: relative;
    }}

    .badge-tag {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--primary-subtle);
      color: var(--primary);
      font-size: 0.76rem;
      font-weight: 700;
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-sm);
      margin-bottom: 0.8rem;
      font-family: 'JetBrains Mono', 'Vazirmatn', monospace;
    }}

    .section-header h2 {{
      font-size: 1.8rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 0.8rem;
      letter-spacing: -0.01em;
      line-height: 1.4;
    }}

    .section-lead {{
      color: var(--text-muted);
      font-size: 1.05rem;
      line-height: 1.9;
      max-width: 780px;
    }}

    .content-block {{
      margin-bottom: 3.8rem;
      scroll-margin-top: 5.5rem;
    }}

    .content-block h3 {{
      font-size: 1.32rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 2.8rem 0 1.1rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      letter-spacing: -0.01em;
    }}

    .content-block h4 {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text-main);
      margin: 2rem 0 0.85rem;
    }}

    .content-block p {{
      color: var(--text-muted);
      margin-bottom: 1.4rem;
      font-size: 1rem;
      line-height: 1.95;
    }}

    strong, b {{
      color: var(--text-main);
      font-weight: 600;
    }}

    .category-pill {{
      display: inline-block;
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--primary);
      background: var(--primary-subtle);
      border: 1px solid rgba(65, 166, 196, 0.25);
      padding: 0.2rem 0.65rem;
      border-radius: 20px;
      margin-bottom: 0.5rem;
    }}

    /* Elevated Callout Banners */
    .callout {{
      display: flex;
      gap: 1.1rem;
      padding: 1.25rem 1.6rem;
      border-radius: var(--radius-md);
      margin: 2rem 0;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      position: relative;
    }}

    .callout-icon {{
      font-size: 1.35rem;
      flex-shrink: 0;
      line-height: 1.4;
    }}

    .callout-body {{
      font-size: 0.94rem;
      color: var(--text-main);
      line-height: 1.85;
    }}

    .callout-body strong {{
      display: block;
      margin-bottom: 0.3rem;
      color: var(--text-main);
      font-size: 0.98rem;
    }}

    .callout-info {{
      border-right: 3px solid var(--primary);
    }}

    .callout-tip {{
      border-right: 3px solid var(--primary-light);
    }}

    .callout-warning {{
      border-right: 3px solid var(--accent-amber);
    }}

    .callout-important {{
      border-right: 3px solid var(--accent-rose);
    }}

    .callout-note {{
      border-right: 3px solid var(--accent-purple);
    }}

    /* Visual Workflow Diagrams (Section 3 & 4) */
    .diagram-caption {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .workflow-diagram {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      padding: 1.4rem 1.6rem;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      margin: 0.5rem 0 3rem;
      overflow-x: auto;
      scroll-behavior: smooth;
      direction: rtl;
      -webkit-overflow-scrolling: touch;
    }}

    .workflow-diagram::-webkit-scrollbar {{
      height: 6px;
    }}

    .workflow-diagram::-webkit-scrollbar-thumb {{
      background: rgba(65, 166, 196, 0.3);
      border-radius: 3px;
    }}

    .diagram-step {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-width: 110px;
      padding: 0.9rem 0.75rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      text-decoration: none;
      color: inherit;
      transition: all 0.2s ease;
      flex-shrink: 0;
      position: relative;
    }}

    .diagram-step:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(65, 166, 196, 0.15);
      background: var(--bg-card-hover);
    }}

    .diagram-step .step-num {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: var(--primary-subtle);
      color: var(--primary);
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 0.45rem;
      border: 1px solid rgba(65, 166, 196, 0.3);
    }}

    .diagram-step:hover .step-num {{
      background: var(--primary);
      color: #090c10;
    }}

    .diagram-step .step-title {{
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-main);
      font-family: 'JetBrains Mono', Consolas, monospace;
      direction: ltr;
      white-space: nowrap;
    }}

    .diagram-arrow {{
      color: var(--primary);
      opacity: 0.6;
      font-size: 1rem;
      flex-shrink: 0;
      transform: rotate(180deg);
      user-select: none;
    }}

    /* Paradigm Comparison Diagram (Section 1) */
    .paradigm-comparison {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.6rem;
      margin: 1rem 0 3rem;
    }}

    .paradigm-col {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.6rem;
      display: flex;
      flex-direction: column;
    }}

    .paradigm-col.vibe-coding {{
      border-top: 3px solid var(--accent-rose);
    }}

    .paradigm-col.sdd-coding {{
      border-top: 3px solid var(--primary);
    }}

    .paradigm-header {{
      margin-bottom: 1.4rem;
      text-align: center;
    }}

    .paradigm-badge {{
      display: inline-block;
      font-size: 0.82rem;
      font-weight: 700;
      padding: 0.35rem 0.9rem;
      border-radius: 20px;
    }}

    .paradigm-badge.bad {{
      background: rgba(244, 63, 94, 0.12);
      color: var(--accent-rose);
      border: 1px solid rgba(244, 63, 94, 0.3);
    }}

    .paradigm-badge.good {{
      background: var(--primary-subtle);
      color: var(--primary);
      border: 1px solid rgba(65, 166, 196, 0.35);
    }}

    .flow-steps {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.55rem;
    }}

    .flow-node {{
      width: 100%;
      padding: 0.75rem 1rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      font-size: 0.88rem;
      text-align: center;
      color: var(--text-main);
      font-weight: 500;
    }}

    .flow-node.danger {{
      border-color: rgba(244, 63, 94, 0.4);
      background: rgba(244, 63, 94, 0.08);
      color: #fca5a5;
      font-weight: 700;
    }}

    .flow-node.success {{
      border-color: rgba(65, 166, 196, 0.4);
      background: var(--primary-subtle);
      color: var(--primary);
      font-weight: 700;
    }}

    .flow-arrow {{
      color: var(--text-dim);
      font-size: 0.95rem;
      opacity: 0.7;
    }}

    /* Grid Concept Cards */
    .grid-cards {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.4rem;
      margin: 2rem 0;
    }}

    .concept-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.6rem;
      transition: all 0.22s ease;
      position: relative;
    }}

    .concept-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(65, 166, 196, 0.12);
      background: var(--bg-card-hover);
    }}

    .concept-card.border-green {{
      border-right: 3px solid var(--primary);
    }}

    .concept-card.border-amber {{
      border-right: 3px solid var(--accent-amber);
    }}

    .card-icon {{
      font-size: 1.8rem;
      margin-bottom: 0.85rem;
    }}

    .concept-card h4 {{
      font-size: 1.1rem;
      color: var(--text-main);
      margin-bottom: 0.5rem;
      font-weight: 700;
    }}

    .concept-card p {{
      font-size: 0.92rem;
      color: var(--text-muted);
      margin: 0;
      line-height: 1.8;
    }}

    /* Terminology List */
    .term-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.4rem 1.6rem;
      margin-bottom: 1.2rem;
      transition: all 0.2s ease;
    }}

    .term-item:hover {{
      border-color: var(--primary);
      background: var(--bg-card-hover);
    }}

    .term-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.6rem;
    }}

    .term-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary);
      font-family: 'JetBrains Mono', 'Vazirmatn', monospace;
    }}

    .term-tag {{
      font-size: 0.74rem;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-dim);
    }}

    .term-desc {{
      font-size: 0.94rem;
      color: var(--text-muted);
      margin: 0;
      line-height: 1.85;
    }}

    .rule-highlight {{
      color: var(--accent-amber);
      font-weight: 600;
    }}

    /* Code Container & Terminal Mockup */
    .code-container {{
      background: var(--bg-code);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      margin: 2rem 0;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }}

    .code-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.65rem 1.1rem;
      background: var(--code-header-bg);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      direction: ltr;
    }}

    .terminal-dots {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      display: inline-block;
      opacity: 0.85;
    }}
    .dot.red {{ background: #ef4444; }}
    .dot.yellow {{ background: #f59e0b; }}
    .dot.green {{ background: #89c0b6; }}

    .code-lang {{
      color: #9ca3af;
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-size: 0.72rem;
      letter-spacing: 0.5px;
      font-weight: 600;
      background: rgba(255, 255, 255, 0.05);
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
    }}

    .copy-btn {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      border-radius: var(--radius-sm);
      padding: 0.3rem 0.75rem;
      font-size: 0.76rem;
      cursor: pointer;
      font-family: 'Vazirmatn', sans-serif;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .copy-btn:hover {{
      background: var(--primary-subtle);
      color: var(--primary-light);
      border-color: rgba(65, 166, 196, 0.4);
    }}

    pre {{
      margin: 0;
      padding: 1.3rem 1.6rem;
      overflow-x: auto;
      direction: ltr;
      text-align: left;
      font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
      font-size: 0.88rem;
      line-height: 1.8;
      color: #e5e7eb;
      tab-size: 2;
    }}

    code {{
      font-family: inherit;
    }}

    /* Persian Comments inside Code Blocks - Vazirmatn Luminous Mint */
    .code-comment {{
      display: block;
      font-family: 'Vazirmatn', -apple-system, BlinkMacSystemFont, Tahoma, sans-serif !important;
      font-size: 0.86rem;
      font-weight: 500;
      color: #89c0b6;
      line-height: 1.85;
      margin-top: 0.65rem;
      margin-bottom: 0.25rem;
      direction: ltr;
      text-align: left;
      letter-spacing: normal;
    }}

    [data-theme="light"] .code-comment {{
      color: #2f849e;
    }}

    code > .code-comment:first-child {{
      margin-top: 0;
    }}

    p code, li code, td code {{
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-size: 0.84em;
      color: var(--primary);
      background: var(--primary-subtle);
      padding: 0.15em 0.45em;
      border-radius: 4px;
      direction: ltr;
      display: inline-block;
    }}

    /* Tables */
    .table-container {{
      overflow-x: auto;
      margin: 2rem 0;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      background: var(--bg-surface);
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: right;
      font-size: 0.92rem;
    }}

    th {{
      background: var(--bg-surface-elevated);
      color: var(--text-main);
      padding: 0.9rem 1.2rem;
      font-weight: 700;
      border-bottom: 1px solid var(--border-strong);
    }}

    td {{
      padding: 0.9rem 1.2rem;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-muted);
      line-height: 1.8;
    }}

    tr:last-child td {{
      border-bottom: none;
    }}

    tr:hover td {{
      background: var(--bg-card-hover);
    }}

    /* Step Timeline in Section 3 & 4 */
    .step-timeline {{
      margin: 2.5rem 0;
      position: relative;
    }}

    .step-timeline::before {{
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      right: 18px;
      width: 2px;
      background: var(--border-strong);
    }}

    .step-entry {{
      position: relative;
      padding-right: 3.2rem;
      margin-bottom: 2.5rem;
    }}

    .step-entry:last-child {{
      margin-bottom: 0;
    }}

    .step-marker {{
      position: absolute;
      right: 6px;
      top: 0.15rem;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--bg-canvas);
      border: 2px solid var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--primary);
      font-family: 'JetBrains Mono', monospace;
    }}

    .step-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.45rem;
    }}

    .step-desc {{
      color: var(--text-muted);
      font-size: 0.95rem;
      line-height: 1.85;
    }}

    /* Lists */
    ul, ol {{
      margin: 1rem 0 1.5rem 0;
      padding-right: 1.5rem;
      color: var(--text-muted);
    }}

    li {{
      margin-bottom: 0.6rem;
      line-height: 1.85;
    }}

    /* Footer & Author Attribution */
    .doc-footer {{
      border-top: 1px solid var(--border-subtle);
      padding-top: 3rem;
      margin-top: 6rem;
      text-align: center;
      color: var(--text-dim);
      font-size: 0.88rem;
      line-height: 1.9;
    }}

    .author-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: var(--bg-surface-elevated);
      border: 1px solid rgba(65, 166, 196, 0.35);
      padding: 0.5rem 1.25rem;
      border-radius: 30px;
      margin-bottom: 0.9rem;
    }}

    .author-label {{
      color: var(--text-dim);
      font-size: 0.84rem;
    }}

    .author-name {{
      color: var(--primary);
      font-weight: 700;
      font-size: 0.96rem;
      text-decoration: none;
      transition: color 0.15s ease;
    }}

    .author-name:hover {{
      color: var(--accent-pink);
      text-decoration: underline;
    }}

    .author-social-links {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      margin-top: 0.2rem;
      margin-bottom: 1.2rem;
    }}

    .author-social-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.85rem;
      border-radius: 20px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.8rem;
      font-family: 'JetBrains Mono', 'Vazirmatn', monospace;
      direction: ltr;
      transition: all 0.2s ease;
    }}

    .author-social-link:hover {{
      border-color: var(--primary);
      color: var(--primary);
      background: var(--primary-subtle);
      transform: translateY(-1px);
    }}

    /* Mobile Responsiveness */
    @media (max-width: 860px) {{
      .mobile-header {{
        display: flex;
      }}
      
      .sidebar {{
        position: fixed;
        right: -100%;
        top: 0;
        bottom: 0;
        width: 310px;
        transition: right 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: -10px 0 30px rgba(0, 0, 0, 0.4);
      }}
      
      .sidebar.open {{
        right: 0;
      }}
      
      .main-content {{
        padding: 2rem 1.4rem 5rem;
        max-width: 100%;
      }}
      
      .hero-title {{
        font-size: 1.75rem;
      }}

      .hero-stats {{
        grid-template-columns: 1fr;
        gap: 0.8rem;
      }}

      .paradigm-comparison {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Scroll Progress Indicator -->
  <div id="scroll-progress"></div>

  <!-- Mobile Header Bar -->
  <header class="mobile-header">
    <div class="brand-logo">
      <div class="brand-icon-box">🌱</div>
      <div class="brand-text">
        <h1>Spec Kit</h1>
      </div>
    </div>
    <div class="header-actions">
      <button class="theme-toggle-btn" onclick="toggleTheme()" title="تغییر تم">
        <span class="theme-icon">🌙</span>
      </button>
      <button class="menu-toggle" onclick="toggleSidebar()">فهرست ☰</button>
    </div>
  </header>

  <div class="app-container">

    <!-- Unified Interactive Sidebar -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <div class="brand-row">
          <a href="#" class="brand-logo">
            <div class="brand-icon-box">🌱</div>
            <div class="brand-text">
              <h1>GitHub Spec Kit</h1>
              <span>راهنمای جامع توسعه مبتنی بر مشخصات</span>
            </div>
          </a>
          <button class="theme-toggle-btn" onclick="toggleTheme()" title="تغییر تم بین تاریک و روشن">
            <span class="theme-icon">🌙</span>
          </button>
        </div>

        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" id="search-input" class="search-input" placeholder="جستجوی دستور، مفهوم یا بخش..." onkeyup="filterNavigation()">
        </div>
      </div>

      <nav class="sidebar-nav" id="sidebar-nav">
        <div class="nav-group-title">سرفصل‌ها و دستورات</div>
        
        <!-- Section 01 -->
        <div class="nav-section-group">
          <a href="#intro-concepts" class="nav-item active" onclick="selectNav(this)">
            <span class="nav-num">01</span>
            <span>مقدمه، فلسفه SDD و واژه‌نامه</span>
          </a>
        </div>

        <!-- Section 02 -->
        <div class="nav-section-group">
          <a href="#setup-cli" class="nav-item" onclick="selectNav(this)">
            <span class="nav-num">02</span>
            <span>پیش‌نیازها و نصب CLI</span>
          </a>
        </div>

        <!-- Section 03 -->
        <div class="nav-section-group">
          <a href="#step-by-step-new" class="nav-item" onclick="selectNav(this)">
            <span class="nav-num">03</span>
            <span>پروژه جدید (Greenfield)</span>
          </a>
          <div class="nav-sub-items">
            <a href="#cmd-init" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify init</code>
              <span class="nav-sub-label">گام ۰: راه‌اندازی</span>
            </a>
            <a href="#cmd-constitution" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.constitution</code>
              <span class="nav-sub-label">گام ۱: قانون اساسی</span>
            </a>
            <a href="#cmd-specify" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.specify</code>
              <span class="nav-sub-label">گام ۲: نیازمندی‌ها</span>
            </a>
            <a href="#cmd-clarify" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.clarify</code>
              <span class="nav-sub-label">گام ۳: رفع ابهام</span>
            </a>
            <a href="#cmd-plan" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.plan</code>
              <span class="nav-sub-label">گام ۴: معماری</span>
            </a>
            <a href="#cmd-checklist" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.checklist</code>
              <span class="nav-sub-label">گام ۵: چک‌لیست شروط</span>
            </a>
            <a href="#cmd-tasks" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.tasks</code>
              <span class="nav-sub-label">گام ۶: وظایف اجرایی</span>
            </a>
            <a href="#cmd-analyze" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.analyze</code>
              <span class="nav-sub-label">گام ۷: تحلیل انطباق</span>
            </a>
            <a href="#cmd-implement" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.implement</code>
              <span class="nav-sub-label">گام ۸: کدنویسی خودکار</span>
            </a>
            <a href="#cmd-converge" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.converge</code>
              <span class="nav-sub-label">گام ۹: تست و همگرایی</span>
            </a>
          </div>
        </div>

        <!-- Section 04 -->
        <div class="nav-section-group">
          <a href="#step-by-step-existing" class="nav-item" onclick="selectNav(this)">
            <span class="nav-num">04</span>
            <span>پروژه موجود (Brownfield)</span>
          </a>
          <div class="nav-sub-items">
            <a href="#cmd-bf-init" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify init --existing</code>
              <span class="nav-sub-label">گام ۱: استقرار امن</span>
            </a>
            <a href="#cmd-bf-constitution" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.constitution</code>
              <span class="nav-sub-label">گام ۲: خطوط قرمز</span>
            </a>
            <a href="#cmd-bf-specify" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.specify</code>
              <span class="nav-sub-label">گام ۳: فیچر جدید</span>
            </a>
            <a href="#cmd-bf-plan" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.plan</code>
              <span class="nav-sub-label">گام ۴: اتصال سیستم</span>
            </a>
            <a href="#cmd-bf-tasks-implement" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.tasks & implement</code>
              <span class="nav-sub-label">گام ۵: ساخت محتاط</span>
            </a>
          </div>
        </div>

        <!-- Section 05 -->
        <div class="nav-section-group">
          <a href="#extra-commands" class="nav-item" onclick="selectNav(this)">
            <span class="nav-num">05</span>
            <span>دستورات پیشرفته و افزونه‌ها</span>
          </a>
          <div class="nav-sub-items">
            <a href="#cmd-ext-bug" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.bug.assess</code>
              <span class="nav-sub-label">مدیریت باگ</span>
            </a>
            <a href="#cmd-ext-assess" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.assess</code>
              <span class="nav-sub-label">سنجش ایده</span>
            </a>
            <a href="#cmd-ext-git" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.git.checkpoint</code>
              <span class="nav-sub-label">مدیریت گیت</span>
            </a>
            <a href="#cmd-ext-agent-context" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>/speckit.agent-context</code>
              <span class="nav-sub-label">کانتکست ایجنت</span>
            </a>
            <a href="#cmd-integration" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify integration</code>
              <span class="nav-sub-label">مدیریت ایجنت‌ها</span>
            </a>
            <a href="#cmd-extension" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify extension</code>
              <span class="nav-sub-label">اکستنشن‌ها</span>
            </a>
            <a href="#cmd-preset" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify preset</code>
              <span class="nav-sub-label">پریست‌ها</span>
            </a>
            <a href="#cmd-bundle" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify bundle</code>
              <span class="nav-sub-label">بسته‌های نقشی</span>
            </a>
            <a href="#cmd-workflow" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify workflow</code>
              <span class="nav-sub-label">موتور پایپ‌لاین</span>
            </a>
            <a href="#cmd-artifact" class="nav-sub-item" onclick="selectSubNav(this)">
              <code>specify artifact</code>
              <span class="nav-sub-label">بازرسی عمیق</span>
            </a>
          </div>
        </div>

        <!-- Section 06 -->
        <div class="nav-section-group">
          <a href="#tips-troubleshooting" class="nav-item" onclick="selectNav(this)">
            <span class="nav-num">06</span>
            <span>نکات طلایی و رفع اشکال</span>
          </a>
        </div>
      </nav>
    </aside>

    <!-- Main Content Container -->
    <main class="main-content">

      <!-- Engineering Hero Console with Restored Stats Boxes -->
      <header class="hero-banner">
        <div class="hero-tag-row">
          <div class="hero-status-pill">
            <span class="status-dot"></span>
            <span>محیط پایدار نسخه ۱.۰.۰</span>
          </div>
          <span class="hero-badge">Spec-Driven Development</span>
          <span class="hero-badge">Human-In-The-Loop</span>
        </div>
        <h1 class="hero-title">راهنمای جامع و کاربردی GitHub Spec Kit</h1>
        <p class="hero-desc">
          توسعه نرم‌افزار حرفه‌ای، مستند و بدون خطا با تمام ایجنت‌های هوش مصنوعی. تعریف دقیق «آنچه باید ساخته شود» پیش از آنکه دست به کد ببرید.
        </p>
        <div class="hero-stats">
          <div class="stat-item">
            <h4>۳۰+ Agent</h4>
            <p>سازگار با تمام ابزارهای مطرح هوش مصنوعی</p>
          </div>
          <div class="stat-item">
            <h4>۰٪ توهم و حدس</h4>
            <p>تثبیت مشخصات پیش از آغاز کدنویسی</p>
          </div>
          <div class="stat-item">
            <h4>۱۰۰٪ همگرایی</h4>
            <p>تضمین انطباق کامل کدهای خروجی با نیازها</p>
          </div>
        </div>
      </header>

      <!-- Included Sections Content -->
      {body_content}

      <!-- Footer & Author Attribution -->
      <footer class="doc-footer">
        <div class="author-badge">
          <span class="author-label">تهیه و تدوین:</span>
          <a href="https://github.com/mahdiasd" target="_blank" rel="noopener" class="author-name">مهدی اسداله پور</a>
        </div>
        <div class="author-social-links">
          <a href="https://github.com/mahdiasd" target="_blank" rel="noopener" class="author-social-link">
            <span>GitHub</span>
            <span>↗</span>
          </a>
          <a href="https://www.linkedin.com/in/mahdiasd96/" target="_blank" rel="noopener" class="author-social-link">
            <span>LinkedIn</span>
            <span>↗</span>
          </a>
        </div>
        <p>مستندسازی و تالیف اختصاصی به زبان فارسی برای مهندسان نرم‌افزار و تیم‌های فنی</p>
        <p style="margin-top: 0.4rem; opacity: 0.75;">بر اساس پروژه متن‌باز <a href="https://github.com/github/spec-kit" target="_blank" rel="noopener" style="color: var(--primary); text-decoration: none;">github/spec-kit</a> و پژوهش‌های John Lam</p>
        <p style="margin-top: 0.5rem; font-size: 0.82rem; opacity: 0.85;">با تشکر ویژه از <a href="https://www.youtube.com/@iampedi" target="_blank" rel="noopener" style="color: var(--accent-pink); font-weight: 600; text-decoration: none;">iampedi</a> برای آموزش و ویدیوی عالی درباره این ابزار</p>
      </footer>

    </main>
  </div>

  <script>
    // Copy Code to Clipboard with tactile feedback
    function copyCode(button) {{
      const container = button.closest('.code-container');
      const pre = container.querySelector('pre');
      const code = pre.innerText;
      
      navigator.clipboard.writeText(code).then(() => {{
        const originalText = button.innerHTML;
        button.innerHTML = 'کپی شد! ✓';
        button.style.color = '#41a6c4';
        button.style.borderColor = '#41a6c4';
        button.style.background = 'rgba(65, 166, 196, 0.2)';
        
        setTimeout(() => {{
          button.innerHTML = originalText;
          button.style.color = '';
          button.style.borderColor = '';
          button.style.background = '';
        }}, 2000);
      }}).catch(err => {{
        console.error('Failed to copy code: ', err);
      }});
    }}

    // Inject macOS terminal dots into all code containers automatically
    document.querySelectorAll('.code-header').forEach(header => {{
      if (!header.querySelector('.terminal-dots')) {{
        const dots = document.createElement('div');
        dots.className = 'terminal-dots';
        dots.innerHTML = '<span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span>';
        header.insertBefore(dots, header.firstChild);
      }}
    }});

    // Theme Toggle Logic with LocalStorage persistence
    function applyTheme(theme) {{
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('speckit_theme', theme);
      document.querySelectorAll('.theme-toggle-btn .theme-icon').forEach(icon => {{
        icon.innerText = (theme === 'light') ? '☀️' : '🌙';
      }});
    }}

    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const next = (current === 'dark') ? 'light' : 'dark';
      applyTheme(next);
    }}

    // Initialize theme on load
    (function initTheme() {{
      const saved = localStorage.getItem('speckit_theme');
      if (saved) {{
        applyTheme(saved);
      }} else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {{
        applyTheme('light');
      }} else {{
        applyTheme('dark');
      }}
    }})();

    // Scroll Progress Indicator
    window.addEventListener('scroll', () => {{
      const winScroll = document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) : 0;
      const bar = document.getElementById('scroll-progress');
      if (bar) {{
        bar.style.transform = `scaleX(${{scrolled}})`;
      }}
    }});

    // Mobile Sidebar Toggle
    function toggleSidebar() {{
      const sidebar = document.getElementById('sidebar');
      sidebar.classList.toggle('open');
    }}

    // Close mobile sidebar on link click
    function selectNav(element) {{
      document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-sub-item').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
      const sidebar = document.getElementById('sidebar');
      if (window.innerWidth <= 860) {{
        sidebar.classList.remove('open');
      }}
    }}

    // Direct command sub-item click handler
    function selectSubNav(element) {{
      document.querySelectorAll('.nav-sub-item').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
      const parentGroup = element.closest('.nav-section-group');
      if (parentGroup) {{
        const parentLink = parentGroup.querySelector('.nav-item');
        if (parentLink) {{
          document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
          parentLink.classList.add('active');
        }}
      }}
      const sidebar = document.getElementById('sidebar');
      if (window.innerWidth <= 860) {{
        sidebar.classList.remove('open');
      }}
    }}

    // Realtime search filter across sections and nested commands
    function filterNavigation() {{
      const query = document.getElementById('search-input').value.toLowerCase().trim();
      const groups = document.querySelectorAll('.nav-section-group');
      
      groups.forEach(group => {{
        const parentItem = group.querySelector('.nav-item');
        const subItems = group.querySelectorAll('.nav-sub-item');
        let anySubMatch = false;

        subItems.forEach(sub => {{
          const text = sub.innerText.toLowerCase();
          if (query === '' || text.includes(query)) {{
            sub.style.display = 'flex';
            if (query !== '' && text.includes(query)) {{
              anySubMatch = true;
            }}
          }} else {{
            sub.style.display = 'none';
          }}
        }});

        const parentText = parentItem ? parentItem.innerText.toLowerCase() : '';
        const parentMatches = query === '' || parentText.includes(query);

        if (parentMatches || anySubMatch) {{
          group.style.display = 'block';
          if (parentItem) parentItem.style.display = 'flex';
          if (parentMatches && query !== '') {{
            subItems.forEach(sub => sub.style.display = 'flex');
          }}
        }} else {{
          group.style.display = 'none';
        }}
      }});
    }}

    // Active Scrollspy navigation
    window.addEventListener('scroll', () => {{
      const sections = document.querySelectorAll('.doc-section');
      const scrollPos = window.scrollY + 160;
      
      sections.forEach(section => {{
        const top = section.offsetTop;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');
        
        if (scrollPos >= top && scrollPos < top + height) {{
          document.querySelectorAll('.sidebar-nav .nav-item').forEach(link => {{
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + id) {{
              link.classList.add('active');
            }}
          }});
        }}
      }});
    }});
  </script>
</body>
</html>"""

# Write to current workspace index.html
with open(output_file, "w", encoding="utf-8") as out:
    out.write(template)

# Also write to Antigravity artifact directory
try:
    with open(artifact_file, "w", encoding="utf-8") as out:
        out.write(template)
    print("SUCCESS! Written to both:", output_file, "and", artifact_file)
except Exception as e:
    print("Artifact write note:", e)

print("Size of master index.html:", os.path.getsize(output_file), "bytes")
