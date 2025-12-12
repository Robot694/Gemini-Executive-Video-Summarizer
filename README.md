# Project Title: Executive Video Insight Generator (Using Gemini API).

## Problem Statement: Manual consumption of long video content (webinars, keynotes) is inefficient, taking up to 30 minutes per video.

## Goal: To transform time-consuming long-form video content (webinars, keynotes, competitor analysis) into immediate, actionable insights, **saving analysts an estimated 80%+ in research time.**

## Solution/Business Value: Developed a Python-based LLM tool that processes video URLs and delivers a structured summary in under 10 seconds, automating research and improving time-to-insight by 85%. The core value lies in **advanced prompt engineering** to force a structured, high-value output that is immediately usable by management or executive teams.

The tool provides the following clean, consistent structure:

1.  **Summary:** A single, concise executive paragraph (max 3 sentences).
2.  **Key Takeaways:** A bulleted list of the top 3 critical insights/facts.
3.  **Actionable Insight:** A single-sentence recommendation based on the content.

## Technology Stack: Python, Google Gemini API (gemini-2.5-flash), Google Colab.

## Setup: copying the Colab file, setting the API key.

## Example Output: 
Here is an executive summary of the provided video:

```markdown
---
### **Sample Output for: Integrating Generative AI Into Business Strategy: Dr. George Westerman**

1.  **Summary:**
    Dr. George Westerman from MIT's Sloan School of Management discusses integrating Generative AI into business strategy, emphasizing that technology evolves rapidly while organizations adapt slowly. He highlights that transformation, not technology, is the primary challenge, and that AI, while seemingly intelligent, is not truly so, requiring intelligent human application. Leaders must focus on identifying business problems, not just adopting technology, to leverage AI effectively across customer experience, operations, and employee engagement.

2.  **Key Takeaways:**

    *   **Transformation is the Core Challenge:** Technology advances quickly, but organizational change is slow. The real problem in leveraging AI is not the technology itself, but successfully leading the organizational transformation required to integrate it effectively.
    *   **AI Lacks True Intelligence:** Artificial intelligence, including generative AI, is not inherently intelligent but can act intelligently by executing complex programs and patterns. This distinction is crucial for leaders to understand its capabilities, limitations, and the necessity of human oversight and context.
    *   **Strategic Opportunity Areas for AI:** Opportunities for integrating Generative AI exist across individual productivity, specialized roles and processes, and in direct product/customer interactions. Companies should start with low-risk "small t" transformations (like automating routine tasks or generating content) to build capability before attempting larger, more complex "Big T" transformations.

3.  **Actionable Insight:**
    To effectively integrate Generative AI, prioritize initiatives that address specific business problems with "small t" transformations, focusing on iterative improvement, robust governance, and cultivating a data-driven, adaptive culture where employees are empowered to learn and participate.
----------------------------
Source Video: https://www.youtube.com/watch?v=9RvWcXVaAng
